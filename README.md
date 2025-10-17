# poetry-analysis

[![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fnorn-uio%2Fpoetry-analysis%2Frefs%2Fheads%2Fmain%2Fpyproject.toml)](https://www.python.org/downloads/)
[![PyPI - Version](https://img.shields.io/pypi/v/poetry-analysis)](https://pypi.org/project/poetry-analysis/)
[![License](https://img.shields.io/pypi/l/poetry-analysis)](https://creativecommons.org/licenses/by/4.0/deed.en)
[![Github Action tests](https://github.com/norn-uio/poetry-analysis/actions/workflows/check.yml/badge.svg?branch=main&event=push)](https://github.com/norn-uio/poetry-analysis/actions/workflows/check.yml)

- **Github repository**: <https://github.com/norn-uio/poetry-analysis/>
- **Documentation**: <https://norn-uio.github.io/poetry-analysis/>

Rule-based tool to extract repetition patterns and other lyric features from poetry, or other text data where the newline is a meaningful segment boundary.

Lyric features that can be extracted with this tool includes

- end rhyme schemes
- alliteration
- anaphora
- lyrical subject

`poetry_analysis` has been developed alongside [NORN Poems](https://github.com/norn-uio/norn-poems), a corpus of Norwegian poetry from the 1890's, which is freely available to use with this tool.

## Installation

This library requires python >= 3.11. Create and activate a virtual environment before installing, e.g. with [`uv`](https://docs.astral.sh/uv/):

```shell
# Create environment with uv
uv venv --python 3.11

# Activate environment
source .venv/bin/activate

# Install poetry_analysis
pip install poetry-analysis
```

## Contact

This tool was developed as a collaboration project between a literary scholar and a computational linguist in the [NORN project](https://www.hf.uio.no/iln/english/research/projects/norn-norwegian-romantic-nationalisms/index.html):

- Ranveig Kvinnsland [<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/refs/heads/6.x/svgs/brands/github.svg" width="20" height="20">](https://github.com/ranveigk)
[<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/envelope.svg" width="20" height="20">](mailto:ranveig.kvinnsland@ibsen.uio.no)
- Ingerid Dale [<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/refs/heads/6.x/svgs/brands/github.svg" width="20" height="20">](https://github.com/ingerid)
[<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/envelope.svg" width="20" height="20">](mailto:ingerid.dale@nb.no)

If you discover any bugs, have any questions, or suggestions for improvements, please open an issue and assign an appropriate label to it. Contributions and pull requests are also welcome! Please check out the [contributing](./CONTRIBUTING.md) document for guidelines.
