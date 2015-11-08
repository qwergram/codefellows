# Code Fellows Python Test
class Library:
    def __init__(self):
        self.shelves = []

    def shelves_report(self):
        return len(self.shelves)

    def add_shelf(self, shelves):
        if type(shelves) == Shelf:
            shelves = [shelves]

        for shelf in shelves:
            assert type(shelf) == Shelf
            self.shelves.append(shelf)

    def remove_shelf(self, shelves):
        if type(shelves) != list:
            shelves = [shelves]

        for book_id in shelves:
            if type(shelf) == int:
                self.shelves.pop(shelf)

            elif type(shelf) == str:
                for book in self.shelves:
                    if str(book) == shelf:
                        self.shelves.remove(book)
            else:
                raise ValueError('Invalid Input type')


    def books_report(self):
        books = [str(book) for shelf in self.shelves for book in shelf.books]
        if books:
            return ' == [ ' + str(len(books)) + ' Books Total on ' + str(len(self.shelves)) + ' shelves ] ==\n - ' + '\n - '.join(books)
        else:
            return '== [No Books Found! :(] =='

class Shelf:
    def __init__(self):
        self.books = []

    def add_books(self, books):
        if type(books) == Book:
            books = [books]

        if type(books) == list:
            for book in books:
                assert type(book) == Book
                self.books.append(book)
        else:
            raise ValueError('Invalid Input')

    def remove_books(self, book_ids):
        if type(book_ids) != list:
            book_ids = [book_ids]

        for book_id in book_ids:
            if type(book_id) == int:
                self.books.pop(book_id)

            elif type(book_id) == str:
                for book in self.books:
                    if str(book) == book_id:
                        self.books.remove(book)
            else:
                raise ValueError('Invalid Input type')


    def books_report(self):
        if self.books:
            return ' == [ ' + str(len(self.books)) + ' Books Total ] ==\n - ' + '\n - '.join([str(book) for book in self.books])
        else:
            return '== [No Books Found! :(] =='

    def __str__(self):
        return self.books_report()

class Book:
    def __init__(self, book_name):
        assert type(book_name) == str
        self.name = book_name

    def __str__(self):
        return self.name


Lib1 = Library()
HouseOfWolves = Book('House of Wolves')
DragonRider = Book('Dragon Rider')
CookBook = Book('Book of Good Eats')
Spells = Book('Book of evil spells')
FirstShelf = Shelf()
FirstShelf.add_books(CookBook)
FirstShelf.add_books([HouseOfWolves, DragonRider, Spells])
Lib1.add_shelf(FirstShelf)
print(Lib1.books_report())
# print(FirstShelf)
# FirstShelf.remove_books
