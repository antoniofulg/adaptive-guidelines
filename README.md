# Adaptive Guidelines

[![skills.sh](https://skills.sh/b/antoniofulg/adaptive-guidelines)](https://skills.sh/antoniofulg/adaptive-guidelines)

Adaptive Guidelines turns recurring user corrections and stable project
conventions into small, reviewable guidelines. It adapts to an existing agent
workflow when one exists and falls back to evidence-based work-unit detection
for features, fixes, goals, reviews, migrations, and releases.

The skill captures observations automatically only after standing permission,
reviews useful candidates at meaningful checkpoints, and never silently edits
official project guidelines.

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
/adaptive-guidelines:adaptive-guidelines finish
```

## Use

Codex examples:

```text
$adaptive-guidelines enable
$adaptive-guidelines capture
$adaptive-guidelines review
$adaptive-guidelines finish
$adaptive-guidelines apply <candidate-id>
$adaptive-guidelines status
```

Standalone Claude Code installations use `/adaptive-guidelines`. Other Agent
Skills hosts may use a slash command, a skill picker, or natural language. The
words after the skill name are intents, not a dependency on a command parser.

Typical setup:

1. Run `enable` once in a repository to permit automatic observation capture.
2. Work normally. The agent notices reusable corrections without interrupting
   active work.
3. At a workflow-defined checkpoint—or an inferred completed goal—the agent
   proposes only candidates worth reviewing.
4. Run `apply <candidate-id>` to promote an approved rule into the best existing
   project guideline.

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
