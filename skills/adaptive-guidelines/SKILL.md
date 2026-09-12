---
name: adaptive-guidelines
description: >
  Reuse durable lessons at work-unit start, resumption, or a phase change by
  checking for relevant saved guidance. Capture lessons when the user corrects
  an instruction or declares a convention, the agent identifies its own
  mistake or inefficiency, or a checkpoint surfaces reusable guidance. Use
  also to assess a lesson's later use or validity, suggest skills from recurring
  procedures, or when the user asks to remember or review lessons or invokes
  $adaptive-guidelines. Do not use for ordinary completion without relevant
  lessons or reusable procedures, or for unexplained tool failures.
license: MIT
---

# Adaptive Guidelines

Turn grounded user corrections, conventions, and agent self-observations into
durable lessons and small, reviewable project guidelines.

## Operating contract

- A **work unit** is any bounded research, plan, feature, fix, goal, issue batch,
  review, migration, release, or direct correction. Do not assume one workflow
  model or restrict learning to development.
- Discover and respect the repository's existing instructions, lifecycle,
  knowledge stores, and completion gates before using fallbacks.
- Commands are convenient intents, not a required parser or host integration.
- Analyze learning signals automatically. Persist observations automatically
  only when project instructions or the ledger grant standing capture
  permission.
- Never silently promote an observation into an official guideline. Explicit
  `$adaptive-guidelines apply <id>` or equivalent user wording authorizes the
  selected promotion, including a presented new-skill proposal with a clear
  scope and destination.
- Repository files provide cross-session memory. Do not imply access to hidden
  model memory or unavailable conversations.

When work-unit boundaries are unclear, read
[references/lifecycle-detection.md](references/lifecycle-detection.md) in full.
When assessing matched records or creating or updating persistent records, read
[references/ledger.md](references/ledger.md) in full. When the agent identifies
its own mistake or workflow inefficiency, read
[references/self-observation.md](references/self-observation.md) in full before
capturing the lesson.
When recurring procedures suggest a new skill, or when reviewing or applying a
skill proposal, read [references/skill-proposals.md](references/skill-proposals.md)
in full.

## Invocation modes

Interpret natural-language equivalents the same way.

- **Automatic:** Consult relevant saved lessons before work. Notice corrections
  and self-observations while continuing the main task. With standing
  permission, capture grounded lessons, meaningful reuse outcomes, and validity
  changes at the next safe pause. Review affected observations at meaningful
  checkpoints and suggest eligible candidates for promotion.
- **`enable`:** Locate or create the repository ledger and set standing capture
  permission to automatic. This does not enable automatic promotion.
- **`capture`:** Review available context now and create or update eligible
  observations. This invocation authorizes ledger changes, not guideline
  promotion.
- **`review`:** Re-evaluate observations, reuse outcomes, validity, conflicts,
  scope, wording, and destinations; assess whether recurring procedures justify
  a new skill. It may update the ledger, but must not create skills or change
  official guidelines.
- **`finish`:** Resolve the current work-unit checkpoint, then capture and
  review in one pass. This authorizes ledger changes, not promotion. If
  completion is uncertain, state that and still offer the review rather than
  claiming the work is complete.
- **`apply <id>` / `apply eligible`:** Recheck the selected candidate or every
  unambiguous eligible candidate, make the approved guideline change or create
  the approved skill at its accepted destination, then update ledger status.
- **`status` / `explain <id>`:** Read-only: summarize the ledger or show the
  evidence and lifecycle of one rule, including any validity concerns.
- **`reject <id>` / `supersede <id>`:** Preserve the record while changing its
  status and reason.

## Before work

At work-unit start or resumption, and when the phase or relevant context changes:

1. Locate the existing project learning store or the fallback at
   `.adaptive-guidelines/ledger.md`. If none exists, continue the task; lookup
   alone neither creates a ledger nor enables capture.
2. Search record IDs, rules, scope, and context for the current objective and
   phase. Match meaning as well as keywords. Read matching records in full,
   including their status and evidence, instead of loading the entire ledger.
3. Check applicability and validity using the ledger's rules. Exclude
   `rejected`, `expired`, `superseded`, and `conflicted` lessons from
   recommendations; follow a superseded record's replacement link and evaluate
   that record independently. For promoted lessons, check the current
   authoritative destination.
4. Select only lessons supported by current instructions and context. Keep
   their IDs and intended adjustments available for the current work unit.
   Observations inform the approach; they are not binding project rules.
   Uncreated skill proposals are suggestions, not callable skills.

Reuse this selection until the relevant context or ledger changes. If nothing
matches, continue without a learning report. Lookup is read-only; recording a
validity change or reuse outcome follows the existing capture permissions.

## Capture

For each user instruction, correction, or agent self-observation:

1. Check applicable `AGENTS.md`, `CLAUDE.md`, guidelines, ADRs, skills, and
   existing learning stores. Reuse an authoritative rule when one exists.
   For an actual failure to follow it, record the incident with a link to the
   rule instead of proposing a duplicate guideline.
2. Ignore task-only choices, inconclusive experiments, temporary workarounds,
   short-lived facts, unsupported inference, and context that cannot be safely
   preserved.
3. Normalize reusable guidance into one atomic rule. Preserve its narrowest
   valid scope, target, context, exceptions, and strength: preference or
   requirement.
4. Find a semantic equivalent before creating a record. Update its evidence
   without resetting its status or creating another wording of the same rule.
5. Record concise evidence tied to the work unit, source, and relevant phase.
   Never store raw conversation, secrets, personal data, or unnecessary
   sensitive context.

Use these defaults:

- One grounded correction or self-observation becomes `observed` and is
  durable as soon as capture is authorized; recurrence is not needed to save it.
- Two consistent occurrences make it eligible for `candidate` review. Count
  an incident once even if the agent, a check, and the user all identify it.
  Keep it `observed` if reusable scope or context remains unresolved.
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

At a phase transition, approach change, workflow-defined review, or completion
checkpoint, briefly check whether the agent made an avoidable mistake, spent
effort without useful progress, or found a better approach for similar work.
Capture grounded lessons through the same flow and review affected records.
Use existing pauses; do not add a separate retrospective gate.

For lessons actually used, assess whether they helped under the current
conditions. Record meaningful results in `Reuse validation` using the ledger
format, and review affected lessons when evidence changes their validity.

When related lessons or repeated successful work reveal a reusable procedure,
assess a skill proposal through the linked reference. Prefer a short guideline
or an improvement to an existing skill when that adequately covers the need.

If a repository completion gate fails, keep the work unit active and report the
decisive missing evidence. Still perform an explicitly requested capture or
review; do not present the checkpoint as successful completion.

If no useful candidate exists, omit the promotion suggestion in automatic mode.
For an explicit `capture`, `review`, or `finish`, report saved observations and
whether any guidance is eligible for promotion. For each candidate, report only:

- proposed rule;
- reason it is ready for review;
- scope and important exception;
- suggested destination;
- action needed from the user.

For a new-skill proposal, use the proposal summary defined in its reference.
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
4. For a guideline, add the smallest standalone rule. For an approved skill
   proposal, follow its creation and validation procedure. Keep supporting
   evidence in the ledger rather than in the generated instructions.
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
