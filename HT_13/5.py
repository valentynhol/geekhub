"""
5. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
"""


class Library(object):
    bookshelf_count = 0

    def __init__(self, school, size=100):
        self.school = school
        self.library_size = size


class Librarian(object):
    name = 'Natalya'
    sex = 'Female'
    age = 43
    height = 163
    hair_colour = 'Black'
    eyes_colour = 'Green'

    def say_favourite_phrase(self):
        print('Shhhhhhh')

    def say_favourite_phrase_when_angry(self):
        print('SHHHHHHHHHHHH')

    def wear_glasses(self):
        print(self.name, 'weared glasses.')


class Bookshelf(Library):
    floors = 0
    books = 0

    def __init__(self, colour='White'):
        Library.bookshelf_count += 1
        self.bookshelf_colour = colour


class BookshelfFloor(Bookshelf):
    def __init__(self):
        BookshelfFloor.floors += 1

    def check_books(self):
        for i in range(4):
            print('You'+' really'*(i+1)+' wanna do it? y/n')
            if input() == 'n':
                print('So why you doing it? lol')
                break
            if i == 3:
                print('ahh ok... You see some colourful books')


class Book(Bookshelf):
    def __init__(self, title, pages, colour='White'):
        Bookshelf.books += 1
        self.book_title = title
        self.book_pages = pages
        self.book_colour = colour

    def open(self):
        print(f'shkhsh... {self.book_title} opened')

    def look(self):
        print(f'Hmm... a simple {self.book_title} book with {self.book_pages} pages')

    def read(self):
        print(f'OWWW {self.book_pages} PAGES *closed book*')

    def kick(self):
        print('Librarian: (╯ ° □ °) ╯ (┻━┻)')
