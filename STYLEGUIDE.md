## Conda Style Guide

In an effort to decrease the context switching/learning barrier between the different projects within the Conda org a standard set of code styles is defined. The intention of these guidelines is not to overburden or complicate the contribution process, if any style starts to become a burden its inherent benefit should be reevaluated.

> ⚠️ See conda-incubator/ceps#24 for our policy regarding the Python versions Conda projects need to support. Conda plugins must also support this range of versions in order to continue to be of value to current users.

| | Policy | Tooling |
|---|---|---|
| <a name="0"></a>0 | Use `black` (or `darker` for preexisting projects). | [`black`](https://github.com/psf/black) [`darker`](https://github.com/akaihola/darker) |
| <a name="1"></a>1 | Prefer f-strings over all other string formatting styles (e.g. `str.format`, c-style). | [`flake8-use-fstring`](https://github.com/MichaelKim0407/flake8-use-fstring) |
| <a name="2"></a>2 | Prefer `pathlib` over `os.path`. | [`flake8-use-pathlib`](https://gitlab.com/RoPP/flake8-use-pathlib) |
| <a name="3"></a>3 | Define typing aliases at the top of files. | |
| <a name="4"></a>4 | Define loggers at the top of files. | |
| <a name="5"></a>5 | Only use `assert` in tests. | [`flake8-useless-assert`](https://github.com/decorator-factory/flake8-useless-assert) |
| <a name="6"></a>6 | Use descriptive variable names: <ul><li>no one-char variables</li><li>avoid abbreviations</li><li>avoid overloading builtins</li></ul> | [`flake8-variables-names`](https://github.com/best-doctor/flake8-variables-names) |
| <a name="7"></a>7 | When indicating a change that requires a future version of Python (or dropping a currently supported version) use the following format:<br>`# FUTURE: <minimum Python requirement>, <details>`<br>e.g.:<br>`# FUTURE: Python 3.9+, replace with ...` | |

| Other Tooling |
|---|
| [`flake8-bugbear`](https://github.com/PyCQA/flake8-bugbear) |
| [`flake8-simplify`](https://github.com/MartinThoma/flake8-simplify) |
