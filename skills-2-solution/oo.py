
"""1. Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Abstraction
    Allows a programmer to hide certain pieces of their code from the
    interface that other programs or users interact with. By properly
    abstracting, a user of your class doesn't have to understand all of the
    internal details to use it properly, reducing complexity.

Polymorphism
    Allows for groups to share interchangeable functionality, so that
    component that do the same kinds of things can be used interchangeably.

Encapsulation
    Means that methods pertaining to certain parts of a program stays
    associated, or "belongs to", that part of the program. For example, all
    of the functionality of an exam can travel in an `Exam` class --- import
    that, and you get all of the parts.



2. What is a class?

A class is a "type of thing" --- like an `Exam`. It can define the kind of
information that type of thing needs to keep track of, as well as actions
it needs to perform. You can make individual instances of classes.


3. What is a method?

A method is a function that is associated to a class. A method is like a
behavior that a class can execute.


4. What is an instance in object orientation?

An instance is an individual occurrence of an object, the idea made
manifest. For a `Exam` class, each individual exam is an instance.


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

Class attributes exist on the class, whereas instance attributes exist on
the individual instances, and therefore their values may vary by instance.
For example, in a `Cat` class, it would make sense to have a class
attribute of `species` (which would have the value `Felis catus` for all
Cat instances), and an instance attribute of `name` (which would be
different for each Cat instance).
"""



#####################################################################

"""2. Road Class"""

class Road:
    """A road for motor vehicles."""

    num_lanes = 2
    speed_limit = 25

road_1 = Road()
road_2 = Road()

road_1.num_lanes = 4
road_1.speed_limit = 60

#####################################################################

"""3. Update Password"""

class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password

    def update_password(self, current_pw, new_pw):
        """Update user's password."""

        if current_pw == self.password:
            self.password = new_pw
        else:
            print('Invalid password')


#####################################################################

"""4. Build a Library"""

class Book:
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author
        print(self.title, self.author)

    # def __repr__(self):
    #     return f"<Book title={self.title} author={self.author}>"


class Library:
    """A library of books."""

    def __init__(self):
        """Create a library with an empty list of books."""

        self.books = []

    def create_and_add_book(self, title, author):
        """Add a book to the library."""

        self.books.append(Book(title, author))

    def find_books_by_author(self, name):
        """Return a list of books by the given author."""

        return [book for book in self.books if book.author == name]


#####################################################################

"""5. Rectangle"""

class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width


class Square(Rectangle):
    """A square."""

    def __init__(self, width):
        """Create a square with the given width."""

        super().__init__(width, width)

    def calculate_area(self):
        """Return the area of the square."""

        if self.length == self.width:
            return super().calculate_area()
        else:
            print('Invalid square')
