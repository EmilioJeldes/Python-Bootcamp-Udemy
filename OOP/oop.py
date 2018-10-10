# Defining the simplest possible class


# The pass statement in Python is used when a statement is required syntactically but you do not want any command or
# code to execute.

# _name     : convention for private variables (not really)
# __name    : _NameClass__name (python mangle the name)
#             mainly used for inheritance so if both classes have the same attribute, it wont cause any conflicts
# __name__  : override method (dunder method).
#           : Python specific method

# __init__  : constructor
# __repr__  : toString
# class method attributes: Static atributes and methods
#                          are all shared between all class instances. Like a singleton object, same space in memory
# Inheritance syntax: class Cat(Animal):
#                     public class Cat extends Animal   # JAVA representation


class Person:
    
    # __init__ = constructor
    def __init__(self):
        self.name = "Tony"
        self._secret = "Hi"
        self.__msg = "I like turtles"
        self.__lol = "AHAHAHAHA"
    
    def __repr__(self) -> str:
        return f"name= {self.name}, _secret= {self._secret}"


person = Person()
print(person.name)
print(person._secret)
# Access mangle name
# print(person._Person__msg)
