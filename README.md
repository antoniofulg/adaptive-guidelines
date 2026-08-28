# Adaptive Guidelines

[![skills.sh](https://skills.sh/b/antoniofulg/adaptive-guidelines)](https://skills.sh/antoniofulg/adaptive-guidelines)

Adaptive Guidelines turns recurring user corrections and stable project
conventions into small, reviewable guidelines. It adapts to an existing agent
workflow when one exists and falls back to evidence-based work-unit detection
for features, fixes, goals, reviews, migrations, and releases.

After standing permission, the skill can capture observations automatically
during matching agent turns, review useful candidates at meaningful
checkpoints, and suggest promotion. It is not a background service and never
silently edits official project guidelines.

## Install

Choose one installation method. Installing both the standalone skill and a
plugin can expose the same skill twice.

### Agent Skills installer

Install for Codex and Claude Code:

```bash
npx skills add antoniofulg/adaptive-guidelines \
  --skill adaptive-guidelines \
  --agent codex \
  --agent claude-code
```

Add `--global` to make it available across projects.

### Codex plugin

```bash
codex plugin marketplace add antoniofulg/adaptive-guidelines
codex plugin add adaptive-guidelines@adaptive-guidelines
```

Start a new Codex thread after installation so the new skill is discovered.

### Claude Code plugin

Run these commands inside Claude Code:

```text
/plugin marketplace add antoniofulg/adaptive-guidelines
/plugin install adaptive-guidelines@adaptive-guidelines
```

Marketplace skills are namespaced in Claude Code. Invoke this one with:

```text
/adaptive-guidelines:adaptive-guidelines enable
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

Then work normally. When the host activates the skill from a correction or
workflow checkpoint, the agent:

1. captures reusable corrections in the project ledger;
2. consolidates repeated observations;
3. reviews them when a work unit reaches a meaningful checkpoint;
4. suggests candidates worth promoting.

You only approve the candidates you want:

```text
$adaptive-guidelines apply <candidate-id>
```

Automatic capture is model-driven, not a background process. If you want a
deterministic end-of-feature checkpoint, run `finish` explicitly. Promotion
always remains manual.

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
| `enable` | Creates or finds the project ledger and grants standing permission for automatic observation capture. Run once per repository. | Ledger configuration |
| `capture` | Reviews the available conversation and work context now, then creates or updates reusable observations. | Ledger only |
| `review` | Rechecks observations for scope, duplicates, conflicts, evidence, wording, and destination; promotes eligible records to candidate status. | Ledger status and history only |
| `finish` | Treats the current moment as a work-unit checkpoint, then runs capture and review together. It reports uncertainty instead of claiming completion when a required gate is missing. | Ledger only |
| `apply <candidate-id>` | Rechecks one approved candidate, writes the smallest rule to the best official guideline, and records the promotion. | Official guideline and ledger |
| `apply eligible` | Applies every approved, unambiguous candidate that passes the promotion checks; skips and reports unresolved candidates. | Official guidelines and ledger |
| `status` | Summarizes observations, candidates, conflicts, and promoted records. | Nothing |
| `explain <candidate-id>` | Shows one record's normalized rule, evidence, scope, history, and suggested destination. | Nothing |
| `reject <candidate-id>` | Marks an incorrect or unwanted candidate as rejected while preserving its history. | Ledger only |
| `supersede <candidate-id>` | Retires an outdated rule in favor of a newer one without deleting its audit history. | Ledger only |

## Candidate storage

Project observations and candidates live in one tracked file:

```text
.adaptive-guidelines/ledger.md
```

Commit this ledger when its contents are project knowledge. It stores status,
scope, concise evidence summaries, and promotion history. It must not contain
raw conversations, credentials, customer data, personal data, or secrets.

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

Both plugin manifests use the same version. Bump them together before a
release.

## License

[MIT](LICENSE)
