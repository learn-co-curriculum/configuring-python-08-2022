# Configuring Python Applications

## Learning Goals

- Find and install packages using PyPI and `pip`.

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

## Resources

- [Python 3 Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)
- [Traps for the Unwary in Python's Import System - Nick Coghlan](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)
- [Absolute vs Relative Imports in Python - RealPython](https://realpython.com/absolute-vs-relative-python-imports/)
- [What is `__pycache__`? - stackoverflow](https://stackoverflow.com/questions/16869024/what-is-pycache)
- [Python File I/O - Programiz](https://www.programiz.com/python-programming/file-operation)
