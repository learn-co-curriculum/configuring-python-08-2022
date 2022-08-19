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

## File and Directory Structure

If you take a look at this repo, you'll notice a `lib/` directory with a number
of different subcategories: fiction and nonfiction, then further categories
within. You should also notice a `book.py` and `library.py`. We will be updating
these as we go along.

First and foremost: what differences do you notice between the fiction and
nonfiction directory structures?

<p align="center">
    <img src="https://www.clipartmax.com/png/middle/186-1862669_rich-thinking-emoji-face-emoji-apple.png"
         alt="Thinking emoji"
         width="400"
         height="400"/>
</p>

### `__init__.py`

In the olden days (pre-2016 or so), Python needed a little good faith gesture
from developers to recognize packages as true Python packages: `__init__.py`
was that gesture.

`__init__.py` in any directory told the interpreter that it should be on the
lookout for other Python modules in that directory. Python likes its developers
to be very explicit, so this allowed it to ignore any directories without the
file. This was useful for image files, markdown, HTML, and more.

> **IMPORTANT: Any package with an `__init__.py` and surrounding Python packages**
> **can be used in imports.**

Python 3.3 introduced implicit **namespace** packages. These are packages
without an `__init__.py` file but a `.py` file in some subdirectory. While this
is not the most explicit approach, it provides some benefits to the developer:

- No need for `__init__.py`. Any directory with a `.py` file in it or a
  subdirectory is a Python package.

- Separate grouping of tightly- and loosely-related modules: two namespace
  packages can exist in the same namespace.
  - _Think about it this way: if I have one set of modules that inherit from
    a "Tools" base class and one that inherit from another "Machines" base
    class, they might belong in a `workshop` namespace but not next to one
    another._

- Using `__init__.py` in Python 3.3+ overrides other packages in the same
  namespace, and can be used to flag current versions of directories.

#### Should I Use `__init__.py`?

This is a source of some contention in the Python community; just know that in
PEP guidelines, it's only suggested that you be consistent.

- If you're using `__init__.py` for every package, keep doing that.

- If you're using `__init__.py` for every active package, keep doing that.

- If you're never using `__init__.py`, keep doing that. You're living a blessed
life.

- If you're using `__init__.py` in some old packages but not new ones, you
  should probably remove it.

***

## Relative vs. Absolute Imports

Python allows you to retrieve modules and the objects within in two different
ways: **relative** and **absolute** imports.

### Relative Imports

Let's take a look at "The Narrative of Frederick Douglass" as we discuss
relative imports:

```py
from book import Book
from ...biography.leonardo_da_vinci import leonardo_da_vinci

narrative_of_the_life_of_frederick_douglass = Book(
    title="Narrative of the Life of Frederick Douglass",
    author="Frederick Douglass",
    inspired=leonardo_da_vinci
)
```

Take a look at the imports at the top. What does this import syntax remind you
of?

<p align="center">
    <img src="https://image.similarpng.com/very-thumbnail/2020/07/Thinking-emoji-face-vector-PNG.png"
         alt="Confused thinking emoji"
         width="400"
         height="400"/>
</p>

The syntax for relative imports in Python is based largely on the commands for
navigating directories in Unix. A single dot (`.`) denotes the current working
directory, two refers to the next directory up, and so on.

While relative imports have a familiar syntax, they are recommended against in
PEP-8. The relative locations of files can change, and although chains of
directory names can get long, the amount of saved space with relative imports
is usually trivial.

### Absolute Imports

Absolute imports follow the same structure as you've seen with imports from
Python's standard libraries and external libraries so far. There is a base
package or module that is added to the path- this would be the top-level package
containing `__init__.py` in Python 2 or any `.py` file in Python 3- and its
submodules are accessed through dot notation.

Let's look at `library.py` for some absolute imports:

```py
from book import Book
from fiction.fantasy.game_of_thrones import game_of_thrones
from nonfiction.biography.leonardo_da_vinci import leonardo_da_vinci
from nonfiction.biography.autobiography.narrative_of_the_life_of_frederick_douglass \
    import narrative_of_the_life_of_frederick_douglass
```

While you can see that the last of the imports here is quite long, it should be
noted that this is the same import statement that one would use in a relative
format. Going down the line in our directory structure takes up some space, but
it's very explicit and easy to refactor should the need arise later on.

***

## The Python Package Index (PyPI)

One of Python's best features is its standard library. The standard library
includes over 200 modules written in C that provide developers access to a
computer's environment, operating system, and files, as well as important
functionality like regular expressions (through `re`) and basic database
connectivity (through `sqlite3`). That being said, there are still many tasks
that require external libraries. Most of these libraries are available through
the Python Package Index, or PyPI.

Run `lib/library.py` and you'll see that we're missing a PyPI package called
"Faker". Let's search for "Faker" on PyPI and implement it in our `Book` class.

<img src="https://curriculum-content.s3.amazonaws.com/python/fakerpypi.png"
 alt="screenshot of Faker on PyPI"
 title="screenshot of Faker on PyPI" />

```console
$ pip install faker
# => Collecting faker
# =>   Downloading Faker-14.1.0-py3-none-any.whl (1.6 MB)
# =>      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.6/1.6 MB 6.4 MB/s eta 0:00:00
# => Collecting python-dateutil>=2.4
# =>   Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
# => Requirement already satisfied: six>=1.5 in /Users/me/.pyenv/versions/3.8.13/lib/python3.8/site-packages (from python-dateutil>=2.4->faker) (1.16.0)
# => Installing collected packages: python-dateutil, faker
# => Successfully installed faker-14.1.0 python-dateutil-2.8.2
```

Now let's implement it in `book.py`:

```py
from faker import Faker
from datetime import datetime

class Book:
    def __init__(self,
            title,
            author, 
            inspired=None):
        
        self.title = title
        self.author = author
        self.inspired = inspired

        now = datetime.now()
        self.published_date = f'{now.month}/{now.day}/{now.year}'

        fake = Faker()
        self.published_location = fake.city()
        
    def __repr__(self):
        return 'Book({} by {})'.format(self.title, self.author)
```

> NOTE: we can import `datetime` without a `pip` command- this is because it's
> part of Python's standard library!

Run `lib/library.py` and you should see something similar to the following:

```console
# => Book(Game of Thrones by George R. R. Martin)
# => Published on 8/18/2022 at Hannahfurt.
# => Book(Leonardo da Vinci by Walter Isaacson)
# => Published on 8/18/2022 at East Douglaschester.
# => Book(Narrative of the Life of Frederick Douglass by Frederick Douglass)
# => Published on 8/18/2022 at North Scottfurt.
```

***

## I Don't Want Every PyPI Library to Live on my Computer Forever!

Most people don't!

Run `pip freeze` to see what you have installed:

```console
$ pip freeze
# => certifi==2022.5.18.1
# => distlib==0.3.4
# => Faker==14.1.0
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

You might not see all of the same stuff here. That's OK!

We definitely don't need Faker for every project, so let's remove it.
If you've been coding along, run `pip uninstall Faker==14.1.0`:

```console
$ pip uninstall Faker==14.1.0
# => Found existing installation: Faker 14.1.0
# => Uninstalling Faker-14.1.0:
# =>   Would remove:
# =>     /Users/me/.pyenv/versions/3.8.13/bin/faker
# =>     /Users/me/.pyenv/versions/3.8.13/lib/python3.8/site-packages/Faker-14.1.0.dist-info/*
# =>     /Users/me/.pyenv/versions/3.8.13/lib/python3.8/site-packages/faker/*
# => Proceed (Y/n)? Y
# =>   Successfully uninstalled Faker-14.1.0
```

All set! In the next lesson, we'll learn about managing dependencies in a
virtual environment.

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
