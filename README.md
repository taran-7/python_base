# Python Base Learning Project

This repository is designed for learning the basics of Python.

## Prerequisites

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) — fast Python package manager (replaces pip, virtualenv, poetry)

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Environment Setup

1. **Clone the repository and navigate to the project:**

   ```bash
   git clone <repo-url>
   cd base_python
   ```

2. **Install all dependencies:**

   With uv (creates `.venv` automatically):

   ```bash
   uv sync
   ```

   Without uv (classic way):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .
   ```

3. **Activate the virtual environment:**

   ```bash
   source .venv/bin/activate
   ```

## Usage

Run the main script:

```bash
uv run main.py
```

Or with activated venv:

```bash
python main.py
```

## Managing Dependencies

### With uv

| Action                  | Command                  |
| ----------------------- | ------------------------ |
| Add a dependency        | `uv add <package>`      |
| Add a dev dependency    | `uv add --dev <package>` |
| Remove a dependency     | `uv remove <package>`   |
| Update lock file        | `uv lock`               |
| Install all from lock   | `uv sync`               |
| List installed packages | `uv pip list`           |

### Without uv (classic pip)

| Action                  | Command                               |
| ----------------------- | ------------------------------------- |
| Add a dependency        | `pip install <package>` + edit `pyproject.toml` manually |
| Remove a dependency     | `pip uninstall <package>`             |
| Install from project    | `pip install -e .`                    |
| Freeze dependencies     | `pip freeze > requirements.txt`       |
| Install from freeze     | `pip install -r requirements.txt`     |
| List installed packages | `pip list`                            |

All dependencies are stored in `pyproject.toml`. With uv, the `uv.lock` file pins exact versions for reproducible builds.

## Starting a New Python Project (Cheat Sheet)

### With uv

```bash
# 1. Create project directory
mkdir my_new_project && cd my_new_project

# 2. Initialize project (creates pyproject.toml + .venv)
uv init

# 3. Add dependencies
uv add requests flask

# 4. Initialize git
git init

# 5. Write code and run
uv run main.py
```

### Without uv (classic way)

```bash
# 1. Create project directory
mkdir my_new_project && cd my_new_project

# 2. Create virtual environment
python3 -m venv .venv

# 3. Activate it
source .venv/bin/activate

# 4. Install packages
pip install requests flask

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Initialize git
git init

# 7. Write code and run
python main.py

# 8. Deactivate when done
deactivate
```

> **Rule:** Each project = its own folder = its own `.venv`.
> Never share a virtual environment between projects.

Example of a properly organized workspace:

```
~/Documents/Python/
├── project_a/
│   ├── .venv/          # its own packages
│   └── pyproject.toml
├── project_b/
│   ├── .venv/          # its own packages
│   └── pyproject.toml
└── project_c/
    ├── .venv/          # its own packages
    └── pyproject.toml
```

## Virtual Environment (venv) Overview

A **virtual environment** is an isolated Python installation with its own packages, independent of the system Python.

**Why use it?**

- Different projects can require different versions of the same package
- `pip install` without venv installs packages globally, which can break other projects
- A venv makes it clear which dependencies belong to which project

**Structure of `.venv/`:**

```
.venv/
├── bin/            # python, pip, activate scripts
├── lib/            # installed packages (site-packages)
└── pyvenv.cfg      # environment configuration
```

> The `.venv/` folder is **never committed to Git** — it is listed in `.gitignore`.
> Instead, commit `pyproject.toml` and `uv.lock`.

## Development Tools

The project is configured with the following tools to ensure code quality:

- **Black**: Automatic code formatting.
- **Isort**: Import sorting.
- **Flake8**: Linter for checking errors and style.

Formatting is applied automatically when saving a file in VS Code.
