# Learneris EMI Strategy

Strategic positioning and product roadmap for Learneris as the leading EdTech platform for Vietnam's national EMI (English as a Medium of Instruction) initiative.

## The Opportunity

Vietnam's government has launched the most ambitious English education reform in the country's history:

- **QD 2371/QD-TTg (Oct 2025)**: Prime Minister's Decision approving the national plan "Making English the Second Language in Schools 2025-2035, Vision to 2045"
- **NQ 71-NQ/TW (Aug 2025)**: Politburo Resolution on breakthrough development of education
- **HCMC De An (2026)**: Ho Chi Minh City's own implementation plan covering all education levels from preschool to university
- **SGDDT-GDMN 2551 (2026)**: HCMC directive for English integration in preschool starting AY 2026-2027
- **KH 18/KH-BGDDT**: Ministry of Education plan to survey English proficiency of all teachers nationwide (Jan-Jun 2026)

### Scale of the Policy

| Metric | HCMC Alone |
|--------|-----------|
| Preschools targeted (by 2030) | 70% of all GDMN institutions |
| K-12 schools (by 2030) | 100% teaching English from Grade 1; 30% at Level 1 EMI |
| Teachers surveyed (2025) | 50,300 public school teachers |
| English language centers | 1,915 |
| Timeline | 3 phases: 2025-2030, 2030-2040, 2040-2045 |

The policy explicitly calls for:
- AI integration in English teaching (Step 3 of the implementation plan)
- Online learning platforms and bilingual digital content repositories
- Teacher proficiency assessment and development at scale
- CLIL (Content and Language Integrated Learning) methodology adoption
- Public-private partnership ("xa hoi hoa") for technology and content delivery

## Why Learneris Is Uniquely Positioned

### Prepared Go-to-Market Kit for Schools

Learneris has developed a **Hanoi EMI Standardized Kit** — a ready-to-submit document package designed to help schools apply for EMI pilot approval with their Department of Education. The kit is a Learneris-created asset (not a government document) that positions Learneris as the default technology partner:

1. **To Trinh** (Petition template) — names Learneris as the support tool
2. **De An** (Implementation Plan template) — names Learneris as the technical platform
3. **Phu Luc** (Partner Annex template) — names Vietlearn/AVS as delivery partners for Learneris
4. **Template** — standardized shell for any school to customize and submit

The goal is to make Learneris the **path of least resistance** for schools seeking EMI approval — a turnkey package that solves both the bureaucratic and technical hurdles simultaneously.

### Existing Product-Policy Alignment

| Policy Requirement | Learneris Capability | Status |
|-------------------|---------------------|--------|
| AI-powered English learning tools | ai-gateway (multi-model: GPT-4o, Claude, Gemini) | Live |
| Teacher training & certification | Credits-Management teacher certification pipeline | Building |
| Bilingual digital content | "Hoc Cung AI" curriculum (TH0, THCS, THPT) | Government-certified |
| Online learning platform | LMS (200K concurrent capacity target) | Live |
| Content creation at scale | lesson-agent ($0.10/lesson, 3 min/package) | Live |
| CLIL methodology support | AI-Course-fresh (Math/Science in English content) | Extensible |
| Teacher proficiency assessment | PD-Slides (6-7 hour training pathway) | Live |
| Mobile student access | Capacitor mobile app (iOS + Android) | Live |
| Information Security compliance | Level 3 certification (TT 12/2022/TT-BTTTT) | Certified |
| Curriculum government approval | VNIES appraisal certification (July 2025) | Certified |

### Competitive Moats

1. **Ready-made school onboarding kit** — Turnkey document package that embeds Learneris into EMI pilot applications
2. **Government certifications** — InfoSec Level 3 + VNIES curriculum approval (barriers competitors must clear)
3. **AI content production cost** — $0.10/lesson at 3 min vs 45 min manual
4. **Full-stack ownership** — Content + Platform + Training + Assessment in one vendor
5. **YCCD compliance tracking** — Element-by-element standard mapping (QD 3439) unmatched by competitors

## Product Roadmap: Extend, Don't Rebuild

> See [docs/product-alignment.md](docs/product-alignment.md) for the full mapping of every EMI need to existing Learneris capabilities.

Nearly every EMI requirement maps to something already built. The strategy is to **configure, extend, and rebrand** — not start from scratch.

### What We Already Have (Ready for EMI)

| EMI Need | Existing Product | What It Already Does |
|----------|-----------------|---------------------|
| Online learning platform | **LMS** | Full teacher+student platform, 6 content block types, AI quiz gen, analytics, EN/VI bilingual UI |
| Teacher training | **PD-Slides** | 8 training modules, quiz engine with leaderboard, bilingual certificates, EMI school variant already exists in activity data |
| Teacher certification | **Credits-Management** | Training pipeline with PENDING→APPROVED→ISSUED workflow, TeacherQualification model, 12 API endpoints |
| AI-powered tools | **ai-gateway** | Multi-model router (GPT-4o, Claude, Gemini), credit billing, failover — all products route through this |
| Content at scale | **lesson-agent** | 5-step pipeline (study guide→slides→teaching guide→quiz→interactive), $0.10/lesson, YAML extension system |
| Bilingual content | **AI-Course-fresh** | EN/VN toggle, EMI school variant, HCAI Engine bilingual mode (`biText(vn,en)`), 80+ lessons with bilingual infrastructure |
| Interactive activities | **AI-Course-fresh** | 25+ activity HTML files, 7 interactive types (sorting, matching, quiz, flashcard, fill-blank, sequence, memory), HCAI Engine with 20+ slide types |
| School onboarding | **Credits-Management** | Parse contract PDF → create org → users → classes → assign credits → Drive upload. CRM with pipeline stages. |
| School admin portal | **Credits-Management Portal** | Self-service: user mgmt, class mgmt, usage stats, CSV export, import pipeline, temp passwords |
| Mobile access | **Mobile app** | Capacitor 8 (iOS + Android) |
| Monitoring/reporting | **LMS + Credits-Mgmt** | Analytics dashboards, credit reports, usage rollups, finance module |
| Content creation SaaS | **creator.learnery** | AI course pipeline (title→objectives→outline→slides→PPTX), 7+ output languages, embed routes |

### What to Extend (Weeks, Not Months)

| Extension | Base Product | Work Required | Effort |
|-----------|-------------|---------------|--------|
| CLIL bilingual content generation | lesson-agent | Add `language: bilingual` mode + CLIL YAML flows (`clil-math.yaml`, `clil-science.yaml`) | 2-3 weeks |
| EMI teacher PD modules | PD-Slides | New content modules: "CLIL Methodology", "Classroom English", "Teaching Math in English" — using existing quiz/activity/cert infrastructure | 2 weeks |
| English practice AI chatbots | AI-Course-fresh | New chatbot personas (conversation partner, vocab drill, scenario practice) — same Azure OpenAI endpoint, new system prompts | 1 week |
| EMI course templates in LMS | LMS | Pre-configured course structures with CLIL content blocks | 1 week |
| Org-level analytics | LMS | Extend existing teacher-scoped analytics to school-wide view | 1-2 weeks |
| EMI metrics in School Portal | Credits-Management | Add EMI readiness scorecard, English exposure tracking, DoE report export | 2 weeks |
| Wire qualification gating | Credits-Management | Connect existing TeacherQualification → class assignment (planned Phase 4) | 1 week |

### Only 2 Net-New Builds

| New Build | Effort | Approach |
|-----------|--------|----------|
| **EMI Readiness Assessment** | Small (1-2 weeks) | School self-assessment questionnaire using existing PD-Slides quiz engine or LMS assignment system, mapped to QD 2371's 3-level framework |
| **CLIL Content Templates** | Medium (2-3 weeks) | New YAML prompt flows for lesson-agent: Vietnamese curriculum standard → bilingual lesson package with adjustable English ratio (20-100%) |

## Go-to-Market Strategy

### Immediate (April-May 2026)
- [ ] Deploy Hanoi Standardized Kit to target schools
- [ ] Engage HCMC SGDDT through KDI/school relationships
- [ ] Offer free EMI Readiness Assessment to pilot schools
- [ ] Position for HCMC's May 14, 2026 registration deadline (SGDDT-GDMN 2551)
- [ ] Create 2-3 EMI PD modules in PD-Slides (reuse existing format)

### Near-term (Q3-Q4 2026)
- [ ] Ship CLIL bilingual mode in lesson-agent
- [ ] Add EMI chatbot personas to AI-Course-fresh
- [ ] Launch EMI course templates in LMS with 5 pilot schools
- [ ] Add EMI metrics to School Admin Portal
- [ ] Present at YC W27 with EMI as the wedge story

### Medium-term (2027)
- [ ] 100+ schools on EMI platform
- [ ] Provincial Department of Education partnerships in 5+ provinces
- [ ] Southeast Asia pilot (Philippines)

## Policy Reference Documents

| Document | Issuer | Date | Key Content |
|----------|--------|------|-------------|
| QD 2371/QD-TTg | Prime Minister | Oct 27, 2025 | National EMI plan 2025-2035 |
| NQ 71-NQ/TW | Politburo | Aug 22, 2025 | Breakthrough education development |
| NQ 51/NQ-CP | Government | Mar 18, 2025 | Action program implementing KL 91 |
| KL 91-KL/TW | Politburo | Aug 12, 2024 | Continuation of NQ 29 education reform |
| CV 8151/BGDDT | MOET | Dec 11, 2025 | EMI implementation guidance |
| HCMC De An (draft) | UBND HCMC | 2026 | HCMC EMI plan 2025-2035 |
| SGDDT-GDMN 2551 | SGDDT HCMC | 2026 | Preschool English integration pilot |
| KH 18/KH-BGDDT | MOET | 2026 | Teacher English proficiency survey |
| Hanoi Standardized Kit | Learneris (internal) | Jan 2026 | Learneris-created template kit for school EMI applications |

## Repository Structure

```
emi-strategy/
├── README.md                    # This file — overview and roadmap
├── docs/
│   ├── product-alignment.md     # Existing product → EMI need mapping (START HERE)
│   ├── policy-analysis.md       # Detailed policy breakdown
│   ├── competitive-landscape.md # Competitor analysis
│   ├── product-specs/           # Feature specifications
│   └── go-to-market.md          # GTM playbook
├── research/
│   ├── hcmc-de-an-summary.md    # HCMC implementation plan analysis
│   ├── teacher-capacity.md      # Teacher proficiency data
│   └── market-sizing.md         # TAM/SAM/SOM analysis
└── assets/
    └── diagrams/                # Architecture and strategy diagrams
```

## Team

- **Kelsie Nguyen** — CPO/Strategy (ex-Recruit Holdings/Quipper)
- **Quoc Le** — CEO/Bizdev (ex-Instamo/Polariis)
- **Calvin Phan** — Project Management (ex-StarHub Singapore)
- **Mi Nguyen** — Strategy/Ops

Advisors: Harvard/NUS public policy professor, ex-OpenAI Gen AI Engineering Lead

## License

Proprietary — Learneris Pte. Ltd. (Singapore)
