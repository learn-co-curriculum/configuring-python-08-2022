class Book:
    def __init__(self, title, author, inspired=None):
        self.title = title
        self.author = author
        self.inspired = inspired

    def __repr__(self):
        return 'Book({} by {})'.format(self.title, self.author)
