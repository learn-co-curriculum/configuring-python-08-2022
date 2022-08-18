# don't do relative imports unless they save you a lot of space
# python is as useful as it is because it is as specific as it is
# PEP-8 even suggests that you only use absolute imports

from book import Book
from ...biography.leonardo_da_vinci import leonardo_da_vinci

narrative_of_the_life_of_frederick_douglass = Book(
    title="Narrative of the Life of Frederick Douglass",
    author="Frederick Douglass",
    inspired=leonardo_da_vinci
)
