#!/usr/bin/env python3

'''
explicit use of python3 in the shebang ensures that the script runs through
the python3 interpreter, regardless of the python environment.
'''

from book import Book
from fiction.fantasy.game_of_thrones import game_of_thrones
from nonfiction.biography.leonardo_da_vinci import leonardo_da_vinci
from nonfiction.biography.autobiography.narrative_of_the_life_of_frederick_douglass import (
    narrative_of_the_life_of_frederick_douglass
)

books = [
    game_of_thrones,
    leonardo_da_vinci,
    narrative_of_the_life_of_frederick_douglass
]

'''
`if __name__ == '__main__':` ensures that the script is only executed when
the specific file (library.py) is executed.

otherwise, the script runs when another file imports anything from it!
'''

if __name__ == '__main__':
    for book in books:
        if isinstance(book, Book):
            print(book)
