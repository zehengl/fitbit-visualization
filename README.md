<div align="center">
    <img src="https://cdn1.iconfinder.com/data/icons/logos-1/24/technology-fitbit-512.png" alt="logo" height="128">
</div>

# fitbit-visualization

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

fitbit visualization

## Install

    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -U pip
    pip install -r requirements.txt

Use `pip install -r requirements-dev.txt` for development.

## Usage

Create a `.env` file with your data folder name. For example,

    # .env
    name=xxx

Then simply run the script.

    python inspect_sleep.py
    python inspect_weight.py

## Credits

- [Logo][1] by [Webalys][2]

[1]: https://www.iconfinder.com/icons/7763742/technology_fitbit_icon
[2]: https://www.iconfinder.com/webalys
