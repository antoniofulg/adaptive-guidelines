# Skill proposals

Use this reference when recurring work suggests a new skill, or when reviewing
or applying a proposal. Evaluate during the existing checkpoint review.

## Choose the destination

- Keep a standalone behavioral rule in the appropriate guideline.
- Extend an existing relevant skill when the procedure fits its trigger and
  scope. Inspect available project and installed skills before proposing a new
  one; record the coverage gap rather than assuming none exists.
- Suggest a new skill when a bounded procedure recurs across separate work
  units, has a successful verified example, and benefits from reusable steps,
  decisions, or references. It needs its own clear trigger and useful outcome.
  A command or existing script may already cover the need without a new skill.

For example, keeping manifest versions aligned is a guideline. A repeatedly
validated procedure for preparing a package release may justify a skill.
Successful work alone can support a proposal; no error or user correction is
required. Keep grounded patterns with insufficient evidence as observations;
skip unsupported speculation. These criteria govern suggestions, not an
explicit user request to create a particular skill.

## Record and present

Without capture permission, present the proposal in conversation and offer
saving once at a checkpoint, as the ledger requires. The user can also approve
creation directly from that concrete summary; saving first is not required.

Persist only with the ledger's existing capture permission or an explicit
promotion request for the presented proposal. Deduplicate by procedure, trigger,
and scope; reuse the proposal's stable ID without resetting its status when
adding supporting work. Preserve the individual lessons, their evidence counts,
statuses, and destinations.

Store one proposal in the same ledger using the existing lifecycle statuses:

```md
## prepare-package-release

- Type: skill-proposal
- Status: candidate
- Proposed skill: package-release
- Scope: repository
- Context: Preparing a release of this repository's package.
- Trigger: A request to prepare a package release.
- Inputs: Target version and repository release instructions.
- Outcome: Consistent package versions and a validated release diff.
- Procedure: Locate version fields, synchronize them, run package checks,
  and summarize the release diff and results.
- Existing coverage: Available skills do not cover this package's release checks.
- Related lessons: align-manifest-versions, validate-package-installation
- Suggested destination: skills/package-release/SKILL.md
- Supporting work:
  - 2026-09-01 — `release/one` — Version alignment and package checks succeeded.
  - 2026-09-12 — `release/two` — The same preparation procedure passed its checks.
- History:
  - 2026-09-12 — candidate; repeated procedure with verified outcomes.
```

This is an illustrative record; store only actual available evidence. Omit
`Related lessons` when none exist. Cite real work-unit artifacts or existing
`Reuse validation` entries in `Supporting work`; do not manufacture lessons or
copy successful runs into an error record's `Evidence`. Skill-proposal
eligibility comes from the procedure criteria above, independently of
`candidate_threshold`. A proposal alone does not promote its related lessons.

Present the proposed name, trigger, scope, inputs, expected outcome, concise
procedure, evidence of recurrence and success, coverage gap, and destination.
Keep the summary short enough to approve as a concrete proposal. Offer creation
at the checkpoint; do not repeat an unchanged or rejected suggestion.

## Create after approval

`review`, `finish`, and automatic capture authorize proposals, not skill files.
An explicit `apply <proposal-id>` after the scope and destination were presented,
or equivalent approval, authorizes that creation and its ledger record. If no
ledger exists, keep capture manual unless standing permission already applies.
Honor an already explicit creation request without asking again.
`apply eligible` can include clearly presented, qualifying skill proposals when
the request accepts those scopes and destinations. Skip and report proposals
whose scope or destination remains unresolved, while continuing with the other
eligible candidates.

Before creating, recheck the supporting work, scope, conflicts, and existing
skill coverage. If an existing skill now covers the need, report the changed
destination instead of silently changing what was approved.

Create the smallest skill at the accepted destination, following available
authoring guidance. Define its trigger, inputs, outcome, procedure, and checks;
add references or scripts only when the procedure needs them. Check metadata,
paths, and a representative use case within the authorized scope before marking
the proposal `promoted` with date and destination. If validation fails, keep the
proposal unpromoted and record the remaining issue.

Creation does not execute the captured workflow, grant it standing execution
permission, or authorize global installation, publishing, commits, or pushes.
Keep the related lessons' statuses unchanged unless their own approved
promotion is also completed. Validity review and historical preservation apply
to the proposal as to other ledger records.
