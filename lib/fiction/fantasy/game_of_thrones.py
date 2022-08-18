'''
`Book` can be imported using its module name (instead of a whole path)
because the interpreter automatically traverses backward to the base directory
to find a match.

Since `lib` is the highest directory that contains a python file and a valid
module name, `book` is visible from all the way down here.
'''

from book import Book

game_of_thrones = Book(
    title="Game of Thrones",
    author="George R. R. Martin"
)
