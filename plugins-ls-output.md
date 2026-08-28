
                                           Plugins                                           
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┓
┃ Name                       ┃ Status      ┃ Version ┃ Description                ┃ Source  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━┩
│ browser-browser-use        │ not enabled │ 1.0.0   │ Browser Use                │ bundled │
│                            │             │         │ (https://browser-use.com)  │         │
│                            │             │         │ cloud browser backend.     │         │
│                            │             │         │ Supports both direct       │         │
│                            │             │         │ BROWSER_USE_API_KEY and    │         │
│                            │             │         │ the managed Nous tool      │         │
│                            │             │         │ gateway. Also powers the   │         │
│                            │             │         │ 'Nous Subscription' UX     │         │
│                            │             │         │ flow that bills usage to a │         │
│                            │             │         │ Nous subscription.         │         │
│ browser-browserbase        │ not enabled │ 1.0.0   │ Browserbase                │ bundled │
│                            │             │         │ (https://browserbase.com)  │         │
│                            │             │         │ cloud browser backend.     │         │
│                            │             │         │ Requires                   │         │
│                            │             │         │ BROWSERBASE_API_KEY +      │         │
│                            │             │         │ BROWSERBASE_PROJECT_ID.    │         │
│                            │             │         │ Supports stealth, proxies, │         │
│                            │             │         │ and keep-alive sessions;   │         │
│                            │             │         │ auto-falls-back when paid  │         │
│                            │             │         │ features are unavailable.  │         │
│ browser-firecrawl          │ not enabled │ 1.0.0   │ Firecrawl                  │ bundled │
│                            │             │         │ (https://firecrawl.dev)    │         │
│                            │             │         │ cloud browser backend.     │         │
│                            │             │         │ Requires                   │         │
│                            │             │         │ FIRECRAWL_API_KEY.         │         │
│                            │             │         │ Distinct from the          │         │
│                            │             │         │ firecrawl WEB              │         │
│                            │             │         │ search/extract plugin —    │         │
│                            │             │         │ the two share an API key   │         │
│                            │             │         │ but operate on different   │         │
│                            │             │         │ endpoints.                 │         │
│ basic                      │ not enabled │ 1.0.0   │ Dashboard auth provider —  │ bundled │
│                            │             │         │ username/password (no      │         │
│                            │             │         │ OAuth IDP). A self-hosted  │         │
│                            │             │         │ 'just put a password on my │         │
│                            │             │         │ dashboard' provider.       │         │
│                            │             │         │ Activates when             │         │
│                            │             │         │ dashboard.basic_auth.user… │         │
│                            │             │         │ plus a password (or        │         │
│                            │             │         │ password_hash) are         │         │
│                            │             │         │ configured via config.yaml │         │
│                            │             │         │ (canonical surface) or the │         │
│                            │             │         │ HERMES_DASHBOARD_BASIC_AU… │         │
│                            │             │         │ env vars. Sessions are     │         │
│                            │             │         │ stateless HMAC-signed      │         │
│                            │             │         │ tokens minted by the       │         │
│                            │             │         │ provider; password hashing │         │
│                            │             │         │ uses stdlib scrypt (no     │         │
│                            │             │         │ third-party dependency).   │         │
│                            │             │         │ Set                        │         │
│                            │             │         │ dashboard.basic_auth.secr… │         │
│                            │             │         │ for restart-surviving /    │         │
│                            │             │         │ multi-worker sessions.     │         │
│ nous                       │ not enabled │ 1.0.0   │ Dashboard auth provider —  │ bundled │
│                            │             │         │ OAuth 2.0                  │         │
│                            │             │         │ (authorization-code +      │         │
│                            │             │         │ PKCE) against Nous Portal. │         │
│                            │             │         │ Auto-activates when a      │         │
│                            │             │         │ client_id is configured    │         │
│                            │             │         │ via either                 │         │
│                            │             │         │ dashboard.oauth.client_id  │         │
│                            │             │         │ in config.yaml (canonical  │         │
│                            │             │         │ surface) or                │         │
│                            │             │         │ HERMES_DASHBOARD_OAUTH_CL… │         │
│                            │             │         │ env var (operator          │         │
│                            │             │         │ override; Portal injects   │         │
│                            │             │         │ this at Fly.io             │         │
│                            │             │         │ provisioning).             │         │
│                            │             │         │ dashboard.oauth.portal_url │         │
│                            │             │         │ /                          │         │
│                            │             │         │ HERMES_DASHBOARD_PORTAL_U… │         │
│                            │             │         │ are optional and default   │         │
│                            │             │         │ to                         │         │
│                            │             │         │ https://portal.nousresear… │         │
│ self-hosted                │ not enabled │ 1.0.0   │ Dashboard auth provider —  │ bundled │
│                            │             │         │ generic self-hosted OpenID │         │
│                            │             │         │ Connect                    │         │
│                            │             │         │ (authorization-code +      │         │
│                            │             │         │ PKCE, public client).      │         │
│                            │             │         │ Works against any          │         │
│                            │             │         │ conformant OIDC identity   │         │
│                            │             │         │ provider (Authentik,       │         │
│                            │             │         │ Keycloak, Zitadel,         │         │
│                            │             │         │ Authelia, Auth0, Okta,     │         │
│                            │             │         │ Google, …) via OIDC        │         │
│                            │             │         │ discovery. Auto-activates  │         │
│                            │             │         │ when an issuer + client_id │         │
│                            │             │         │ are configured, either     │         │
│                            │             │         │ under                      │         │
│                            │             │         │ dashboard.oauth.self_host… │         │
│                            │             │         │ in config.yaml (canonical  │         │
│                            │             │         │ surface) or via the        │         │
│                            │             │         │ HERMES_DASHBOARD_OIDC_ISS… │         │
│                            │             │         │ +                          │         │
│                            │             │         │ HERMES_DASHBOARD_OIDC_CLI… │         │
│                            │             │         │ env vars (operator         │         │
│                            │             │         │ override / secret          │         │
│                            │             │         │ injection). Scopes default │         │
│                            │             │         │ to 'openid profile email'. │         │
│                            │             │         │ Verifies the OIDC ID token │         │
│                            │             │         │ (RS256/ES256) against the  │         │
│                            │             │         │ discovered jwks_uri.       │         │
│ disk-cleanup               │ not enabled │ 2.0.0   │ Auto-track and clean up    │ bundled │
│                            │             │         │ ephemeral files (test      │         │
│                            │             │         │ scripts, temp outputs,     │         │
│                            │             │         │ cron logs) created during  │         │
│                            │             │         │ Hermes sessions. Runs via  │         │
│                            │             │         │ plugin hooks — no agent    │         │
│                            │             │         │ action required.           │         │
│ google_meet                │ not enabled │ 0.2.0   │ Join a Google Meet call,   │ bundled │
│                            │             │         │ transcribe live captions,  │         │
│                            │             │         │ speak in realtime, and     │         │
│                            │             │         │ follow up afterwards. v1   │         │
│                            │             │         │ transcribe-only is the     │         │
│                            │             │         │ default; v2 realtime       │         │
│                            │             │         │ duplex audio via OpenAI    │         │
│                            │             │         │ Realtime +                 │         │
│                            │             │         │ BlackHole/PulseAudio ships │         │
│                            │             │         │ with mode='realtime'; v3   │         │
│                            │             │         │ remote node host lets the  │         │
│                            │             │         │ bot run on a different     │         │
│                            │             │         │ machine than the gateway   │         │
│                            │             │         │ (gateway on Linux,         │         │
│                            │             │         │ Chrome+signed-in profile   │         │
│                            │             │         │ on the user's Mac).        │         │
│                            │             │         │ Explicit-by-design: only   │         │
│                            │             │         │ joins meet.google.com URLs │         │
│                            │             │         │ passed in — no calendar    │         │
│                            │             │         │ scanning, no auto-dial.    │         │
│ fal                        │ not enabled │ 1.0.0   │ FAL.ai image generation    │ bundled │
│                            │             │         │ backend (flux-2-klein,     │         │
│                            │             │         │ flux-2-pro, nano-banana,   │         │
│                            │             │         │ gpt-image-1.5, recraft-v3, │         │
│                            │             │         │ etc.).                     │         │
│ krea                       │ not enabled │ 1.0.0   │ Krea image generation      │ bundled │
│                            │             │         │ backend (Krea 2 Large +    │         │
│                            │             │         │ Krea 2 Medium foundation   │         │
│                            │             │         │ models).                   │         │
│ openai                     │ not enabled │ 1.0.0   │ OpenAI image generation    │ bundled │
│                            │             │         │ backend (gpt-image-2).     │         │
│                            │             │         │ Saves generated images to  │         │
│                            │             │         │ $HERMES_HOME/cache/images… │         │
│ openai-codex               │ not enabled │ 1.0.0   │ OpenAI image generation    │ bundled │
│                            │             │         │ backed by ChatGPT/Codex    │         │
│                            │             │         │ OAuth (gpt-image-2 via the │         │
│                            │             │         │ Responses image_generation │         │
│                            │             │         │ tool). Saves generated     │         │
│                            │             │         │ images to                  │         │
│                            │             │         │ $HERMES_HOME/cache/images… │         │
│ xai                        │ not enabled │ 1.0.0   │ xAI image generation       │ bundled │
│                            │             │         │ backend                    │         │
│                            │             │         │ (grok-imagine-image).      │         │
│                            │             │         │ Text-to-image.             │         │
│ alibaba-provider           │ not enabled │ 1.0.0   │ Alibaba DashScope          │ bundled │
│                            │             │         │ (international)            │         │
│ alibaba-coding-plan-provi… │ not enabled │ 1.0.0   │ Alibaba Cloud Coding Plan  │ bundled │
│ anthropic-provider         │ not enabled │ 1.0.0   │ Anthropic (Claude)         │ bundled │
│ arcee-provider             │ not enabled │ 1.0.0   │ Arcee AI                   │ bundled │
│ azure-foundry-provider     │ not enabled │ 1.0.0   │ Microsoft Foundry          │ bundled │
│ bedrock-provider           │ not enabled │ 1.0.0   │ AWS Bedrock                │ bundled │
│ copilot-provider           │ not enabled │ 1.0.0   │ GitHub Copilot             │ bundled │
│ copilot-acp-provider       │ not enabled │ 1.0.0   │ GitHub Copilot via ACP     │ bundled │
│                            │             │         │ subprocess                 │         │
│ custom-provider            │ not enabled │ 1.0.0   │ Custom / Ollama / local    │ bundled │
│                            │             │         │ OpenAI-compatible endpoint │         │
│ deepseek-provider          │ not enabled │ 1.0.0   │ DeepSeek                   │ bundled │
│ gemini-provider            │ not enabled │ 1.0.0   │ Google Gemini (API key +   │ bundled │
│                            │             │         │ Cloud Code OAuth)          │         │
│ gmi-provider               │ not enabled │ 1.0.0   │ GMI Cloud                  │ bundled │
│ huggingface-provider       │ not enabled │ 1.0.0   │ HuggingFace Inference      │ bundled │
│                            │             │         │ Providers                  │         │
│ kilocode-provider          │ not enabled │ 1.0.0   │ Kilo Code                  │ bundled │
│ kimi-coding-provider       │ not enabled │ 1.0.0   │ Moonshot Kimi Coding       │ bundled │
│                            │             │         │ (global + China)           │         │
│ minimax-provider           │ not enabled │ 1.0.0   │ MiniMax M-series (global + │ bundled │
│                            │             │         │ China + OAuth)             │         │
│ nous-provider              │ not enabled │ 1.0.0   │ Nous Research Portal       │ bundled │
│ novita-provider            │ not enabled │ 1.0.0   │ NovitaAI AI-native cloud   │ bundled │
│                            │             │         │ for builders and agents    │         │
│ nvidia-provider            │ not enabled │ 1.0.0   │ NVIDIA NIM                 │ bundled │
│ ollama-cloud-provider      │ not enabled │ 1.0.0   │ Ollama Cloud               │ bundled │
│ openai-codex-provider      │ not enabled │ 1.0.0   │ OpenAI Codex (Responses    │ bundled │
│                            │             │         │ API)                       │         │
│ opencode-zen-provider      │ not enabled │ 1.0.0   │ OpenCode (Zen + Go)        │ bundled │
│ openrouter-provider        │ not enabled │ 1.0.0   │ OpenRouter aggregator      │ bundled │
│ qwen-oauth-provider        │ not enabled │ 1.0.0   │ Qwen Portal (OAuth)        │ bundled │
│ stepfun-provider           │ not enabled │ 1.0.0   │ StepFun Step Plan          │ bundled │
│ xai-provider               │ not enabled │ 1.0.0   │ xAI Grok (Responses API)   │ bundled │
│ xiaomi-provider            │ not enabled │ 1.0.0   │ Xiaomi MiMo                │ bundled │
│ zai-provider               │ not enabled │ 1.0.0   │ Z.AI / GLM                 │ bundled │
│ langfuse                   │ not enabled │ 1.0.0   │ Optional Langfuse          │ bundled │
│                            │             │         │ observability for Hermes — │         │
│                            │             │         │ traces conversations, LLM  │         │
│                            │             │         │ calls, and tool usage.     │         │
│                            │             │         │ Opt-in via `hermes plugins │         │
│                            │             │         │ enable                     │         │
│                            │             │         │ observability/langfuse` or │         │
│                            │             │         │ `hermes tools → Langfuse   │         │
│                            │             │         │ Observability`.            │         │
│ nemo_relay                 │ not enabled │ 0.1.0   │ Optional NeMo Relay        │ bundled │
│                            │             │         │ observability for Hermes.  │         │
│                            │             │         │ Opt in with `hermes        │         │
│                            │             │         │ plugins enable             │         │
│                            │             │         │ observability/nemo_relay`; │         │
│                            │             │         │ HERMES_NEMO_RELAY_* env    │         │
│                            │             │         │ vars configure exports     │         │
│                            │             │         │ after the plugin is        │         │
│                            │             │         │ enabled.                   │         │
│ discord-platform           │ not enabled │ 1.0.0   │ Discord gateway adapter    │ bundled │
│                            │             │         │ for Hermes Agent. Connects │         │
│                            │             │         │ to Discord via the         │         │
│                            │             │         │ discord.py library and     │         │
│                            │             │         │ relays messages between    │         │
│                            │             │         │ Discord guilds/DMs and the │         │
│                            │             │         │ Hermes agent. Supports     │         │
│                            │             │         │ voice mode, slash          │         │
│                            │             │         │ commands, free-response    │         │
│                            │             │         │ channels, role-based DM    │         │
│                            │             │         │ auth, threads, reactions,  │         │
│                            │             │         │ and channel skill          │         │
│                            │             │         │ bindings.                  │         │
│                            │             │         │                            │         │
│ google_chat-platform       │ not enabled │ 1.0.0   │ Google Chat gateway        │ bundled │
│                            │             │         │ adapter for Hermes Agent.  │         │
│                            │             │         │ Connects via Cloud Pub/Sub │         │
│                            │             │         │ pull subscription for      │         │
│                            │             │         │ inbound events and the     │         │
│                            │             │         │ Google Chat REST API for   │         │
│                            │             │         │ outbound messages — same   │         │
│                            │             │         │ ergonomics as Slack Socket │         │
│                            │             │         │ Mode or Telegram           │         │
│                            │             │         │ long-polling, no public    │         │
│                            │             │         │ URL required. Native file  │         │
│                            │             │         │ attachments are delivered  │         │
│                            │             │         │ via per-user OAuth (each   │         │
│                            │             │         │ user runs /setup-files     │         │
│                            │             │         │ once in their own DM).     │         │
│                            │             │         │                            │         │
│ homeassistant-platform     │ not enabled │ 1.0.0   │ Home Assistant gateway     │ bundled │
│                            │             │         │ adapter for Hermes Agent.  │         │
│                            │             │         │ Subscribes to HA's         │         │
│                            │             │         │ WebSocket event bus and    │         │
│                            │             │         │ forwards state-change      │         │
│                            │             │         │ events (with per-entity    │         │
│                            │             │         │ cooldowns and              │         │
│                            │             │         │ domain/entity filtering)   │         │
│                            │             │         │ to the agent. Outbound     │         │
│                            │             │         │ messages are delivered as  │         │
│                            │             │         │ HA persistent              │         │
│                            │             │         │ notifications via the REST │         │
│                            │             │         │ API. Out-of-process cron   │         │
│                            │             │         │ delivery via the           │         │
│                            │             │         │ ``notify.notify`` service  │         │
│                            │             │         │ is also supported.         │         │
│                            │             │         │                            │         │
│ irc-platform               │ not enabled │ 1.0.0   │ IRC gateway adapter for    │ bundled │
│                            │             │         │ Hermes Agent. Connects to  │         │
│                            │             │         │ an IRC server and relays   │         │
│                            │             │         │ messages between an IRC    │         │
│                            │             │         │ channel (or DMs) and the   │         │
│                            │             │         │ Hermes agent.  No external │         │
│                            │             │         │ dependencies — uses        │         │
│                            │             │         │ Python's stdlib asyncio    │         │
│                            │             │         │ for the IRC protocol.      │         │
│                            │             │         │                            │         │
│ line-platform              │ not enabled │ 1.0.0   │ LINE Messaging API gateway │ bundled │
│                            │             │         │ adapter for Hermes Agent.  │         │
│                            │             │         │ Runs an aiohttp webhook    │         │
│                            │             │         │ server that receives LINE  │         │
│                            │             │         │ webhook events (with       │         │
│                            │             │         │ HMAC-SHA256 signature      │         │
│                            │             │         │ verification) and relays   │         │
│                            │             │         │ messages between LINE      │         │
│                            │             │         │ chats (1:1, groups, rooms) │         │
│                            │             │         │ and the Hermes agent.      │         │
│                            │             │         │ Outbound replies prefer    │         │
│                            │             │         │ the free reply token and   │         │
│                            │             │         │ fall back to the metered   │         │
│                            │             │         │ Push API when the token    │         │
│                            │             │         │ has expired or is absent.  │         │
│                            │             │         │ Slow LLM responses surface │         │
│                            │             │         │ a Template Buttons         │         │
│                            │             │         │ postback bubble so the     │         │
│                            │             │         │ user can fetch the answer  │         │
│                            │             │         │ with a fresh reply token   │         │
│                            │             │         │ (free) once it's ready.    │         │
│                            │             │         │                            │         │
│ mattermost-platform        │ not enabled │ 1.0.0   │ Mattermost gateway adapter │ bundled │
│                            │             │         │ for Hermes Agent. Connects │         │
│                            │             │         │ to a self-hosted or cloud  │         │
│                            │             │         │ Mattermost instance via    │         │
│                            │             │         │ the v4 REST API +          │         │
│                            │             │         │ WebSocket event stream and │         │
│                            │             │         │ relays messages between    │         │
│                            │             │         │ Mattermost channels/DMs    │         │
│                            │             │         │ and the Hermes agent.      │         │
│                            │             │         │ Supports thread-mode       │         │
│                            │             │         │ replies, native file       │         │
│                            │             │         │ uploads, channel-scoped    │         │
│                            │             │         │ allowlists, and            │         │
│                            │             │         │ home-channel cron          │         │
│                            │             │         │ delivery.                  │         │
│                            │             │         │                            │         │
│ ntfy-platform              │ not enabled │ 1.0.0   │ ntfy push-notification     │ bundled │
│                            │             │         │ gateway adapter for Hermes │         │
│                            │             │         │ Agent. Subscribes to a     │         │
│                            │             │         │ topic on ntfy.sh or any    │         │
│                            │             │         │ self-hosted ntfy server    │         │
│                            │             │         │ via HTTP streaming, and    │         │
│                            │             │         │ publishes replies via HTTP │         │
│                            │             │         │ POST. Lightweight — no     │         │
│                            │             │         │ external SDK, only httpx   │         │
│                            │             │         │ (already a Hermes          │         │
│                            │             │         │ dependency).               │         │
│                            │             │         │ ntfy has no native         │         │
│                            │             │         │ user-identity primitive;   │         │
│                            │             │         │ the adapter treats each    │         │
│                            │             │         │ topic as a single trusted  │         │
│                            │             │         │ channel and never derives  │         │
│                            │             │         │ user identity from         │         │
│                            │             │         │ publisher-controlled       │         │
│                            │             │         │ fields. Use a private      │         │
│                            │             │         │ topic + read token for any │         │
│                            │             │         │ real trust boundary.       │         │
│                            │             │         │                            │         │
│ photon-platform            │ not enabled │ 0.3.0   │ Photon Spectrum gateway    │ bundled │
│                            │             │         │ adapter for Hermes Agent.  │         │
│                            │             │         │ Connects to iMessage (and  │         │
│                            │             │         │ other Spectrum interfaces) │         │
│                            │             │         │ through Photon's managed   │         │
│                            │             │         │ Spectrum platform. Both    │         │
│                            │             │         │ directions run over the    │         │
│                            │             │         │ `spectrum-ts` SDK's        │         │
│                            │             │         │ long-lived gRPC stream via │         │
│                            │             │         │ a small supervised Node    │         │
│                            │             │         │ sidecar — inbound messages │         │
│                            │             │         │ arrive on the SDK's        │         │
│                            │             │         │ `app.messages` stream (no  │         │
│                            │             │         │ webhook, no public URL, no │         │
│                            │             │         │ signing secret), and       │         │
│                            │             │         │ outbound messages are sent │         │
│                            │             │         │ over the same sidecar.     │         │
│                            │             │         │ The plugin ships with a    │         │
│                            │             │         │ `hermes photon` CLI for    │         │
│                            │             │         │ the one-time device login  │         │
│                            │             │         │ + project + user setup.    │         │
│                            │             │         │ Runtime credentials are    │         │
│                            │             │         │ written to                 │         │
│                            │             │         │ ``~/.hermes/.env``         │         │
│                            │             │         │ (``PHOTON_PROJECT_ID`` =   │         │
│                            │             │         │ the Spectrum project id,   │         │
│                            │             │         │ ``PHOTON_PROJECT_SECRET``) │         │
│                            │             │         │ like every other channel,  │         │
│                            │             │         │ with management metadata   │         │
│                            │             │         │ (device token, dashboard   │         │
│                            │             │         │ project id) in             │         │
│                            │             │         │ ``~/.hermes/auth.json``.   │         │
│                            │             │         │ Photon's free shared-line  │         │
│                            │             │         │ model lets users get       │         │
│                            │             │         │ started without a paid     │         │
│                            │             │         │ plan.                      │         │
│                            │             │         │                            │         │
│ simplex-platform           │ not enabled │ 1.1.0   │ SimpleX Chat gateway       │ bundled │
│                            │             │         │ adapter for Hermes Agent.  │         │
│                            │             │         │ Connects to a local        │         │
│                            │             │         │ simplex-chat daemon via    │         │
│                            │             │         │ WebSocket and relays       │         │
│                            │             │         │ messages between SimpleX   │         │
│                            │             │         │ contacts/groups and the    │         │
│                            │             │         │ Hermes agent. SimpleX is   │         │
│                            │             │         │ decentralised and assigns  │         │
│                            │             │         │ no persistent user IDs —   │         │
│                            │             │         │ every contact is an opaque │         │
│                            │             │         │ internal ID generated at   │         │
│                            │             │         │ connection time, making it │         │
│                            │             │         │ one of the most private    │         │
│                            │             │         │ messengers available.      │         │
│                            │             │         │                            │         │
│ teams-platform             │ not enabled │ 1.0.0   │ Microsoft Teams gateway    │ bundled │
│                            │             │         │ adapter for Hermes Agent.  │         │
│                            │             │         │ Connects to Microsoft      │         │
│                            │             │         │ Teams via the Bot          │         │
│                            │             │         │ Framework and relays       │         │
│                            │             │         │ messages between Teams     │         │
│                            │             │         │ chats (personal DMs, group │         │
│                            │             │         │ chats, channel posts) and  │         │
│                            │             │         │ the Hermes agent. Supports │         │
│                            │             │         │ Adaptive Card approval     │         │
│                            │             │         │ prompts.                   │         │
│                            │             │         │                            │         │
│ security-guidance          │ not enabled │ 0.1.0   │ Append security warnings   │ bundled │
│                            │             │         │ to file-write tool results │         │
│                            │             │         │ when the new content       │         │
│                            │             │         │ contains known-dangerous   │         │
│                            │             │         │ patterns (pickle.load,     │         │
│                            │             │         │ yaml.load, eval(,          │         │
│                            │             │         │ os.system,                 │         │
│                            │             │         │ dangerouslySetInnerHTML,   │         │
│                            │             │         │ verify=False, ECB, XXE,    │         │
│                            │             │         │ GitHub Actions injection,  │         │
│                            │             │         │ ...). 25 regex/substring   │         │
│                            │             │         │ rules forked from          │         │
│                            │             │         │ Anthropic's                │         │
│                            │             │         │ claude-plugins-official    │         │
│                            │             │         │ under Apache-2.0.          │         │
│                            │             │         │ Non-blocking — the file is │         │
│                            │             │         │ written and the warning    │         │
│                            │             │         │ rides back to the model in │         │
│                            │             │         │ the next turn so it can    │         │
│                            │             │         │ self-correct.              │         │
│ spotify                    │ not enabled │ 1.0.0   │ Native Spotify integration │ bundled │
│                            │             │         │ — 7 tools (playback,       │         │
│                            │             │         │ devices, queue, search,    │         │
│                            │             │         │ playlists, albums,         │         │
│                            │             │         │ library) using Spotify Web │         │
│                            │             │         │ API + PKCE OAuth. Auth via │         │
│                            │             │         │ `hermes auth spotify`.     │         │
│                            │             │         │ Tools gate on              │         │
│                            │             │         │ `providers.spotify` in     │         │
│                            │             │         │ ~/.hermes/auth.json.       │         │
│ teams_pipeline             │ not enabled │ 0.1.0   │ Microsoft Teams meeting    │ bundled │
│                            │             │         │ pipeline plugin with       │         │
│                            │             │         │ durable runtime state and  │         │
│                            │             │         │ operator CLI flows for     │         │
│                            │             │         │ Graph-backed               │         │
│                            │             │         │ transcript-first meeting   │         │
│                            │             │         │ summaries.                 │         │
│ fal                        │ not enabled │ 1.0.0   │ FAL.ai video generation    │ bundled │
│                            │             │         │ backend. Multi-model — Veo │         │
│                            │             │         │ 3.1, Kling, Pixverse —     │         │
│                            │             │         │ covering text-to-video and │         │
│                            │             │         │ image-to-video via         │         │
│                            │             │         │ fal_client's queue API.    │         │
│ xai                        │ not enabled │ 1.0.0   │ xAI Grok Imagine video     │ bundled │
│                            │             │         │ generation backend.        │         │
│                            │             │         │ Supports text-to-video,    │         │
│                            │             │         │ image-to-video, and        │         │
│                            │             │         │ reference-image-guided     │         │
│                            │             │         │ generation via the xAI     │         │
│                            │             │         │ async videos API.          │         │
│ web-brave-free             │ not enabled │ 1.0.0   │ Brave Search (free tier) — │ bundled │
│                            │             │         │ web search via Brave's     │         │
│                            │             │         │ Data-for-Search API.       │         │
│                            │             │         │ Requires                   │         │
│                            │             │         │ BRAVE_SEARCH_API_KEY (free │         │
│                            │             │         │ signup at                  │         │
│                            │             │         │ https://brave.com/search/… │         │
│                            │             │         │ 2k queries/month).         │         │
│ web-ddgs                   │ not enabled │ 1.0.0   │ DuckDuckGo web search via  │ bundled │
│                            │             │         │ the ddgs Python package —  │         │
│                            │             │         │ no API key required.       │         │
│                            │             │         │ Install with `pip install  │         │
│                            │             │         │ ddgs`.                     │         │
│ web-exa                    │ not enabled │ 1.0.0   │ Exa web search and content │ bundled │
│                            │             │         │ extraction. Requires       │         │
│                            │             │         │ EXA_API_KEY — sign up at   │         │
│                            │             │         │ https://exa.ai.            │         │
│ web-firecrawl              │ not enabled │ 1.0.0   │ Firecrawl web search +     │ bundled │
│                            │             │         │ content extraction.        │         │
│                            │             │         │ Supports direct API and    │         │
│                            │             │         │ Nous-hosted tool-gateway   │         │
│                            │             │         │ routing for subscribers.   │         │
│                            │             │         │ Requires FIRECRAWL_API_KEY │         │
│                            │             │         │ (or FIRECRAWL_API_URL for  │         │
│                            │             │         │ self-hosted), or an active │         │
│                            │             │         │ Nous subscription with     │         │
│                            │             │         │ FIRECRAWL_GATEWAY_URL.     │         │
│ web-parallel               │ not enabled │ 1.0.0   │ Parallel.ai web search +   │ bundled │
│                            │             │         │ content extraction. Search │         │
│                            │             │         │ returns objective-tuned    │         │
│                            │             │         │ results; extract uses the  │         │
│                            │             │         │ async SDK for parallel     │         │
│                            │             │         │ page fetches. Requires     │         │
│                            │             │         │ PARALLEL_API_KEY — sign up │         │
│                            │             │         │ at https://parallel.ai.    │         │
│ web-searxng                │ not enabled │ 1.0.0   │ SearXNG web search — free, │ bundled │
│                            │             │         │ self-hosted,               │         │
│                            │             │         │ privacy-respecting         │         │
│                            │             │         │ metasearch engine.         │         │
│                            │             │         │ Requires SEARXNG_URL       │         │
│                            │             │         │ pointing at your instance. │         │
│ web-tavily                 │ not enabled │ 1.0.0   │ Tavily web search +        │ bundled │
│                            │             │         │ content extraction +       │         │
│                            │             │         │ crawl. Search + extract    │         │
│                            │             │         │ are mainstream; crawl is   │         │
│                            │             │         │ unique to Tavily among     │         │
│                            │             │         │ built-in providers.        │         │
│                            │             │         │ Requires TAVILY_API_KEY —  │         │
│                            │             │         │ sign up at                 │         │
│                            │             │         │ https://app.tavily.com/ho… │         │
│ web-xai                    │ not enabled │ 1.0.0   │ xAI Web Search — search    │ bundled │
│                            │             │         │ the web via Grok's agentic │         │
│                            │             │         │ web_search tool (Responses │         │
│                            │             │         │ API). Requires xAI Grok    │         │
│                            │             │         │ OAuth (via `hermes auth`)  │         │
│                            │             │         │ or XAI_API_KEY             │         │
│                            │             │         │ (https://x.ai).            │         │
└────────────────────────────┴─────────────┴─────────┴────────────────────────────┴─────────┘

Compact view: hermes plugins list --plain --no-bundled
Interactive toggle: hermes plugins
Enable/disable: hermes plugins enable/disable <name>
Plugins are opt-in by default — only 'enabled' plugins load.
