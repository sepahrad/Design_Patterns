# The Decorator Pattern is a structural design pattern that lets you attach new behaviors to objects by placing these objects 
# inside special wrapper objects that contain the behaviors.
# Think of it like clothing: You are the base object. When you're cold, you wrap yourself in a sweater. 
# If it rains, you wrap yourself in a raincoat. You are still "you," but you’ve dynamically added "warmth" and "waterproofing" behaviors.

# Why use it?
# Avoids "Class Explosion": Instead of creating 50 different classes for every possible combination of features 
# (e.g., CoffeeWithMilk, CoffeeWithSugar, CoffeeWithMilkAndSugar), you create one Coffee and two decorators.
# Single Responsibility: You can divide a monolithic class that does everything into several smaller, focused classes.
# Runtime Flexibility: You can add or remove behaviors while the program is running, which you can't do with standard inheritance.

from abc import ABC, abstractmethod

class CoffeeMachine(ABC):
    @abstractmethod
    def make_small_coffee(self):
        pass

    @abstractmethod
    def make_large_coffee(self):
        pass

class BasicCoffeeMachine(CoffeeMachine):
    def make_small_coffee(self):
        print("Basic coffee machine is making Small coffee.")
    
    def make_large_coffee(self):
        print("Basic Coffee machine is making Large coffee.")

class EnhancesCoffeeMachine(CoffeeMachine):
    def __init__(self, basic_machine: BasicCoffeeMachine):
        self.basic_machine = basic_machine
    
    def make_small_coffee(self):
        self.basic_machine.make_small_coffee()
    
    def make_large_coffee(self):
        print("Enhanced Coffee Machine is making Large coffee.")

    def make_milk_coffee(self):
        print("Enhanced Coffee Machine: Making milk coffee.")
        self.basic_machine.make_small_coffee()
        print("Enhanced Coffee Machine: Adding milk.")


basic_machine = BasicCoffeeMachine()
enhanced_machine = EnhancesCoffeeMachine(basic_machine)

enhanced_machine.make_small_coffee()
print()
enhanced_machine.make_large_coffee()
print()
enhanced_machine.make_milk_coffee()

print("------------------------------------------------------------------------------------------------")

import functools

# 1. Define the Decorator
def my_logger(func):
    """A decorator that logs when a function is called."""

#    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Functing wrapper"""
        print(f"LOG: Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"LOG: {func.__name__} finished.")
        return result
    return wrapper

# 2. Apply the Decorator using @
@my_logger
def calculate_total(price, tax):
    """Calculating Tax""" 
    return price + (price * tax)

# 3. Call the function
print(f"Result: {calculate_total(100, 0.2)}")
print(calculate_total.__name__)
print(calculate_total.__doc__)
