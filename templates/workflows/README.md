# Workflow templates

Jinja templates synced to downstream repos via
[`conda/actions/template-files`](https://github.com/conda/actions/tree/main/template-files).
Each consumer renders them into `.github/workflows/`.

## When to template here vs. `conda/actions`

These templates work well for small, repo-specific variation (matrix shape, workflow names,
template variables). If a workflow is getting hard to read, test, or keep YAML-safe, prefer a
reusable [workflow or composite action in `conda/actions`](https://github.com/conda/actions)
and call it from a thin workflow template instead.

## YAML-safe Jinja (current conventions)

Dependabot and our pre-commit YAML hooks parse these files **before** Jinja runs. The rules below
are what we follow today; more complex workflows may need different trade-offs, and this section
should be updated when they do.

**Block tags** — put `[% ... %]` on a YAML comment line prefixed with `template-files-`:

- `# template-files-if [%- if ... %]`
- `# template-files-else [%- else %]`
- `# template-files-endif [%- endif %]`
- `# template-files-raw [%- raw %]`
- `# template-files-endraw [%- endraw %]`

Use `raw`/`endraw` around shell that contains `[[ ... ]]`. Rendered workflows keep the
`# template-files-*` lines; GitHub Actions ignores them.

**Expressions** — do not start an unquoted scalar with `[[ ... ]]`. Use a quoted string or a
literal block:

```yaml
      - '[[ tests_workflow | default("Tests") ]]'
  PLATFORMS: |
    [[ (platforms | default(['Linux', 'macOS', 'Windows'])) | join('\n    ') ]]
```

**Conditionals and Dependabot** — both branches of an `if`/`else` remain in the unrendered YAML.
That is fine when `uses:` pins are not duplicated across branches (as in `build.yml`).

**Pre-commit** — `templates/workflows/*.yml` are checked by `check-yaml` and `yamlfmt`. Other
Jinja templates (for example `templates/dependabot.yml`) stay excluded.
