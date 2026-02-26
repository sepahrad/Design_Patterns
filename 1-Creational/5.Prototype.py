# The Prototype Pattern is a creational design pattern that allows you to create new objects by cloning an existing one 
# (the "prototype") rather than creating them from scratch using a constructor.
# Python makes the Prototype pattern incredibly easy because it has a built-in copy module. You don't need to define a 
# complex interface; you just need to decide between a Shallow Copy and a Deep Copy.
# Shallow vs. Deep Copy
# Shallow Copy (copy.copy): Copies the object but shares the references to nested objects (like lists). 
# If you change a list in the clone, it changes in the original.
# Deep Copy (copy.deepcopy): Copies everything recursively. The clone is 100% independent.

import copy
from abc import ABC, abstractmethod

class Shape(ABC):
    def draw(self):
        pass

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def draw(self):
        print(f"Drawing a square of size {self.size}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle of radius {self.radius}")

class AbstractArt:
    def __init__(self, bg_color, shapes):
        self.bg_color = bg_color
        self.shapes = shapes
    
    def draw(self):
        print(f"Background color is {self.bg_color}")
        [x.draw() for x in self.shapes]


if __name__ == "__main__":
    shapes = [Square(2), Square(5), Circle(8)]
    art1 = AbstractArt("Red", shapes)

    art2 = copy.copy(art1)

    art1.draw()
    art2.draw()

    art3 = copy.deepcopy(art2)
    art3.bg_color = "Blue"
    art3.draw()

    art2.draw()