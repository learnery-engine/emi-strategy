# EMI Strategy — Handover

Last updated: 2026-04-11

## Live URLs

| Route | File | Audience |
|---|---|---|
| `https://emi.learneris.com/` | `index.html` | Public landing — general EMI positioning |
| `https://emi.learneris.com/sgddt` | `emi-proposal-sgddt.html` | Formal partnership proposal for HCMC DoET (Ông Bảo Quốc, Phó Giám đốc) |
| `https://emi.learneris.com/demo` | `emi-school-journey.html` | 8-step interactive EMI school journey demo (also embedded inside `/sgddt`) |

## Deployment

Fully automated via GitHub Actions → Azure Static Web Apps. **Any push to `main` auto-deploys in ~1 minute.** No manual upload needed.

### Infrastructure
- **Azure Static Web App**: `emi-school-journey` (resource group `rg-kelsienguyen_ai`, subscription "Microsoft Azure Sponsorship")
- **Default hostname**: `victorious-wave-0991a4200.1.azurestaticapps.net`
- **Custom domain**: `emi.learneris.com` (DNS CNAME → Azure)
- **GitHub repo**: [learnery-engine/emi-strategy](https://github.com/learnery-engine/emi-strategy)

### Pipeline
1. Workflow: [`.github/workflows/azure-swa.yml`](.github/workflows/azure-swa.yml)
2. Trigger: `push` to `main` or PR open/update
3. Secret: `AZURE_STATIC_WEB_APPS_API_TOKEN` (org-scoped deployment token from Azure SWA)
4. Upload target: `emi-strategy/` subdirectory (contains `index.html` + routing config)
5. Close PR → staging environment auto-removed

### Routing config
[`emi-strategy/staticwebapp.config.json`](emi-strategy/staticwebapp.config.json) rewrites:
- `/sgddt` → `/emi-proposal-sgddt.html`
- `/demo` → `/emi-school-journey.html`
- Fallback → `/index.html`

### Rotating the deployment token

```bash
# Fetch new token from Azure and update GitHub secret
TOKEN=$(az staticwebapp secrets list \
  --name emi-school-journey \
  --resource-group rg-kelsienguyen_ai \
  --query properties.apiKey -o tsv)

echo "$TOKEN" | gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN \
  --repo learnery-engine/emi-strategy
```

### Editing content

```bash
# Clone
git clone https://github.com/learnery-engine/emi-strategy.git
cd emi-strategy/emi-strategy

# Edit files directly
vim index.html                    # landing
vim emi-proposal-sgddt.html       # DoET proposal
vim emi-school-journey.html       # interactive demo

# Push = deploy
git add . && git commit -m "…" && git push
```

Preview locally before push: `npx serve emi-strategy -l 8788` then open `http://localhost:8788`.

## Design System

### Proposal (`/sgddt`) — institutional navy + gold

Designed for a government audience (Phó Giám đốc Sở GD&ĐT TPHCM). Palette and typography chosen to signal authority and credibility, not startup energy.

- **Primary**: Navy `#091b38` → `#1e4d87` (authority, stability, trust)
- **Accent**: Gold `#c79a3a` (used sparingly — header rule, cover divider, trust-signal highlights)
- **Headings**: `Fraunces` editorial serif
- **Body**: `Inter` sans
- **Tabular numbers** for stats/dates/reference codes
- **Uppercase micro-labels** with wide tracking for section headers

### Landing (`/`) — existing blue + teal

Unchanged palette (sky primary + teal accent), targeted at broader audience.

## Primary Trust Signal (Proposal)

The most important element in the proposal is the **HCMC DoET certification card** prominently placed near the top of the "Năng Lực Learneris" section:

- **"Học Cùng AI" — Đạt Chất Lượng Sử Dụng Trong Nhà Trường Phổ Thông**
- **QĐ 809/QĐ-SGDĐT** (Jul 23, 2025) — Tổ đánh giá chất lượng
- **Công văn 1388/SGDĐT-GDPT** (Feb 11, 2026) — final certification

Rationale: Ông Quốc is reading a proposal from a vendor "already approved by my own office". This is the strongest possible trust signal — it was previously hidden below the VNIES certification and is now the lead.

Secondary certifications (VNIES, InfoSec Level 3) sit in smaller cards below.

## Content Guardrails

The following rules are baked into current copy — preserve them when editing:

### 1. No internal product codenames
Use **user-facing descriptions**, not internal repo names. Forbidden on public pages:
- ~~`ai-gateway`~~ → "14+ công cụ AI tích hợp (GPT-4o, Claude, Gemini)"
- ~~`lesson-agent`~~ → "Trình tạo bài giảng CLIL bằng AI"
- ~~`PD-Slides`~~ / ~~`Credits-Management`~~ → "Bộ công cụ bồi dưỡng GV + quản lý chứng chỉ số", "Cổng quản lý trường học"

### 2. No hard pricing on public pages
Dealers, Sở, and stakeholders should not see unit economics. Communicate **productivity**, not **cost**:
- ~~`$0.10/bài học`~~ → "15× nhanh hơn soạn thủ công" / "3 phút vs. 45 phút"

### 3. No commercial commitments in the proposal
Avoid "free" / "$0" language. Use MOU framing:
- ~~"Miễn phí giai đoạn thí điểm"~~ → "MOU · Thoả thuận với Sở GD&ĐT"

### 4. Soft scope numbers
Don't lock in hard pilot counts before the MOU negotiation:
- ~~"5 trường thí điểm"~~ / ~~"10 trường thí điểm"~~ → "~10 (dự kiến)" in the stat card only
- Remove hard numbers from process steps and timeline rows; use "các trường thí điểm"

### 5. Audience breadth
Hero copy explicitly names **Bộ GD&ĐT, Sở GD&ĐT, trường phổ thông, cao đẳng và đại học** — not just "Sở và trường học". EMI is positioned as a cross-tier initiative.

### 6. English center ecosystem (roadmap)
Teacher training capacity is framed as connecting to the English-center ecosystem. Mentioned in:
- Product card "Đào Tạo Giáo Viên"
- Roadmap Q3–Q4 2026 bullet

## Recent Commits

| Commit | Summary |
|---|---|
| [`2a8902a`](../../commit/2a8902a) | Rename `emi-landing.html` → `index.html` for Azure SWA |
| [`95c485c`](../../commit/95c485c) | Move workflow to repo root |
| [`9932912`](../../commit/9932912) | Add Azure SWA workflow + routing config |
| [`dfca483`](../../commit/dfca483) | Landing: stakeholder feedback from RL review (pricing, audience, English-center) |
| [`315be32`](../../commit/315be32) | Proposal: institutional redesign (navy+gold, DoET cert prominence, MOU framing) |

## Known Gotchas

1. **`emi-strategy/` vs repo root** — historical: files live in `emi-strategy/` subdirectory of the repo. Workflow's `app_location: "emi-strategy"` reflects this. Don't move files to repo root without also updating the workflow.

2. **`EMI_Project/` untracked folder** — gitignored locally, not deployed. Safe to ignore.

3. **GitHub Pages still enabled** — the repo also has a `pages-build-deployment` workflow running in parallel. This is auto-generated by GitHub and unused; site on `learnery-engine.github.io/emi-strategy` is stale and not the canonical URL. Either disable Pages in repo settings or ignore.

4. **Demo is embedded + standalone** — `emi-school-journey.html` is both served at `/demo` directly AND embedded as an iframe inside `/sgddt`. Changes to the demo affect both places.

5. **Interactive demo header nav** — the demo has prev/next buttons in the header (visible when iframe is embedded without needing to scroll) as well as the bottom nav bar. Both are kept in sync via `goTo()`.

## Contacts

- **Repo owner**: learnery-engine org
- **Azure subscription**: Kelsie Nguyen (personal sponsorship account — consider migrating to org billing before production traffic scales)
- **Email**: hello@learneris.com
