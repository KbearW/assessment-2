"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    1. Abstraction- Hiding details we don't need
    2. Encapsulation- Keeping everything "together"
    3. Polymorphism- Interchangeability of components

2. What is a class?

    Class is an object. 
    It defines class attributes and provides default values for instances.

3. What is a method?

    Method within a class can also be known as the dot method (aka a function) 
    and it always contain "self" as an argument.
    It is an instance within a class.
    For example:

        def speak(self):
            print("Woof!")
        fido = Animal()
        fido.speak() --> "Woof!"

    In this example, fido is an instances within the Animal class and 
    .speak() is a method (aka function) that modify the instance- "fido".
    
4. What is an instance in object orientation?

    An instance is a special case within the class. 
    In the example above, "fido" is part of the Animal class.

    Another way to think about class/ instance/ attribute is as follow:

        (class attributes can casade down to all the instances)

                            class    
            instance1                      instance2
    attribute1  attribute2           attributeA  attributeB
                
            (instance attributes can override class attributes)


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

    Class attribute can not override instance attribute. 
    It provides a default value for all instance attributes in the subclasses.

    For example, Animal is a class and class attribute: .color = pink.
    Dog, ant are instances within the Animal class.
    In this case, if instance dog is brown, then dog.color = brown 
    will override the class attribute of black.
    However, this will not have any effect on ant.color as it's still pink.

"""


"""2. Road Class"""

# create a class "Road"
class Road():
    
    # with two class attributes: num_lanes:2 and speed_limit:25
    def __init__(self):
        self.num_lanes = 2
        self.speed_limit = 25

# Instantiate 2 Road objects with variables called "road_1" and "road_2"
road_1 = Road()
road_2 = Road()

# Undate w instance attributes
road_1.num_lanes = 4
road_1.speed_limit = 60

# test cases:
# if __name__ == "__main__":
#     print(f'road_1.num_lanes: {road_1.num_lanes}')
#     print(f'road_1.speed_limit: {road_1.speed_limit}')
#     print(f'road_2.num_lanes: {road_2.num_lanes}')
#     print(f'road_2.speed_limit: {road_2.speed_limit}')
#     print(f'Q2: create a class "Road" is completed. Yay!')


"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password
    
    def update_password(self, current_pw, new_pw):
        """Method to update password"""
        
        if current_pw == self.password:
            self.password = new_pw
        else:
            print("Invalid password")

# test cases
# if __name__ == "__main__":
#     testcase = User("testusername", "initialpassword")
#     print(f"Original case's pw: {testcase.password}")
#     print("")
#     testcase.update_password("wrongpassword", "thispwshouldntshowup")
#     print(f"Failed case's pw: {testcase.password}")
#     print("")
#     testcase.update_password("initialpassword", "newpassword")
#     print(f"Success case's pw: {testcase.password}")


"""4. Build a Library"""


class Book(object):
    """A Book object. """

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author

class Library:
    """This is a new class "Library"."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.books = []

    def create_and_add_book(self, title, author):
        self.books.append(Book)
        

    def find_books_by_author(self, author):
        for self.author in self.books:
            print(self.books)



# test cases
if __name__ == "__main__":
    Library("Harry Potter","JK Rowing")
    # print(Library.books())
    # print(Library.create_and_add_book("Harry Potter","JK Rowing"))

    



"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""
        
        result = self.length * self.width
        # print(result)
        return (result)

class Square(Rectangle):
    """A square- subclass."""

    def __init__(self, length, width):
        super().__init__(length, width)

    def calculate_area(self):
        """Validate if square is valid"""

        if self.length == self.width:
            result = super().calculate_area()
            return result

        else:
            print("Invalid square")
            return None

if __name__ == "__main__":
    example1 = Rectangle(2, 3)
    print(f"Rectangle Area should be 6: {example1.calculate_area()}")
    print("")

    example2 = Rectangle(2, 2)
    print(f"Rectangle Area should be 4: {example2.calculate_area()}")
    print("")
    
    example3 = Square(2, 3)
    print(f"Rectangle Area should be None: {example3.calculate_area()}")
    print("")

    example4 = Square(2, 2)
    print(f"Rectangle Area should be 4: {example4.calculate_area()}")