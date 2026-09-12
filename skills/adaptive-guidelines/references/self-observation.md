# Agent self-observation

Use this reference when the agent recognizes its own mistake or inefficient
approach in any phase: understanding the request, research, planning,
implementation, validation, review, communication, or handoff.

## Recognize a reusable lesson

Capture an agent action or omission with an observable consequence and a
concrete improvement for similar work. User correction is not required.
Qualifying signals include:

- Misreading a requirement, skipping a required step, or choosing an approach
  that caused avoidable rework.
- Repeating searches or failed attempts without incorporating their results.
- Spending time on unnecessary steps or reading broad material when a targeted
  lookup would have answered the question.
- Loading excessive context or producing verbose output that added no useful
  information, including avoidable token consumption.
- Discovering that action Y would have met the same requirement more directly
  than action X, with a task-specific reason for preferring Y next time.

Ground process lessons in the visible work: redundant calls, irrelevant
material loaded, a missed instruction, a review finding, or a corrected result.
Record measured time or token counts only when available. Otherwise describe
the observed waste qualitatively; do not invent numbers or claimed savings.

An expected failing test, a useful experiment that rules out an option, or an
external outage alone is not an agent mistake. Capture a lesson if the agent's
avoidable decision around it caused waste or an incorrect outcome. A vague
feeling that work was slow needs concrete evidence before persistent capture.

## Record the lesson

1. Identify the action or omission, its consequence, and the evidence. Separate
   the observed fact from any suspected cause; label an unknown cause as such.
2. State the narrow preventive behavior: when the same conditions apply, what
   should the agent do differently, and why? Keep required checks and user
   constraints intact when reducing effort.
3. Use the main skill's capture flow and ledger permission rules. Save eligible
   lessons at the next safe pause, even on their first occurrence or while
   correction is pending. Capture permission does not authorize the correction
   itself or changes to official instructions.
4. Record the correction or better approach and its verification state. If it
   is only proposed, say so; when resolving the original incident, update its
   evidence entry with the actual result. Assess use in a later work unit under
   the ledger's `Reuse validation` rules. A proposed improvement is not a
   proven saving.

Use an existing incident or verification report as evidence when available;
keep its detailed failure history there and the reusable behavior in the
guideline ledger.

At handoff, briefly mention newly saved lessons and their ledger location.
If nothing qualifies, automatic mode stays silent.
