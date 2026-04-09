# EMI Product Alignment: What We Already Have

## Principle: Extend, Don't Rebuild

Nearly every EMI requirement maps to something Learneris already has built or partially built. The strategy is to **configure, extend, and rebrand** existing systems — not build from scratch.

---

## Mapping: EMI Policy Needs → Existing Learneris Capabilities

### 1. "AI integration in English teaching" (Step 3 of HCMC De An)

**What we have:**
- **ai-gateway** — Multi-model AI router (GPT-4o, Claude Sonnet 4, Gemini 2.5 Flash, image gen via FLUX/Imagen). Already handles chat, image generation, credit billing, failover. All Learneris products route through this.
- **AI-Course-fresh** — 4 lesson-scoped AI chatbot personas already live for students (natural/artificial classifier, creative art describer, deliberate-error AI for critical thinking, safety advisor). Uses Azure OpenAI with child-safe system prompts.
- **LMS** — AI content generation (Claude Sonnet 4.6 via SSE streaming) creates lesson HTML and MCQ quizzes from curriculum standards. AI-assisted grading with per-criterion rubric scoring.
- **creator.learnery** — Full AI course creation pipeline: title → objectives → outline → slides → PPTX export. 7+ output languages including English and Vietnamese.

**What to extend for EMI:**
- Add new AI chatbot personas to AI-Course-fresh for English practice (conversation partner, vocabulary drill, pronunciation scenarios)
- Add `language` parameter to lesson-agent prompts (currently English-only output — add bilingual/CLIL output mode)
- Add EMI-specific content types in creator.learnery (CLIL lesson template, bilingual slide template)
- ai-gateway: **no changes needed** — it's already model-agnostic and content-type-routed

**Effort: Small-Medium** — new prompts and templates, not new infrastructure.

---

### 2. "Online learning platform" (Step 3 of HCMC De An)

**What we have:**
- **LMS (lms.learneris.com)** — Full teacher+student platform with:
  - Course authoring (6 block types: text, file, HTML, AI content, AI App, embed)
  - Assignment management with rubrics, scoring, time limits, max attempts
  - AI quiz generation (3-15 MCQ from curriculum KB)
  - Analytics dashboard (completion rates, grade distribution, weekly engagement, top performers)
  - Student dashboard (enrolled courses, assignments, calendar, grades)
  - Multi-org / role switching (teacher at school A, student at school B)
  - **Full EN/VI bilingual UI** (i18next with runtime toggle)
  - 105+ Bubble data types with Zod schemas
  - Class management, student enrollment, org management

**What to extend for EMI:**
- Create EMI-specific course templates pre-loaded with CLIL structure
- Add "English exposure hours" tracking field to student progress (simple schema addition)
- Add school-wide admin view (currently teacher-scoped analytics — extend to org-level rollup)
- Surface the existing `report`, `reportbatch`, `recommendation` schemas as actual pages (they're defined but have no UI yet)

**Effort: Small** — the platform is ready; it needs EMI-specific content and a few dashboard views.

---

### 3. "Bilingual digital content repositories" (Step 3 of HCMC De An)

**What we have:**
- **AI-Course-fresh** — Already has:
  - Full bilingual translation file (`en.json`) covering all TH0 lessons
  - VN/EN language toggle built into student and teacher HTML books (saves to localStorage)
  - **EMI school variant** in PD training data — every activity has 3 `schoolVariants`: `"emi"`, `"vn-elite"`, `"normal"`. EMI variant uses English terminology and global examples.
  - **HCAI Engine bilingual mode** — JSON-driven slide engine with `"bilingual": true` flag per lesson, `biText(vn, en)` helper for dual-language rendering
  - 5 grades × 16 lessons × 35 periods = 80 lessons of AI literacy content, all with bilingual infrastructure
  - THCS content (Grades 6-9) via HCAI Engine with bilingual support
- **lesson-agent** — 5-step content pipeline (study guide → slides → teaching guide → quiz → interactive). Currently English-only prompts. YAML extension system allows adding new content types without code.
- **creator.learnery** — Generates content in 7+ languages. PPTX export. Embed route with language parameter.

**What to extend for EMI:**
- Add `language: "bilingual"` mode to lesson-agent prompts (output Vietnamese content with English integration at configurable ratios)
- Create CLIL YAML prompt flows: `clil-math.yaml`, `clil-science.yaml` — input Vietnamese curriculum standard, output bilingual lesson package
- Use existing HCAI Engine bilingual flag for new EMI subject content (Math, Science)
- Leverage creator.learnery's multi-language generation for schools that want to create their own CLIL materials

**Effort: Medium** — new prompt templates, not new systems. The bilingual infrastructure is already there.

---

### 4. "Teacher proficiency assessment and development" (KH 18, QD 2371)

**What we have:**
- **PD-Slides** — Complete teacher training system:
  - 8 modules (3 Foundation + 4 Topic + 1 Implementation), 6-7 hour pathway
  - Live quiz engine with timed questions, leaderboard, score-based progression
  - Live polling and whiteboard collaboration
  - Breakout room activities with configurable groups
  - Session timer and activity timers
  - Participant registration with session codes and QR access
  - Module completion tracking with facilitator approval
  - **Bilingual certificate generation** (EN/VI) with public verification URL
  - Google Sheets backend for data sync
  - **25+ peer-reviewed research citations** backing the pedagogy
  - **Already has EMI school variant** differentiation in activities
  - Offline-capable (pure static HTML/CSS/JS)
- **Credits-Management** — Teacher training certification pipeline:
  - `TrainingModule` model with levels (FOUNDATIONAL/METHODOLOGY/COURSE_SPECIFIC)
  - `TrainingCompletion` with scoring, section breakdowns, pass/fail, cert status workflow (PENDING → APPROVED → ISSUED)
  - `TeacherQualification` model linking teachers to certified modules
  - `Certificate` model (unified teacher PD + student course certs) with certCode, verification URL, PDF URL
  - 12 API endpoints: submit results, verify, list modules, create/update modules, list/review completions, issue certs, get/revoke qualifications
  - **Planned**: qualification gating on class assignments (teacher must be certified to teach a course)
- **AI-Course-fresh admin** — PD session management (create sessions, assign modules, enrollment, analytics, certificate issuance/revocation)

**What to extend for EMI:**
- Create EMI-specific PD modules: "Teaching Math in English", "CLIL Methodology", "Classroom English for Subject Teachers"
- The module infrastructure is already there — just new content in the existing PD-Slides format
- Add English proficiency self-assessment module (mapped to VNEFR 6-level framework) — a new quiz module in the existing quiz engine
- Wire the existing `TrainingModule` → `TeacherQualification` pipeline to gate EMI teaching assignments
- Use existing PD certificate system for EMI teacher credentials

**Effort: Small** — new content modules, not new systems. The entire training + certification pipeline exists.

---

### 5. "CLIL (Content and Language Integrated Learning)" (Core EMI methodology)

**What we have:**
- **AI-Course-fresh** already implements CLIL concepts:
  - Teaching Math and Science concepts through AI literacy content
  - Activity types: sorting, matching, MCQ, fill-blank, flashcard, sequence, memory game, drag-classify, detective game, discovery cards, poster design, project showcase
  - 25+ interactive activity HTML files
  - HCAI Engine slide types: sorting, MCQ, poll, evaluation, timer-activity, comparison-table, vocabulary, flow, process, timeline — all usable for CLIL
- **lesson-agent** — 7 interactive activity types already defined. YAML extension for new types.
- **LMS** — Embeds any HTML content (block type "HTML code"), so CLIL activities built anywhere can be delivered through LMS

**What to extend for EMI:**
- New lesson-agent YAML flows for CLIL subjects (Math, Science, Social Studies)
- Repurpose existing activity types for English vocabulary and subject-specific language practice
- Add subject vocabulary glossary generation step to the pipeline (new YAML tool, ~50 lines)

**Effort: Small** — new content templates using existing activity infrastructure.

---

### 6. "Monitoring and reporting" (Required by all EMI policies)

**What we have:**
- **LMS Analytics** — Completion rates, grade distribution, weekly engagement, top performers (teacher-scoped)
- **Credits-Management** — Full platform KPIs, credit usage by org/user/day, AI generation type breakdown, usage summary rollups, finance module with revenue/expense/P&L/runway
- **AI-Course-fresh admin** — PD analytics (per-module completion rates, session stats), YCCD compliance tracking (element-by-element coverage heatmap)
- **School Admin Portal** (Credits-Management) — Self-service portal for school admins: user management, class management, usage stats, content-type breakdown, CSV export, import pipeline

**What to extend for EMI:**
- Add EMI-specific metrics to LMS analytics: English exposure hours, CLIL lesson completion rates, teacher EMI certification status
- Extend School Admin Portal with EMI readiness scorecard (use existing KPI card pattern)
- Add auto-generated DoE compliance report (new page/export in Credits-Management using existing data)
- Surface existing `report`/`reportbatch` schemas in LMS as actual pages

**Effort: Small-Medium** — new dashboard views and report templates using existing data infrastructure.

---

### 7. "School onboarding and management" (Scaling EMI across schools)

**What we have:**
- **Credits-Management School Onboarding Pipeline** — Already built:
  - Parse contract PDF (AI-extracted school name, value, dates)
  - Parse Excel roster (smart column detection for email/class/name/role)
  - Full execution: create org → create users → create classes → assign credits → upload contract to Google Drive
  - Bubble sync (bi-directional org/user/class management)
  - Temp password issuance (bulk, per-org, with CSV export)
  - Multi-org role mapping
- **Sales CRM** (Credits-Management) — Leads, contacts, activity log, follow-ups, pipeline stages, revenue forecast, link-to-org
- **Partner Management** — Partner CRUD with linked orgs and purchase orders
- **Purchase Orders + Invoicing** — Full PO lifecycle (DRAFT → SIGNED), per-class billing, semester billing cycles, invoice generation

**What to extend for EMI:**
- Add "EMI Pilot" as a lead source / pipeline stage in the CRM
- Create EMI-specific onboarding template (pre-configured org settings, CLIL course assignments, PD module enrollment)
- Bundle the Hanoi Standardized Kit documents into the onboarding flow

**Effort: Minimal** — configuration, not development.

---

### 8. "Mobile access for students" (Expanding reach)

**What we have:**
- **Mobile app** — Capacitor 8 (iOS + Android), React/Vite frontend, Express backend, Drizzle ORM, Azure deployment, GitHub Actions CI/CD

**What to extend for EMI:**
- The mobile app serves as the student-facing EMI practice tool
- Same content delivered through LMS is accessible on mobile
- No additional development needed unless EMI-specific offline content is required

**Effort: None** for basic EMI delivery.

---

## Summary: Build vs. Extend vs. Configure

| EMI Need | Approach | What Exists | What's New | Effort |
|----------|----------|-------------|------------|--------|
| AI-powered English tools | **Extend** | ai-gateway, AI chatbots, AI quiz gen | New chatbot personas, CLIL prompts | S-M |
| Online learning platform | **Configure** | LMS (full teacher+student) | EMI course templates, org-level analytics | S |
| Bilingual content repository | **Extend** | Bilingual infrastructure, HCAI Engine, lesson-agent | `bilingual` mode for lesson-agent, CLIL YAML flows | M |
| Teacher training & certification | **Extend** | PD-Slides (8 modules), training pipeline, certs | New EMI PD content modules, English self-assessment | S |
| CLIL activities | **Extend** | 25+ activity types, 7 interactive formats | Subject-specific activity templates | S |
| Monitoring & reporting | **Extend** | Analytics, admin dashboard, school portal | EMI metrics, DoE report template | S-M |
| School onboarding | **Configure** | Full onboarding pipeline, CRM, invoicing | EMI pipeline stage, onboarding template | Min |
| Mobile student access | **Use as-is** | Capacitor mobile app | None | None |
| EMI Readiness Assessment | **New (small)** | Quiz engine, YCCD compliance tracking | School self-assessment questionnaire | S |
| School document kit | **Use as-is** | Hanoi Standardized Kit (4 DOCX templates) | Adapt for HCMC and other provinces | Min |

**Legend:** Min = days, S = 1-2 weeks, M = 2-4 weeks, S-M = varies by scope

---

## The Real Net-New Builds (Only 2)

### 1. CLIL Content Templates (Medium effort)
New YAML prompt flows for lesson-agent + new bilingual mode. This is the core differentiator — the ability to take any Vietnamese curriculum standard and produce a bilingual CLIL lesson package.

### 2. EMI Readiness Assessment (Small effort)
A self-assessment tool for schools using the existing PD-Slides quiz engine or LMS assignment system. Maps school capabilities against the 3-level EMI framework from QD 2371.

Everything else is **extending what's already built**.

---

## Architecture: How It Fits Together for EMI

```
┌─────────────────────────────────────────────────────┐
│                    SCHOOL ONBOARDING                 │
│  Credits-Mgmt: CRM → Contract → Org → Users/Classes │
│  + Hanoi Kit (DOCX templates for DoE submission)     │
└──────────────┬──────────────────────────────────────┘
               │
    ┌──────────▼──────────┐
    │   TEACHER TRAINING   │
    │  PD-Slides: EMI PD   │
    │  modules (CLIL, EMI  │
    │  methodology, English │
    │  self-assessment)     │
    │  → Certificate issued │
    │  → TeacherQualification│
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │   CONTENT CREATION   │
    │  lesson-agent: CLIL  │
    │  YAML flows → bilingual│
    │  lesson packages      │
    │  creator.learnery:    │
    │  custom CLIL slides   │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │   CONTENT DELIVERY   │
    │  LMS: courses, assign-│
    │  ments, quizzes, AI   │
    │  apps, analytics      │
    │  AI-Course-fresh:     │
    │  interactive ebooks,  │
    │  HCAI Engine (bilingual)│
    │  Mobile: student app  │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │   AI INFRASTRUCTURE  │
    │  ai-gateway: GPT-4o, │
    │  Claude, Gemini, image│
    │  gen, credit billing  │
    │  Chatbot personas for │
    │  English practice     │
    └──────────┬──────────┘
               │
    ┌──────────▼──────────┐
    │   MONITORING & ADMIN │
    │  LMS Analytics       │
    │  School Portal       │
    │  Credits-Mgmt admin  │
    │  EMI Readiness tool  │
    │  DoE compliance report│
    └─────────────────────┘
```
