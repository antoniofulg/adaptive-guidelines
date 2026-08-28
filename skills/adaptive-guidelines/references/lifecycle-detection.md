# Workflow-agnostic lifecycle detection

Use this reference only when deciding whether a bounded work unit started,
reached a meaningful checkpoint, or ended.

## Work-unit model

A work unit is a bounded outcome, not a required artifact or phase name. It may
be a feature, fix, goal, issue batch, review, migration, release, or direct
correction. Nested tasks can belong to a larger work unit; completing a child
task does not necessarily complete its parent.

Track only enough lifecycle context to associate evidence and choose a review
checkpoint:

- name or concise outcome;
- parent work unit, if any;
- current state: inferred start, active, checkpoint, or complete;
- evidence supporting that state.

Do not create a separate lifecycle database.

## Discover the local workflow

Use the strongest available source, in this order:

1. Applicable repository instructions and workflow documentation.
2. Host-provided goal, issue, task, plan, or review state.
3. Repository artifacts such as specs, task lists, validation reports,
   handoffs, or release records.
4. Verification, review, Git, and changed-tree evidence.
5. Conversation intent and outcome as fallback.

Phase names are evidence only. Preserve local meaning: a project may require a
verifier, final QA, merge, or another gate before it considers work complete.
Do not replace that contract with generic heuristics.

Existing workflows may already maintain lessons or durable knowledge. Reuse
their lifecycle signals, but do not merge user-derived guideline observations
with verification failures or other knowledge categories whose semantics
differ.

## Start detection

A work unit probably starts when a bounded outcome becomes active and at least
one supporting signal exists:

- the user establishes a concrete capability, defect, or goal;
- a goal, issue, feature, or plan becomes active;
- a spec, task artifact, branch, or handoff identifies the work;
- material implementation begins after agreement on the outcome.

A vague discussion or isolated question is not a work-unit start. Do not wait
for a formal start marker when the outcome and active work are already clear.

## Checkpoint and completion detection

Prefer the workflow's authoritative terminal signal. Otherwise combine
evidence such as:

- the requested outcome is demonstrably satisfied;
- required tasks are complete;
- applicable validation or review passed;
- no known required work or blocker remains;
- the goal or issue reached its terminal state;
- the user or agent begins a final handoff.

A commit, code generation, passing one test, or an agent saying “done” is not
enough by itself when stronger completion requirements exist.

Classify the inference:

- **High:** workflow-defined terminal evidence is satisfied.
- **Medium:** outcome, relevant checks, and remaining-work evidence agree.
- **Low:** mainly conversational or ambiguous evidence.

At high or medium confidence, run checkpoint review when learning signals
exist. At low confidence, describe the possible checkpoint and suggest review;
do not assert completion or trigger unrelated workflow actions.

When an authoritative terminal check fails, keep the work unit active. Report
the shortest decisive failure and any required next lifecycle step. An explicit
adaptive-guidelines request still permits capture and review, but it does not
permit changing workflow state or claiming completion.

## Sparse-project fallback

When no descriptive workflow exists:

1. Derive the bounded outcome from the user's request.
2. Treat implementation or another material action as active work.
3. Use relevant verification and remaining-work checks as completion evidence.
4. Treat final handoff or explicit goal completion as a review checkpoint.

Do not invent artifacts, gates, commits, or process merely to improve lifecycle
confidence.

## Explicit override

`$adaptive-guidelines capture`, `review`, or `finish` is a checkpoint chosen by
the user. It does not prove the parent feature or goal is complete. Capture and
review the available context even when lifecycle evidence is incomplete, and
state uncertainty when it matters.
