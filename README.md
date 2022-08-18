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

## `pipenv`

Run `lib/library.py` real quick.

Does it work?

Of course not! We just uninstalled Faker!

<img src="https://c.tenor.com/KLpryzwu7qAAAAAC/of-course-not-edward-cullen.gif"
 alt="edward cullen of course not" />

We want to make sure that our projects that depend on certain external libraries
have access to them, but that those libraries aren't taking up space on our
computers or confusing our linters in other projects. There are a number of
tools available to Python developers for dependency management- in our
curriculum, we use `pipenv`.

`pipenv` is a tool that aims to bring the best of all packaging tools- bundler,
composer, npm, cargo, yarn- to the Python world. `pipenv` treats Windows as a
"first-class citizen" unlike many other tools that generate virtual
environments, so everyone at Flatiron should be able to use it without much
trouble.

`pipenv` automatically creates a virtual environment and adds packages to your
project's `Pipfile` (think `requirements`).

### Getting Started

`pipenv` is very easy to use- you can think of it as `pip` when you're setting
up, then as a virtual environment afterward. Let's get our application working
again. Run `pipenv install faker` from the command line:

```console
$ pipenv install faker
# => Creating a virtualenv for this project...
# => Pipfile: /Users/me/Documents/new-curriculum/delivery-pd/configuring-python-08-2022/Pipfile
# => Using /Users/me/.pyenv/versions/3.10.4/bin/python3 (3.10.4) to create virtualenv...
# => ⠸ Creating virtual environment...created virtual environment CPython3.10.4.final.0-64 in 224ms
# =>   creator CPython3Posix(dest=/Users/me/Documents/new-curriculum/delivery-pd/configuring-python-08-2022/.venv, clear=False, no_vcs_ignore=False, global=False)
# =>   seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/Users/me/Library/Application Support/virtualenv)
# =>     added seed packages: pip==22.2.2, setuptools==63.2.0, wheel==0.37.1
# =>   activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
# => 
# => ✔ Successfully created virtual environment!
# => Virtualenv location: /Users/me/Documents/new-curriculum/delivery-pd/configuring-python-08-2022/.venv
# => Creating a Pipfile for this project...
# => Installing faker...
# => Adding faker to Pipfile's [packages]...
# => ✔ Installation Succeeded
# => Pipfile.lock not found, creating...
# => Locking [dev-packages] dependencies...
# => Locking [packages] dependencies...
# => Building requirements...
# => Resolving dependencies...
# => ✔ Success!
# => Updated Pipfile.lock (63d9b1)!
# => Installing dependencies from Pipfile.lock (63d9b1)...
# =>   🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
# => To activate this project's virtualenv, run pipenv shell.
# => Alternatively, run a command inside the virtualenv with pipenv run.
```

Awesome! Now let's run `lib/library.py` again to see the desired output:

```console
$ lib/library.py
# => Traceback (most recent call last):
# =>   File "lib/library.py", line 13, in <module>
# =>     from book import Book
# =>   File "/Users/me/Documents/new-curriculum/delivery-pd/configuring-python-08-2022/lib/book.py", line 1, in <module>
# =>     from faker import Faker
# => ModuleNotFoundError: No module named 'faker'
```

<img src="https://c.tenor.com/u8UrPRK3BAAAAAAC/space-jam-lebron-james.gif"
 alt="lebron james that dude is a hater" />

While we have _created_ a virtual environment, we're not actually inside of it
yet. We have two options to get our code to run:

1. Stay outside of the virtual environment and execute code with `pipenv run`.
2. Enter the virtual environment with `pipenv shell`.

Let's try both to make sure everything works:

```console
$ pipenv run lib/library.py
# => Book(Game of Thrones by George R. R. Martin)
# => Published on 8/18/2022 at Lake Cynthia.
# => Book(Leonardo da Vinci by Walter Isaacson)
# => Published on 8/18/2022 at Coryland.
# => Book(Narrative of the Life of Frederick Douglass by Frederick Douglass)
# => Published on 8/18/2022 at South Shawna.

$ pipenv shell
# => Launching subshell in virtual environment...
# => . /Users/me/Documents/new-curriculum/delivery-pd/configuring-python-08-2022/.venv/bin/activate
$  . /Users/me/Documents/new-curriculum/delivery-pd/configuring-python-08-2022/.venv/bin/activate
(configuring-python-08-2022) $ lib/library.py
# => Book(Game of Thrones by George R. R. Martin)
# => Published on 8/18/2022 at Jeffreyhaven.
# => Book(Leonardo da Vinci by Walter Isaacson)
# => Published on 8/18/2022 at Nathanstad.
# => Book(Narrative of the Life of Frederick Douglass by Frederick Douglass)
# => Published on 8/18/2022 at North Patriciaton.
```

Excellent! Now let's make sure we aren't dealing with any pesky lingering
libraries. Exit your virtual environment with `exit` if you're coding along
and run `pip freeze` to see what we've got:

```console
$ pip freeze
# => certifi==2022.5.18.1
# => distlib==0.3.4
# => filelock==3.7.1
# => importlib-metadata==4.11.4
# => pipenv==2022.5.2
# => platformdirs==2.5.2
# => python-dateutil==2.8.2
# => six==1.16.0
# => virtualenv==20.14.1
# => virtualenv-clone==0.5.7
# => zipp==3.8.0
```

No Faker in sight- looks like `pipenv` kept our local environment clean!

### `Pipfile.lock`

The `Pipfile` lists all of your project's dependencies, so what's the point of
`Pipfile.lock`?

`pipenv` is like the bouncer at a club: it looks at the `Pipfile.lock` as a
guest list for your application's environment. It doesn't just look at the names
of the packages, it looks at _versions_ as well. (A good bouncer won't just let
any John Smith in, after all.)

If a user's `Pipfile` _perfectly_ matches the application's `Pipfile.lock`, they
are allowed into the virtual environment and all of the package dependencies
are installed.

***

## Resources

- [Python 3 Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)
- [Traps for the Unwary in Python's Import System - Nick Coghlan](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)
- [Absolute vs Relative Imports in Python - RealPython](https://realpython.com/absolute-vs-relative-python-imports/)
- [What is `__pycache__`? - stackoverflow](https://stackoverflow.com/questions/16869024/what-is-pycache)
- [Python File I/O - Programiz](https://www.programiz.com/python-programming/file-operation)
