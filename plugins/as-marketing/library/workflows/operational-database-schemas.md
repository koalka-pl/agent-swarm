# Operational Database Schemas

## 1. Contact and Market Signal Radar

### Fields
| Field | Type | Purpose |
|---|---|---|
| Name | Text | Person, organization, post, or signal label |
| Type | Select | Person; Organization/Signal; Post/Discussion |
| Organization | Text | Associated organization |
| Role / Context | Text | Current role or contextual description |
| Segment / Market | Select or Text | Active vertical, market, or audience |
| Topic | Text | Problem or theme |
| Source URL | URL | Canonical public evidence |
| Signal date | Date | Publication or event date |
| Why now | Long text | Evidence-based relevance |
| Recommended action | Select | Observe; Comment; Reply; Write; Use in content; Skip |
| Draft | Long text | Proposed comment or message |
| Status | Status | Lifecycle state |
| Last interaction | Date | Most recent verified interaction |
| Planned follow-up | Date | Next review or action date |
| Related asset | Text or relation | Content, offer, event, or proof asset |
| Outcome | Long text | Observable result |
| Notes | Long text | Caveats, identity checks, rejection reason |

### Status lifecycle
New → Review → Accepted → Actioned → Follow-up → Closed.

Rules:
- New requires a source and signal date.
- Review requires relevance and recommended action.
- Accepted records have human approval.
- Actioned records store actual action date and channel.
- Follow-up requires owner and date.
- Closed records store outcome or rejection reason.

### Suggested additions
Canonical identity key, author/commenter/operator role, expiry date, evidence confidence, relationship stage, owner, created/updated timestamps, dedup key, and do-not-contact flag.

## 2. Editorial Campaign Plan

### Fields
| Field | Type | Purpose |
|---|---|---|
| Working title | Text | Record label |
| Publication date | Date | Planned or actual date |
| Campaign week / sequence | Select or Number | Position in narrative |
| Segment / Market | Select or Text | Target market |
| Topic area | Text | Pillar or theme |
| Asset type | Select | Article, report, post, email, video, etc. |
| Channel | Select | Primary destination |
| Status | Status | Production lifecycle |
| Content objective | Text | Audience or business job |
| Primary thesis | Long text | Main claim or answer |
| Required evidence | Long text | Proof needed before drafting |
| Proposed structure | Long text | Brief outline |
| CTA | Text | Intended next action |
| Success criterion | Long text | Observable decision metric |
| Notes | Long text | Dependencies and caveats |
| Source / URL | URL | Published asset or primary source |

### Recommended status lifecycle
Placeholder → Idea → Research → Brief approved → Drafting → Review → Ready → Scheduled → Published → Measured → Refresh / Repurpose / Archive.

Rules:
- Research cannot advance without named evidence requirements.
- Brief approved requires audience, thesis, structure, limitations, CTA, and reviewer.
- Ready means evidence and editorial review passed.
- Published requires canonical URL and date.
- Measured requires an observation window and captured outcomes.

### Suggested additions
Campaign ID, audience, owner, reviewer, source records, derivative-of relation, dependency relation, evidence status, approval timestamp, actual publication date, metric window, result, and next decision.

## Governance
Use stable IDs, controlled status values, canonical URLs, timestamps, and explicit owners. Separate facts from inference. Preserve rejected records to improve scoring, but archive or minimize personal data that has no continuing operational use.