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
