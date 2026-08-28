---
name: adaptive-guidelines
description: >
  Capture reusable user corrections and project conventions, infer meaningful
  work-unit checkpoints across different agent workflows, and propose or apply
  minimal guideline updates. Use when the user corrects or repeats an
  instruction, declares a durable project rule, asks to remember or review
  learned guidance, invokes $adaptive-guidelines, or completes a bounded goal
  after reusable guidance surfaced. Do not use for ordinary task completion
  when no reusable guidance appeared.
license: MIT
---

# Adaptive Guidelines

Turn grounded corrections and conventions into small, reviewable project
guidelines without treating every instruction as permanent.

## Operating contract

- A **work unit** is any bounded feature, fix, goal, issue batch, review,
  migration, release, or direct correction. Do not assume one workflow model.
- Discover and respect the repository's existing instructions, lifecycle,
  knowledge stores, and completion gates before using fallbacks.
- Commands are convenient intents, not a required parser or host integration.
- Analyze learning signals automatically. Persist observations automatically
  only when project instructions or the ledger grant standing capture
  permission.
- Never silently promote an observation into an official guideline. Explicit
  `$adaptive-guidelines apply <id>` or equivalent user wording authorizes the
  selected promotion.
- Repository files provide cross-session memory. Do not imply access to hidden
  model memory or unavailable conversations.

When work-unit boundaries are unclear, read
[references/lifecycle-detection.md](references/lifecycle-detection.md). When
creating or updating persistent records, read
[references/ledger.md](references/ledger.md).

## Invocation modes

Interpret natural-language equivalents the same way.

- **Automatic:** Notice reusable corrections while continuing the main task.
  At a meaningful checkpoint, suggest review only when something worth
  reviewing exists.
- **`enable`:** Locate or create the repository ledger and set standing capture
  permission to automatic. This does not enable automatic promotion.
- **`capture`:** Review available context now and create or update eligible
  observations. This invocation authorizes ledger changes, not guideline
  promotion.
- **`review`:** Re-evaluate observations, conflicts, scope, wording, and
  destinations. It may update ledger status and history, but must not change
  official guidelines.
- **`finish`:** Resolve the current work-unit checkpoint, then capture and
  review in one pass. This authorizes ledger changes, not promotion. If
  completion is uncertain, state that and still offer the review rather than
  claiming the work is complete.
- **`apply <id>` / `apply eligible`:** Recheck the selected candidate or every
  unambiguous eligible candidate, make the smallest change in the best existing
  guideline destination, then update ledger status.
- **`status` / `explain <id>`:** Summarize the ledger or show the evidence and
  lifecycle of one rule.
- **`reject <id>` / `supersede <id>`:** Preserve the record while changing its
  status and reason.

## Capture

For each user instruction or correction:

1. Check applicable `AGENTS.md`, `CLAUDE.md`, guidelines, ADRs, skills, and
   existing learning stores. Do not duplicate a rule already documented.
2. Ignore task-only choices, experiments, temporary workarounds, short-lived
   facts, unsupported inference, and context that cannot be safely preserved.
3. Normalize reusable guidance into one atomic rule. Preserve its narrowest
   valid scope, target, context, exceptions, and strength: preference or
   requirement.
4. Find a semantic equivalent before creating a record. Update its evidence;
   do not create another wording of the same rule.
5. Record a concise evidence summary tied to the work unit. Never store raw
   conversation, secrets, personal data, or unnecessary sensitive context.

Use these defaults:

- One reusable correction becomes `observed`.
- Two consistent corrections make it eligible for `candidate` review. Keep it
  `observed` if reusable scope or context remains unresolved.
- Recurrence across separate work units is stronger than repetition within
  one work unit.
- An explicit stable project convention may become a candidate immediately.
- “Add this to our guidelines” authorizes direct candidate review and, when
  the destination is clear, promotion.
- High impact raises review priority; it does not bypass promotion approval.

When evidence conflicts, compare scope and context. Represent a real exception
or narrower rule when both can coexist; otherwise mark the record `conflicted`
and do not enforce it.

## Checkpoint review

At a workflow-defined review or completion event—or a confidently inferred
goal completion—capture remaining signals and review affected records. Do not
interrupt active work for weak observations.

If a repository completion gate fails, keep the work unit active and report the
decisive missing evidence. Still perform an explicitly requested capture or
review; do not present the checkpoint as successful completion.

If no useful candidate exists, say nothing in automatic mode. For an explicit
`capture`, `review`, or `finish`, report that no eligible guidance was found.
If a candidate exists, report only:

- proposed rule;
- reason it is ready for review;
- scope and important exception;
- suggested destination;
- action needed from the user.

Do not repeat an unchanged suggestion at later checkpoints.

## Promotion

Before applying a candidate:

1. Recheck current instructions, semantic duplicates, conflicts, stability,
   and scope.
2. Prefer the existing authoritative destination: agent behavior in agent
   instructions, architecture in architecture docs or an ADR, test policy in
   testing guidance, and specialized procedures in the relevant skill.
3. If no authoritative destination exists, propose one and require the apply
   request to accept it before creating a new guideline file.
4. Add the smallest standalone rule. Keep evidence in the ledger, not in the
   official guideline.
5. Mark the record `promoted` with date and destination. Preserve rejected,
   superseded, and conflicted history.

Broad wording such as “promote everything eligible” authorizes promotion only
for candidates that pass every check above. Skip and report any candidate with
unresolved scope, destination, conflict, stability, or safety concerns.

A failed work-unit completion gate blocks the completion claim, not a separate
explicit promotion request. Promote an independently stable candidate only if
it passes the same checks; treat guidance derived from unfinished experiments
as unstable.

Promotion does not authorize commits, pushes, PRs, or unrelated cleanup.
