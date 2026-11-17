"""A suspended turn may renew its unclaimed row, but never a successor's lease."""

import sqlite3
import time
from types import SimpleNamespace

import pytest

import hermes_state_compression
from agent import turn_facade_lease
from hermes_state import SessionDB


@pytest.fixture
def suspended_lease(tmp_path, monkeypatch):
    now = [1000.0]
    clock = SimpleNamespace(time=lambda: now[0], monotonic=time.monotonic, sleep=time.sleep)
    monkeypatch.setattr(turn_facade_lease, "time", clock)
    monkeypatch.setattr(hermes_state_compression, "time", clock)
    db = SessionDB(tmp_path / "state.db")
    db.create_session("s1", source="test")
    assert db.try_acquire_session_turn_lease("s1", "original")
    interruptions = []
    agent = SimpleNamespace(session_id="s1", interrupt=lambda msg, **kw: interruptions.append(msg))
    lease = turn_facade_lease.DurableTurnLease(
        agent, db, "s1", "original", expires_at=db.session_turn_lease_expires_at("s1", "original")
    )
    lease.turn_active = True
    now[0] += 478.0  # Flowhaven's thermal sleep exceeded the five-minute TTL.
    yield db, lease, interruptions
    db.close()


@pytest.mark.parametrize("row_state", ["expired", "renewed_by_append", "reclaimed"])
def test_late_callback_checks_durable_holder_before_stopping(suspended_lease, row_state):
    db, lease, interruptions = suspended_lease
    if row_state == "renewed_by_append":
        db.append_messages_batch("s1", [{"role": "assistant", "content": "after wake"}],
                                 turn_lease_holder="original")
    elif row_state == "reclaimed":
        assert db.try_acquire_session_turn_lease("s1", "successor")

    result = lease.refresh_tick()

    if row_state == "reclaimed":
        assert result is False and len(interruptions) == 1
        assert db.session_turn_lease_expires_at("s1", "original") is None
        assert db.session_turn_lease_expires_at("s1", "successor") == 1778.0
    else:
        assert result is None and interruptions == []
        assert lease._authority_deadline == db.session_turn_lease_expires_at("s1", "original") == 1778.0
        assert not db.try_acquire_session_turn_lease("s1", "successor")


def test_late_callback_cannot_wait_through_a_locked_database(suspended_lease):
    db, lease, interruptions = suspended_lease
    # A real second connection owns the WAL writer slot; no retry sleep is needed.
    db._conn.execute("PRAGMA busy_timeout=0")
    blocker = sqlite3.connect(db.db_path, timeout=0)
    blocker.execute("BEGIN IMMEDIATE")
    try:
        assert lease.refresh_tick() is False
        assert len(interruptions) == 1
        assert lease._authority_deadline == 1300.0
    finally:
        blocker.rollback()
        blocker.close()
