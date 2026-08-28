# Repository ledger

Use this reference only when enabling persistent capture or reading, creating,
or updating adaptive-guideline records.

## Location

First inspect existing project conventions and knowledge stores. Reuse an
existing location when it can represent user-derived guideline observations
without changing that store's meaning. Do not mix them with verification
lessons, product facts, or architectural decisions.

When no suitable store exists, use one repository-local, version-controlled
file:

```text
.adaptive-guidelines/ledger.md
```

Do not create separate observation, candidate, promoted, and rejected files.
Status transitions in one ledger provide the audit trail with less duplication.

## Standing capture permission

Automatic persistent capture requires either an applicable project instruction
or this ledger frontmatter:

```yaml
---
capture_mode: automatic
promotion_mode: manual
candidate_threshold: 2
---
```

`$adaptive-guidelines enable` creates or updates that frontmatter with
`capture_mode: automatic`. An explicit `capture`, `review`, or `finish`
invocation authorizes ledger changes for that request only. If it creates the
ledger without standing permission, use `capture_mode: manual`; do not turn a
one-time request into future write permission.

If neither standing nor current permission exists, retain only the available
conversational assessment and offer capture once at a meaningful checkpoint.

`promotion_mode: manual` means observations and candidates may be maintained,
but official guidelines change only after explicit approval. Do not weaken
this boundary because capture is automatic.

## Record format

Keep one section per semantic rule:

```md
## use-bun-for-package-management

- Rule: Use Bun for package management in this repository.
- Scope: repository
- Context: Dependency installation and package scripts.
- Strength: required
- Status: candidate
- First observed: 2026-08-20
- Last observed: 2026-08-28
- Suggested destination: AGENTS.md
- Evidence:
  - 2026-08-20 — `feature/imports` — Corrected an npm install command.
  - 2026-08-28 — `feature/billing` — Reaffirmed Bun as repository convention.
- History:
  - 2026-08-28 — observed → candidate; consistent evidence in two work units.
```

Derive a stable lowercase hyphenated ID from the normalized rule; add a narrow
scope discriminator only when needed to avoid a collision. Do not rename an ID
after its first persistent record. Omit fields that add no useful decision
context. Evidence count is derived from the list; do not maintain a second
counter that can drift.

Allowed statuses:

```text
observed
candidate
promoted
rejected
conflicted
superseded
expired
```

## Invariants

- One semantic rule has one active record.
- One record expresses one atomic behavior.
- Scope and context remain narrow enough for future use.
- Evidence is a concise paraphrase, never a raw conversation transcript.
- Do not store secrets, personal data, credentials, customer data, or
  unnecessary sensitive context.
- A contextual exception refines or splits a rule; it does not erase valid
  evidence from another scope.
- Rejected, conflicted, superseded, and promoted records remain auditable.
- Do not treat observations or candidates as binding instructions.

## Promotion update

After an approved guideline edit:

```md
- Status: promoted
- Promoted: 2026-08-28
- Destination: AGENTS.md
- History:
  - 2026-08-28 — candidate → promoted; approved by user.
```

Keep the official destination concise. The ledger explains why; the guideline
states only what future agents need to do.
