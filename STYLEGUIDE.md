## Conda Style Guide

In an effort to decrease the context switching/learning barrier between the different projects within the Conda org, a standard set of code styles is defined. The intention of these guidelines is not to overburden or complicate the contribution process; if any style starts to become a burden, its inherent benefit should be reevaluated.

| | Policy | Tooling |
|---|---|---|
| <a name="0"></a>0 | Use `black` (or `darker` for preexisting projects). | [`black`](https://github.com/psf/black) [`darker`](https://github.com/akaihola/darker) |
| <a name="1"></a>1 | Use `isort`. | [`isort`](https://github.com/PyCQA/isort) |
| <a name="2"></a>2 | Prefer f-strings over all other string formatting styles (e.g. `str.format`, c-style). | [`flake8-use-fstring`](https://github.com/MichaelKim0407/flake8-use-fstring) |
| <a name="3"></a>3 | Prefer `pathlib` over `os.path`. | [`flake8-use-pathlib`](https://gitlab.com/RoPP/flake8-use-pathlib) |
| <a name="4"></a>4 | Use typing (or gradually enforce for preexisting projects). | [`flake8-annotations`](https://github.com/sco1/flake8-annotations) |
| <a name="4.1"></a>4.1 | Define typing aliases at the top of files. | |
| <a name="4.2"></a>4.2 | Use `TYPE_CHECKING` import guard. | [`flake8-typing-imports`](https://github.com/asottile/flake8-typing-imports)
| <a name="5"></a>5 | Define loggers at the top of files. | |
| <a name="6"></a>6 | Only use `assert` in tests. | [`flake8-useless-assert`](https://github.com/decorator-factory/flake8-useless-assert) |
| <a name="7"></a>7 | Use American English. | [`flake8-spellcheck`](https://github.com/MichaelAquilina/flake8-spellcheck) |
| <a name="7.1"></a>7.1 | Use descriptive variable names: <ul><li>no one-char variables</li><li>avoid abbreviations</li><li>avoid overloading builtins</li></ul> | [`flake8-variables-names`](https://github.com/best-doctor/flake8-variables-names) |
| <a name="8"></a>8 | When indicating a change that requires a future version of Python (or dropping a currently-supported version), use the following format:<br>`# FUTURE: <minimum Python requirement>, <details>`<br>e.g.:<br>`# FUTURE: Python 3.9+, replace with ...` | |

| Other Tooling |
|---|
| [`flake8-bugbear`](https://github.com/PyCQA/flake8-bugbear) |
| [`flake8-simplify`](https://github.com/MartinThoma/flake8-simplify) |
