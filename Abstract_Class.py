# Prevent user from creating an object of the abstract class and to ensure that the child class has implemented all the abstract methods of the parent class, we can use the abc module in Python. 
# The abc module provides a way to define abstract base classes (ABCs) and abstract methods.

# We need at least one abstract method in the abstract class. 
# An abstract method is a method that is declared, but contains no implementation.
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

# The Car class inherits from the Vehicle class and implements the go() method, which is required by the abstract base class.
class Car(Vehicle):
    def go(self):
        print("The car is moving")

#obj = Vehicle()  # This will raise an error because we cannot create an instance of an abstract class
cadillac = Car()  # This is fine because Car is a concrete class that implements the abstract method go()
cadillac.go()  # Output: The car is moving