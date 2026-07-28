# Langfuse Observability Plugin

This plugin ships bundled with Hermes but is **opt-in** — it only loads when
you explicitly enable it.

## Enable

Pick one:

```bash
# Interactive: walks you through credentials + SDK install + enable
hermes tools  # → Langfuse Observability

# Manual
pip install langfuse
hermes plugins enable observability/langfuse
```

## Required credentials

Set these in `~/.hermes/.env` (or via `hermes tools`):

```bash
HERMES_LANGFUSE_PUBLIC_KEY=pk-lf-...
HERMES_LANGFUSE_SECRET_KEY=sk-lf-...
HERMES_LANGFUSE_BASE_URL=https://cloud.langfuse.com   # or your self-hosted URL
```

Without the SDK or credentials the hooks no-op silently — the plugin fails
open.

## Verify

```bash
hermes plugins list                 # observability/langfuse should show "enabled"
hermes chat -q "hello"              # then check Langfuse for a "Hermes turn" trace
```

## Optional tuning

```bash
HERMES_LANGFUSE_ENV=production       # environment tag
HERMES_LANGFUSE_RELEASE=v1.0.0       # release tag
HERMES_LANGFUSE_SAMPLE_RATE=0.5      # sample 50% of traces
HERMES_LANGFUSE_MAX_CHARS=12000      # max chars per field (default: 12000)
HERMES_LANGFUSE_FLUSH_EVERY_TOOLS=5  # completed tools before a live flush
HERMES_LANGFUSE_FLUSH_INTERVAL_S=5   # max seconds between live tool flushes
HERMES_LANGFUSE_DEBUG=true           # verbose plugin logging
```

## Tool outcome telemetry

Each tool observation records `duration_ms`, `status`, `error_type`,
`error_message`, `tool_call_id`, and `middleware_decisions`. Failed or blocked
tools set Langfuse `level=ERROR` and escalate the containing trace to `ERROR`.
Structured failures add queryable metadata where available; for example an
ambiguous `skill_view` result records `error_code=ambiguous_skill`,
`requested_skill`, and `candidate_count`.

Root traces and tool observations include `langfuse_trace_id`,
`hermes_session_id`, and `tui_session_id`, so a TUI/gateway session can be
correlated directly with its Langfuse trace. Tool events flush every five
completions or five seconds by default; tune the values above for lower latency.

## Disable

```bash
hermes plugins disable observability/langfuse
```
