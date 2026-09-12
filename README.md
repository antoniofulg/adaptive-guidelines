# Adaptive Guidelines

[![skills.sh](https://skills.sh/b/antoniofulg/adaptive-guidelines)](https://skills.sh/antoniofulg/adaptive-guidelines)

Adaptive Guidelines turns user corrections, stable project conventions, and
the agent's own mistakes or workflow inefficiencies into durable lessons and
small, reviewable guidelines. Learning can happen in any phase, from research
and planning to execution, validation, and handoff. It adapts to an existing
agent workflow or infers checkpoints from evidence when none is defined.

The skill looks for relevant saved lessons before work. After standing
permission, it can capture observations, assess later reuse, maintain lesson
validity, and suggest promotion at meaningful checkpoints. It is not a
background service and never silently edits official project guidelines.

## Install

```bash
npx skills add antoniofulg/adaptive-guidelines
```

## Use

Examples below use Codex syntax. Standalone Claude Code installations use
`/adaptive-guidelines`; marketplace plugins use
`/adaptive-guidelines:adaptive-guidelines`. Other Agent Skills hosts may use a
skill picker or natural language.

### Recommended: autonomous after `enable`

Run once in each repository:

```text
$adaptive-guidelines enable
```

Then work normally. When the host activates the skill at work-unit start,
resumption, a phase change, or a learning signal, the agent:

1. finds relevant saved lessons and checks their current applicability;
2. captures reusable corrections and self-observations in the project ledger,
   including during active work;
3. records meaningful results of later reuse and reviews affected lessons;
4. consolidates observations and suggests candidates worth promoting.

You only approve the candidates you want:

```text
$adaptive-guidelines apply <candidate-id>
```

Automatic capture is model-driven, not a background process. If you want a
deterministic end-of-feature checkpoint, run `finish` explicitly. Promotion
always remains manual.

### Learn from the agent's own work

The agent can recognize that it repeated an unproductive search, loaded too
much context, spent time on unnecessary steps, skipped a required check, or
chose X where Y would have met the same need more directly. It can save that
lesson without waiting for a user correction or the end of development.

The first grounded occurrence becomes an `observed` record: durable knowledge
that later work can consult. Evidence captures the phase, what happened, its
consequence, the known or suspected cause, what to do differently, and whether
the improvement has been verified. Time and token counts are included only
when measured; qualitative evidence can still establish avoidable waste.

For example, after reading the same unchanged references twice, the agent can
record a lesson to reuse the located reference before broadening its search.
One incident counts once, even if a check or the user also points it out.
Expected test failures and useful experiments alone are not agent mistakes.

Automatic persistence uses the same `enable` permission as user corrections.
Turning a lesson into an official instruction still requires `apply`.

### Reuse and maintain lessons

At the start or resumption of work, or when the phase changes, the agent searches
the existing ledger by the task's subject, scope, and context. It reads only
matching records, checks their evidence and validity, and keeps the selected
lessons available while that context remains current. If no ledger or relevant
lesson exists, the task continues without creating learning artifacts.

After actually using a lesson in a later work unit, the agent can add a
`Reuse validation` entry: `helped`, `inconclusive`, or `failed`, with observable
evidence. This is separate from verifying the original correction and does
not inflate the count of mistakes. Record results that change the assessment,
such as validating a previously untested alternative or finding contrary
evidence; routine successful reuse needs no entry.

During these lookups or reviews, evidence that a context no longer exists can
make a lesson `expired`; an established replacement makes it `superseded` with
a link to the replacement; unresolved contradictory evidence makes it
`conflicted`. Age alone does not invalidate a lesson. History remains in the
same ledger, and changes to an already promoted official rule still require
explicit approval. Reading requires no capture permission; automatic writes
use the existing `enable` permission.

### Manual workflow

Run each stage yourself when you want full control:

```text
$adaptive-guidelines capture
$adaptive-guidelines review
$adaptive-guidelines status
$adaptive-guidelines apply <candidate-id>
```

The sequence is:

```text
capture → review → inspect → apply
```

At the end of a feature or goal, `finish` is the shorter checkpoint flow:

```text
finish → capture + review
```

`finish` does not promote anything. Follow it with `apply <candidate-id>` after
reviewing the suggestion.

### Command reference

| Command | What it does | Writes |
| --- | --- | --- |
| `enable` | Creates or finds the ledger and grants standing permission for capture, reuse validation, and validity updates. Run once per repository. | Ledger configuration |
| `capture` | Reviews the available conversation and work context now, then creates or updates reusable observations. | Ledger only |
| `review` | Rechecks observations, later reuse, validity, conflicts, and destination; promotes eligible records to candidate status. | Ledger records and history only |
| `finish` | Treats the current moment as a work-unit checkpoint, then runs capture and review together. It reports uncertainty instead of claiming completion when a required gate is missing. | Ledger only |
| `apply <candidate-id>` | Rechecks one approved candidate, writes the smallest rule to the best official guideline, and records the promotion. | Official guideline and ledger |
| `apply eligible` | Applies every approved, unambiguous candidate that passes the promotion checks; skips and reports unresolved candidates. | Official guidelines and ledger |
| `status` | Summarizes observations, candidates, conflicts, and promoted records. | Nothing |
| `explain <candidate-id>` | Shows one record's normalized rule, evidence, scope, history, and suggested destination. | Nothing |
| `reject <id>` | Marks a lesson as rejected while preserving its history. | Ledger only |
| `supersede <id>` | Retires a ledger record in favor of an identified replacement; preserves history and the official guideline. | Ledger only |

## Candidate storage

Project observations and candidates live in one tracked file:

```text
.adaptive-guidelines/ledger.md
```

Commit this ledger when its contents are project knowledge. It stores status,
scope, evidence sources, concise self-observations, meaningful reuse results,
and promotion history. It must not contain raw conversations, credentials,
customer data, personal data, or secrets.

Local scratch data may use `*.local.md` or `.adaptive-guidelines/tmp/`; both are
ignored by the supplied `.gitignore`.

Promoted rules remain in the ledger for audit history, while the active rule
lives in the appropriate authoritative file such as `AGENTS.md`, an ADR,
testing guidance, or a specialized skill.

## Workflow compatibility

Adaptive Guidelines first reads the repository's instructions, goal/task state,
workflow artifacts, validation reports, and handoffs. When none exist, it uses
the requested outcome, material implementation, relevant verification, and
remaining work to infer a checkpoint. It does not invent workflow gates or
claim completion when a required verifier or final check is missing.

The canonical Agent Skill is
[`skills/adaptive-guidelines/SKILL.md`](skills/adaptive-guidelines/SKILL.md).
Codex and Claude Code manifests package that same skill without maintaining a
second copy.

## Development

Validate the repository package:

```bash
python3 scripts/validate_package.py
npx skills add . --list
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
```

Test the Claude Code plugin locally:

```bash
claude --plugin-dir .
```

Package versions live in both plugin manifests and the Claude marketplace
manifest, including its plugin entry. Keep these versions synchronized before
a release; Git tags use `vX.Y.Z`. The skill and its references ship together as
one versioned package.

## License

[MIT](LICENSE)
