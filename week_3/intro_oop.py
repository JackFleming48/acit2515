"""
Class: Defines a general category (ie: book, bank account)
    - Blueprint (or template) for creating an object
    - A custom data type

Object or Instance: a "thing" created out of a class
Attributes: values for a specific object
Methods: behevaiours (or capabilities) of a class
State: the current values of the attributes in an object

Important Concepts:
- Modelization
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

Modelization

- How can we describe a problem?
    - For the government: name, address, SIN #
    - At BCIT: name, student number, program

Encapsulation

- The state of an object should be changed by the object itself
- Use behaviours (= methods) to alter the state, instead of changing the attributes
- Some object oriented programming languages have a visibility feature - where you can make attributes private. 
  Only the object itself can change them.
- Does not exist in Python, but there is a convention: use `_` in the beginning of the attribute to mean its private.
- Using private attributes and using methods to change the state is called encapsulation

Abstraction

- The implementation of the behaviours of the object is the responsibility of the class
- Other objects should not depend upon private attributes or methods
- They should only use the public interface of the class: the public methods and attributes

Class syntax in Python

- class MyClassName: to define a new class "block"
- indent the code below
- except for the class variables, a class definition only has methods or functions.
- Methods are defined inside the class block, and receive self as the first parameter
- A special method is __init__ , always called upon initialization of the instance

Example:
"""

class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.program = "BCIT"

    def display(self):
        print(f"{self.name}, {self.student_number} - {self.program}")

    
john = Student("John Doe", "A01234567")
john.display()
bob = Student("Bobby", "A09876543")
bob.display()
print(type(bob))

"""
Self

- 

"""