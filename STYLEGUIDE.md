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

## Conda Style Guide

In an effort to decrease the context switching/learning barrier between the different projects within the Conda org, a standard set of code styles is defined. The intention of these guidelines is not to overburden or complicate the contribution process; if any style starts to become a burden, its inherent benefit should be reevaluated.

| | Policy | Tooling |
|---|---|---|
| <h5>0</h5> | Use `black` (or `darker` for preexisting projects). | [`black`][black] [`darker`][darker] |
| <h5>1</h5> | Use `isort`. | [`isort`][isort] |
| <h5>2</h5> | Prefer f-strings over all other string formatting styles (e.g. `str.format`, c-style). | [`flake8-use-fstring`][flake8-use-fstring] |
| <h5>3</h5> | Prefer `pathlib` over `os.path`. | [`flake8-use-pathlib`][flake8-use-pathlib] |
| <h5>4</h5> | Use typing (or gradually enforce for preexisting projects). | [`flake8-annotations`][flake8-annotations] |
| <h5>4.1</h5> | Define typing aliases at the top of files. | |
| <h5>4.2</h5> | Use `TYPE_CHECKING` import guard. | [`flake8-typing-imports`][flake8-typing-imports]
| <h5>5</h5> | Define loggers at the top of files. | |
| <h5>6</h5> | Only use `assert` in tests. | [`flake8-useless-assert`][flake8-useless-assert] |
| <h5>7</h5> | Use American English. | [`flake8-spellcheck`][flake8-spellcheck] |
| <h5>7.1</h5> | Use inclusive language. See these other great resources for details: <ul><li>[Google][inclusive-google]</li><li>[HubSpot][inclusive-hubspot]</li><li>[Apple][inclusive-apple]</li></ul> | |
| <h5>7.2</h5> | Use descriptive variable names: <ul><li>no one-char variables</li><li>avoid abbreviations</li><li>avoid overloading builtins</li></ul> | [`flake8-variables-names`][flake8-variables-names] |
| <h5>8</h5> | When indicating a change that requires a future version of Python (or dropping a currently-supported version), use the following format:<br>`# FUTURE: <minimum Python requirement>, <details>`<br>e.g.:<br>`# FUTURE: Python 3.9+, replace with ...` | |

| Other Tooling |
|---|
| [`flake8-bugbear`][flake8-bugbear] |
| [`flake8-simplify`][flake8-simplify] |
