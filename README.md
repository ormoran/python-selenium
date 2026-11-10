# Selenium + pytest

A simple Python browser testing project. The test opens Google and checks that
the search field is visible.

## Features

- Selenium WebDriver and pytest
- Automatic download of the matching ChromeDriver through Selenium Manager
- Run tests with a visible browser window or in headless mode
- GitHub Actions workflow that runs tests on every push and pull request

## Requirements

- Python 3.12 or newer
- Google Chrome
- Internet access during installation and test execution

## Installation

In PowerShell, from the project directory:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Selenium Manager downloads a compatible ChromeDriver the first time the
browser is started.

## Running the tests

With a visible browser window:

```powershell
python -m pytest
```

In headless mode:

```powershell
$env:SELENIUM_HEADLESS = "1"
python -m pytest
```

## Project structure

```text
.
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── dependabot.yml
│   └── workflows/
├── tests/
│   └── test_google_search.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

`conftest.py` provides the `driver` fixture, which starts Chrome and closes the
browser after each test. Add new tests to the `tests/` directory in files named
`test_*.py`.

## GitHub Actions

The `.github/workflows/tests.yml` workflow runs tests on GitHub-hosted Ubuntu
for every push and pull request. Tests run in headless mode.

## Issues

Use the bug report or feature request template in the **Issues** tab.
