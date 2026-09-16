# Project Context

Schema version: 1

Single source of truth for this project, shared by every installed AgentSwarm plugin. Replace placeholders with verified facts. Mark anything unconfirmed as `unknown`. Each fact lives in exactly one place: shared facts go under Shared, plugin-specific facts under that plugin's section. Sensitive data (finances, contracts, personal data) does not belong here; keep it in the `private/` folder of the data directory.

## Shared

### Identity
- Project/company: [required]
- Product, service, or venture: [required]
- Website: [required — URL, or none]
- Geography: [optional]
- Stage: [required]

### Business outcome
- Current objective: [required]
- Time horizon: [required]
- Success criteria: [required]
- Failure/stop criteria: [required]

### Market and customer
- Priority audience/segment: [required]
- Buying situation/problem: [required]
- Alternatives: [known/unknown]
- Buying roles: [known/unknown]
- Evidence sources: [links or durable references]

### Offer and delivery
- Current offer: [required]
- Pricing/packaging: [known/unknown]
- Delivery model: [required]
- Capacity and constraints: [required]

### Approved decisions and exclusions
- [decision, date, owner, plugin]

### Assumptions and open questions
- [label every unverified item]

### Last verified
- Date: [required]
- Owner/source: [required]

## as-marketing

Owned by the as-marketing plugin. Other plugins may read it but propose changes in the data directory's `notes/` instead of editing it.

### Business model
- Primary business-model profile: [required]
- Secondary profile: [optional]
- Unit/service economics: [known/unknown]

### Go-to-market
- Current acquisition/distribution mechanisms: [required]
- Sales motion: [required]
- Conversion path: [required]
- Retention/expansion path: [known/unknown]

### Systems and measurement
- Sources of truth: [required]
- Available tools/integrations: [required]
- Current metrics: [known/unknown]
- Consent/privacy constraints: [required]

### Last verified
- Date: [required]
- Owner/source: [required]
