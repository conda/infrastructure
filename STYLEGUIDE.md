[ruff]: https://docs.astral.sh/ruff/
[ruff-rules]: https://docs.astral.sh/ruff/rules/
[mypy]: https://mypy.readthedocs.io/
[pytest]: https://docs.pytest.org/
[coverage]: https://coverage.readthedocs.io/
[black]: https://github.com/psf/black
[darker]: https://github.com/akaihola/darker
[isort]: https://github.com/PyCQA/isort
[flake8-use-fstring]: https://github.com/MichaelKim0407/flake8-use-fstring
[flake8-use-pathlib]: https://gitlab.com/RoPP/flake8-use-pathlib
[flake8-annotations]: https://github.com/sco1/flake8-annotations
[flake8-typing-imports]: https://github.com/asottile/flake8-typing-imports
[flake8-useless-assert]: https://github.com/decorator-factory/flake8-useless-assert
[flake8-spellcheck]: https://github.com/MichaelAquilina/flake8-spellcheck
[inclusive-google]: https://developers.google.com/style/inclusive-documentation
[inclusive-hubspot]: https://blog.hubspot.com/marketing/inclusive-language
[inclusive-apple]: https://support.apple.com/guide/applestyleguide/intro-apdcb2a65d68/1.0/web/1.0
[flake8-variables-names]: https://github.com/best-doctor/flake8-variables-names
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8-simplify]: https://github.com/MartinThoma/flake8-simplify
[flake8-docstrings]: https://github.com/PyCQA/flake8-docstrings
[check-docstring-first]: https://github.com/pre-commit/pre-commit-hooks#check-docstring-first
[docformatter]: https://github.com/PyCQA/docformatter
[sphinx.ext.autodoc]: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directive-autoproperty

## Conda Style Guide

This is a **collection of ideas** for Python-oriented projects in the conda ecosystem—not a single policy enforced everywhere. Repositories choose what runs in CI and pre-commit (for example, **Rust** projects such as **rattler** follow their own tooling and are outside this Python-centric list). When contributing, prefer the target repo’s **`pyproject.toml`**, **`ruff.toml`**, **`mypy`** config, and CI over this document.

The intention is to reduce context switching between projects, not to overburden contributors; if a guideline stops paying for itself in a given repo, drop or relax it there.

**Tooling:** Many Python projects standardize on **[Ruff]** for formatting and linting: **`ruff format`** (Black-compatible) and **`ruff check`** with project-selected rules in `pyproject.toml` / `ruff.toml`. Ruff covers much of what was historically split across Black, isort, and many flake8 plugins—see the **[rule index][ruff-rules]** for mappings. Legacy stacks (**`black`**, **`darker`**, standalone **`isort`** / flake8) remain acceptable until a project migrates.

The table lists **guidelines** first (each optional per repo unless that project’s CI says otherwise); the Tooling column names typical implementations (Ruff-related or legacy).

| | Policy | Tooling |
|---|---|---|
| <h5>0</h5> | Format code with **`ruff format`** (Black-compatible output). Legacy: **`black`** or **`darker`** on brownfield trees. | [`ruff format`][ruff] [`black`][black] [`darker`][darker] |
| <h5>1</h5> | Keep imports sorted (isort-compatible). Use Ruff’s import rules (e.g. **`I`**) or standalone **`isort`**. | [`ruff`][ruff] [`isort`][isort] |
| <h5>2</h5> | Prefer f-strings over all other string formatting styles (e.g. `str.format`, c-style). | [`flake8-use-fstring`][flake8-use-fstring] |
| <h5>3</h5> | Prefer `pathlib` over `os.path`. | [`flake8-use-pathlib`][flake8-use-pathlib] |
| <h5>4</h5> | Use typing (or gradually enforce for preexisting projects). | [`flake8-annotations`][flake8-annotations] |
| <h5>4.1</h5> | Define typing aliases at the top of files. | |
| <h5>4.2</h5> | Use `TYPE_CHECKING` import guard. Optional Ruff **`TC`** (flake8-type-checking) tightens type-only vs runtime imports; optional **`TID251`** / **`TID253`** (**banned-api**, **banned-module-level-imports**) steer heavy or misleading imports—**project-specific**. | [`flake8-typing-imports`][flake8-typing-imports] [`ruff`][ruff] (**`TC`**, **`TID251`**, **`TID253`**) |
| <h5>4.3</h5> | Optional **[mypy][mypy]** or Pyright for static typing beyond what Ruff checks—e.g. `disallow_untyped_defs`, `no_implicit_optional`, extra `enable_error_code`. | [`mypy`][mypy] |
| <h5>5</h5> | Define loggers at the top of files. Avoid **f-strings inside logging calls**—use lazy `%`-style arguments (or equivalent) so formatting runs only when the message is emitted. | [`ruff`][ruff] (**`G004`**) |
| <h5>6</h5> | Only use `assert` in tests. | [`flake8-useless-assert`][flake8-useless-assert] |
| <h5>7</h5> | Use American English. | [`flake8-spellcheck`][flake8-spellcheck] |
| <h5>7.1</h5> | Use inclusive language. See these other great resources for details: <ul><li>[Google][inclusive-google]</li><li>[HubSpot][inclusive-hubspot]</li><li>[Apple][inclusive-apple]</li></ul> | |
| <h5>7.2</h5> | Use descriptive variable names: <ul><li>no one-char variables</li><li>avoid abbreviations</li><li>avoid overloading builtins</li></ul> | [`flake8-variables-names`][flake8-variables-names] |
| <h5>8</h5> | When indicating a change that requires a future version of Python (or dropping a currently-supported version), use the following format:<br>`# FUTURE: <minimum Python requirement>, <details>`<br>e.g.:<br>`# FUTURE: Python 3.9+, replace with ...` | |
| <h5>8.1</h5> | Align syntax with supported Python versions—e.g. Ruff **`UP`** (pyupgrade) and **`FA`** / `from __future__ import annotations`. | [`ruff`][ruff] (**`UP`**, **`FA`**) |
| <h5>9</h5> | All public functions and module constants must include a docstring. | [`flake8-docstrings`][flake8-docstrings] [`docformatter`][docformatter] |
| <h5>9.1</h5> | Module constants are documented using Sphinx autodoc syntax:<br><pre># before constant<br>#: The Answer to the Ultimate Question of Life<br>ANSWER = 42<br><br># or inline<br>ANSWER = 42  #: Life</pre> | [`sphinx.ext.autodoc`][sphinx.ext.autodoc] |
| <h5>10</h5> | **[pytest][pytest]:** declare markers in config and use **`--strict-markers`**. Optionally treat **`PendingDeprecationWarning`**, **`DeprecationWarning`**, and **`FutureWarning`** as errors in tests (**`filterwarnings`**) so deprecations surface immediately. | [`pytest`][pytest] |
| <h5>11</h5> | **[coverage][coverage]:** shared **`pragma: no cover`** (and related) conventions; sensible **`omit`** lists so reports stay comparable across modules. | [`coverage`][coverage] |

| Other Tooling (often available as Ruff rules; see [rule index][ruff-rules]) |
|---|
| [`flake8-bugbear`][flake8-bugbear] |
| [`flake8-simplify`][flake8-simplify] |
