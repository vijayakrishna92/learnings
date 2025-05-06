# classes and objects
# In Python, a class is a blueprint for creating objects. An object is an instance of a class.
# A class can contain attributes (variables) and methods (functions) that define the behavior of the objects created from it.
# The class keyword is used to define a class, and the __init__ method is a special method that is called when an object is created from the class.
# The __init__ method is used to initialize the attributes of the class. It takes self as the first parameter, which refers to the instance of the class being created.
# The self parameter is used to access the attributes and methods of the class from within the class itself.
# The self parameter is not a keyword in Python, but it is a convention to use it as the first parameter of instance methods.
# You can use any name for the first parameter, but it is recommended to use self for readability and consistency.
# The class can also contain class variables, which are shared by all instances of the class, and instance variables, which are unique to each instance of the class.
# Class variables are defined outside of any methods, while instance variables are defined inside the __init__ method.
# The class can also contain static methods and class methods, which are defined using the @staticmethod and @classmethod decorators, respectively.
# Static methods do not take self or cls as the first parameter, while class methods take cls as the first parameter, which refers to the class itself.
# The class can also inherit from other classes, which allows for code reuse and the creation of a hierarchy of classes.
# Inheritance is defined by passing the parent class as a parameter to the child class when defining the child class.
# The child class inherits all the attributes and methods of the parent class, and can also override or extend them.
# Inheritance can be single or multiple, and Python supports multiple inheritance, which allows a class to inherit from multiple parent classes.
# The class can also contain properties, which are a way to define getters and setters for attributes using the @property decorator.
# Properties allow for encapsulation and control over how attributes are accessed and modified.
# The class can also contain magic methods, which are special methods that start and end with double underscores (__).
# Magic methods allow for operator overloading and customization of the behavior of the class when used with built-in functions and operators.
# Some common magic methods include __str__, __repr__, __add__, __sub__, __mul__, and __getitem__.
# These methods allow for string representation, addition, subtraction, multiplication, and indexing of objects, respectively.
# Magic methods are not called directly, but are called implicitly when the corresponding operation is performed on the object.
# The class can also contain decorators, which are functions that modify the behavior of other functions or methods.    

from packages.module_2 import Cat
cat = Cat("Whiskers")
print(cat.speak())  # Output: Whiskers says Meow!

class Dog:
    # class variable
    species = "Canis familiaris"

    # instance variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # class method
    @classmethod
    def get_species(cls):
        return cls.species

    # static method
    @staticmethod
    def is_dog():
        return True
    
    # magic method
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
if __name__ == "__main__": # main function to test the Dog class
    # create an object of the Dog class
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)

    # access instance variables
    print(dog1.name)  # Output: Buddy
    print(dog2.age)   # Output: 5

    # call instance method
    print(dog1.bark())  # Output: Buddy says Woof!

    # access class variable
    print(Dog.species)  # Output: Canis familiaris

    # call class method
    print(Dog.get_species())  # Output: Canis familiaris

    # call static method
    print(Dog.is_dog())  # Output: True

    # call magic method
    print(dog1)  # Output: Buddy is 3 years old.