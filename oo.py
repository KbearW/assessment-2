"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

(replace this with your answer)


2. What is a class?

(replace this with your answer)


3. What is a method?

(replace this with your answer)


4. What is an instance in object orientation?

(replace this with your answer)


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

(replace this with your answer)
"""


"""2. Road Class"""


# Replace this with your code


"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password


"""4. Build a Library"""


class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author


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
