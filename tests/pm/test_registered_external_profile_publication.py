"""PM may edit exact config files of registered external profiles, not arbitrary paths."""
from __future__ import annotations

import pytest

from hermes_cli.runtime_state import finish_publication, recover_publication
from hermes_constants import mark_named_profile_deleted
from pm import paths
from pm.environments import install_state_dir
from pm.publication import PluginSelection


@pytest.fixture
def registered(tmp_path, monkeypatch):
    home = tmp_path / "home"
    profiles = home / "profiles"
    profiles.mkdir(parents=True)
    external = tmp_path / "queue" / "worker"
    external.mkdir(parents=True)
    original = b"plugins:\n  enabled: [old]\n"
    (external / "config.yaml").write_bytes(original)
    link = profiles / "worker"
    link.symlink_to(external, target_is_directory=True)
    project = tmp_path / "repo"
    project.mkdir()
    monkeypatch.setenv("HERMES_HOME", str(home))
    monkeypatch.setattr(paths, "repo_root", lambda: project)
    return external, link, project, original


def selection(home):
    return PluginSelection({"home": str(home), "enabled": ["new"], "disabled": []})


@pytest.mark.parametrize("commit", [False, True])
def test_registered_external_profile_publication_and_recovery(registered, commit):
    external, _link, project, original = registered
    selection(external).publish(project)
    published = (external / "config.yaml").read_bytes()
    assert published != original
    if commit:
        finish_publication(project)
    else:
        recover_publication(project)
    assert (external / "config.yaml").read_bytes() == (published if commit else original)
    assert not (install_state_dir(project) / "publication.json").exists()


@pytest.mark.parametrize("kind", ["unregistered", "invalid-id", "tombstoned"])
def test_invalid_registration_does_not_authorize_external_config(registered, kind):
    external, link, _project, _original = registered
    invalidate = {
        "unregistered": link.unlink,
        "invalid-id": lambda: link.rename(link.with_name("Bad Name")),
        "tombstoned": lambda: mark_named_profile_deleted(link),
    }
    invalidate[kind]()
    with pytest.raises(ValueError, match="outside Hermes state"):
        selection(external)


@pytest.mark.parametrize("kind", ["sibling", "nested"])
def test_registration_does_not_authorize_other_external_directories(registered, kind):
    external, _link, _project, _original = registered
    target = external.parent / "sibling" if kind == "sibling" else external / "nested"
    target.mkdir()
    (target / "config.yaml").write_text("plugins: {}\n")
    with pytest.raises(ValueError, match="outside Hermes state"):
        selection(target)


@pytest.mark.parametrize("dangling", [False, True])
def test_missing_profile_marker_does_not_authorize_external_config(registered, dangling):
    external, _link, _project, _original = registered
    (external / "config.yaml").unlink()
    if dangling:
        external.rmdir()
    with pytest.raises(ValueError, match="outside Hermes state"):
        selection(external)


def test_external_config_symlink_cannot_escape_registered_home(registered, tmp_path):
    external, _link, _project, _original = registered
    (external / "config.yaml").unlink()
    outside = tmp_path / "outside.yaml"
    outside.write_text("plugins: {}\n")
    (external / "config.yaml").symlink_to(outside)
    with pytest.raises(ValueError, match="outside Hermes state"):
        selection(external)


@pytest.mark.parametrize("change", ["remove", "retarget"])
def test_registration_changes_block_recovery_and_preserve_journal(registered, tmp_path, change):
    external, link, project, _original = registered
    selection(external).publish(project)
    published = (external / "config.yaml").read_bytes()
    link.unlink()
    if change == "retarget":
        replacement = tmp_path / "replacement"
        replacement.mkdir()
        (replacement / "config.yaml").write_text("plugins: {}\n")
        link.symlink_to(replacement, target_is_directory=True)
    with pytest.raises(RuntimeError, match="outside Hermes state"):
        recover_publication(project)
    assert (external / "config.yaml").read_bytes() == published
    assert (install_state_dir(project) / "publication.json").exists()
