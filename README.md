# Configuring Python Applications

## Learning Goals

- Configure an application with modules that can `import` from one another.

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

## Resources

- [Python 3 Documentation](https://docs.python.org/3/)
- [Python Package Index (PyPI)](https://pypi.org/)
- [Pipenv: Python Dev Workflow for Humans](https://pipenv.pypa.io/en/latest/)
- [Traps for the Unwary in Python's Import System - Nick Coghlan](http://python-notes.curiousefficiency.org/en/latest/python_concepts/import_traps.html)
- [Absolute vs Relative Imports in Python - RealPython](https://realpython.com/absolute-vs-relative-python-imports/)
- [What is `__pycache__`? - stackoverflow](https://stackoverflow.com/questions/16869024/what-is-pycache)
- [Python File I/O - Programiz](https://www.programiz.com/python-programming/file-operation)
