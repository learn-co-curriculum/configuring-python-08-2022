# Configuring Python Applications

## Learning Goals

- Configure an application with modules that can `import` from one another.
- Find and install packages using PyPI and `pip`.
- Control dependencies in virtual environments with `pipenv`.

***

## Key Vocab

- **Interpreter**: a program installed on your computer that looks at and runs
  Python code. It can be used to open interactive shells and execute code.
- **Python 2**: an old version of Python. Some thought it would never end! Many
  environment setups interpret `python` to mean "Python 2", so be explicit with
  `python3` when possible.
- **Python 3**: the current version of Python. Our environment setup
  instructions should direct all `python` commands to Python 3, but it is still
  always wise to use `python3` in your scripts.
- **Shebang**: `#!/usr/bin/env python3` should be included at the top of any
  modules that you intend to give executable permissions to. This tells the
  command line to execute the program using the `python3` interpreter so you
  don't need to type `python3` from the command line.
- **`__init__.py`**: a file required in Python 2 to create a Python package. No
  longer required in Python 3, but useful for backward compatibility and setting
  up environments within packages.
- **Relative Import**: an import that navigates through the application's
  directory structure with dots (`.`), much like you would from the command
  line. Relative imports are rarely the best option, and explicitly suggested
  against in PEP-8.
- **Absolute Import**: an import that uses the application structure to
  determine a base directory and any Python packages beneath it.
- **PYPI**: the **Py**thon **P**ackage **I**ndex. Contains most Python packages
  that can be retrieved with `pip`. Its search function is notoriously unhelpful.
- **Google**: a much better tool for finding Python packages by desired
  functionality.
- **`pip`**: the package installer from Python. Comes with any installation of
  Python.
- **`pipenv`**: a combination of `pip` and a virtual environment. Manages `pip`
  dependencies and saves them in `Pipfile`s that can be shared with teammates.

***

## Introduction

Welcome to Python PD!

We're starting today with a topic that's often a pain-point for Python
beginners: application structure. In time, Python's insistence on explicit
structure will save you time and frustration. That usually takes a while.

This is going to be structured as a **demo / Q & A**, with three sections of
material and three opportunities for questions. The curriculum team will keep
track of the chat throughout, and we will address the questions when each
section is complete. The first will be a bit longer than the other three.

While this is intended to be a demo rather than a code-along, a GitHub repo
will be shared in the chat in just a moment. Make sure to `fetch` all branches,
as they represent the endpoints of each section.

***

## Resources

- [Python 3 Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)
- [Traps for the Unwary in Python's Import System - Nick Coghlan](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)
- [Absolute vs Relative Imports in Python - RealPython](https://realpython.com/absolute-vs-relative-python-imports/)
- [What is `__pycache__`? - stackoverflow](https://stackoverflow.com/questions/16869024/what-is-pycache)
- [Python File I/O - Programiz](https://www.programiz.com/python-programming/file-operation)
