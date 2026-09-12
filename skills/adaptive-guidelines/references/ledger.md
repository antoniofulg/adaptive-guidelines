# Repository ledger

Use this reference only when enabling persistent capture or reading, creating,
or updating adaptive-guideline records.

## Location

First inspect existing project conventions and knowledge stores. Reuse an
existing location when it can represent user-derived and agent-derived
behavioral lessons without changing that store's meaning. Keep raw verification
failures, product facts, and architectural decisions in their own stores;
reference them as evidence when they support a reusable behavioral lesson.

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
invocation, or an approved promotion request, authorizes ledger changes for
that request only. If it creates the ledger without standing permission, use
`capture_mode: manual`; do not turn a one-time request into future write
permission.

If neither standing nor current permission exists, retain only the available
conversational assessment and offer capture once at a meaningful checkpoint.

`promotion_mode: manual` means observations and candidates may be maintained,
but official guidelines change only after explicit approval. Do not weaken
this boundary because capture is automatic.

The same permission covers user corrections, agent self-observations, reuse
validation, skill proposals, and validity updates in every phase. Reading and
assessing a record requires no write permission. Without capture permission,
leave its record unchanged and disclose a validity concern only when it affects
the task.
Explicit read-only requests such as `status` and `explain` leave records
unchanged even with standing capture permission.
An `observed` record is already durable knowledge; candidate review and
promotion are separate decisions, not prerequisites for saving it.

## Record format

Keep one section per semantic rule. Existing records implicitly have type
`lesson`; no migration is needed. A `Type: skill-proposal` record instead
describes one bounded procedure and references related lesson IDs. When
creating or handling that type, use the format and eligibility rules in
[skill-proposals.md](skill-proposals.md) in full; its supporting work is
separate from lesson recurrence.

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
  - 2026-08-20 — `feature/imports` — Source: user correction; phase: setup.
    Corrected an npm install command.
  - 2026-08-28 — `feature/billing` — Source: user convention; phase: planning.
    Reaffirmed Bun as repository convention.
- History:
  - 2026-08-28 — observed → candidate; consistent evidence in two work units.
```

Derive a stable lowercase hyphenated ID from the normalized rule; add a narrow
scope discriminator only when needed to avoid a collision. Do not rename an ID
after its first persistent record. Omit fields that add no useful decision
context. Correction/observation recurrence is derived only from the `Evidence`
list; do not maintain a second counter that can drift. `First observed` and
`Last observed` describe those occurrences, not reads or successful reuse.

For each new occurrence, identify the source (`user correction`, `user
convention`, or `agent self-observation`) and the local phase name when known.
If other sources identify the same incident, retain its original source and
append their corroboration to that evidence entry.
For agent self-observations, include the action, consequence, evidence, cause
(confirmed, suspected, or unknown), correction or proposed alternative, and
verification result or pending state. Keep these details in the evidence
entry, so one rule can accumulate occurrences from different sources:

```md
- Evidence:
  - 2026-09-12 — `review/capture-flow` — Source: agent self-observation;
    phase: analysis.
    Action and consequence: Loaded the entire reference set twice while
    locating one permission rule, adding redundant context.
    Evidence: Both full-directory reads returned the same unchanged files;
    only references/ledger.md contained the relevant rule.
    Cause (confirmed): Repeated discovery without using the earlier result.
    Better approach (proposed): Reuse the identified file and read only the
    relevant section unless dependencies or changed content require more.
    Verification: Pending; no time or token savings measured.
```

The enclosing rule could be “Reuse located reference material for the same
question; broaden the search when the material changes or proves insufficient.”
Preserve existing evidence as written; annotate unknown historical sources only
when supported by available context. No ledger migration is required.

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

## Reuse validation

Verification in an original evidence entry describes that incident's
correction. When a lesson is actually used in a later work unit, assess its
effect separately at the next natural checkpoint. Use this optional field:

```md
- Reuse validation:
  - 2026-09-12 — `review/permission-followup` — Outcome: helped.
    Applied: Reused the previously located reference for the same question.
    Evidence: Resolved the question from that file without repeating the
    directory search; the required review was completed.
    Limits: No elapsed-time or token savings measured.
```

Use `helped`, `inconclusive`, or `failed`, supported by the action taken, its
observable result, and relevant conditions or limits. A read or the absence
of another error is not proof that the lesson helped. Compare observable
results while preserving the task's required quality and checks; report time
or token savings only when measured.

Write only evidence that changes an assessment: a first supported result for
an untested alternative, a meaningful inconclusive attempt, a contradiction,
or a materially different context. Repeated equivalent successes need no new
entry. Keep routine reuse out of `Evidence`; it neither adds an error occurrence
nor meets the candidate threshold. A separate qualifying mistake during reuse
still enters `Evidence` once through the capture flow.

Before treating a failed reuse as evidence against a lesson, check that its
conditions matched and the agent actually followed it. Distinguish an ineffective
lesson from failure to apply it; preserve inconclusive results as uncertainty.

## Validity review

Review the records being consulted or explicitly reviewed when current context
or new evidence calls their applicability into question. Use these criteria:

- Keep a lesson active when its conditions and evidence still hold. Age or
  lack of recent use alone does not invalidate it.
- Mark `expired` when evidence shows its applicable context no longer exists,
  such as a removed subsystem. A task outside its scope merely skips the lesson.
- Mark `superseded` when an existing, identified record replaces the same
  guidance. Add `Superseded by: <record-id>`; verify the target exists and the
  link introduces no cycle. A proposed alternative alone is not a replacement.
- If contrary evidence can be explained by context, narrow the lesson or
  record a contextual exception while preserving its evidence. Otherwise mark
  it `conflicted` and keep it out of recommendations pending resolution.

For each change, preserve the ID and prior evidence; append a dated history
entry with the old and new status, the reason, and supporting evidence. Include
the replacement ID when superseding. Preserve any earlier promotion destination
and date. Updating evidence does not automatically reactivate a rejected,
expired, superseded, or conflicted record.

These are ledger updates under capture permission, not edits to official
instructions. A validity change on a promoted record does not revoke the rule
at its destination: report the mismatch and require explicit authorization for
an official revision or removal. Current authoritative instructions still
govern the task; report a blocking conflict when they cannot be followed.

Use existing lookups and review checkpoints; do not add periodic full-ledger
scans or delete historical records.

## Invariants

- One semantic rule or skill proposal has one active record.
- Each lesson expresses one atomic behavior; each skill proposal describes
  one bounded procedure without merging its related lessons.
- Scope and context remain narrow enough for future use.
- Evidence is a concise paraphrase, never a raw conversation transcript.
- One incident contributes one occurrence, even when multiple sources report
  it. Updating its cause or verification does not increase recurrence.
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
