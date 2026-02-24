# The Composite Pattern is a structural design pattern that lets you treat individual objects and groups of objects uniformly.
# Think of a File System: you have Files and Folders. A Folder can contain Files, but it can also contain other Folders. 
# Whether you are "Checking the Size" of a single File or a whole Folder, the command is the same. 
# The Composite pattern allows you to ignore the difference between a "leaf" (the file) and a "container" (the folder).

# The Core Concept: The Tree Structure
# The Composite pattern is almost always used to represent Tree structures.
# Component: An interface/base class that defines common operations for both simple and complex objects.
# Leaf: The basic element that doesn't have children (e.g., a File).
# Composite: A container that holds children (Leaves or other Composites) and implements the same operations as the Leaf.

class Equipment:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class Composite:
    def __init__(self, name: str):
        self.name = name
        self.items = []

    def add(self, equipment: Equipment):
        self.items.append(equipment)
        return self
    
    @property
    def price(self):
        return sum([x.price for x in self.items])
    
    @price.setter
    def price(self, value):
        self.price = value
    


if __name__ == "__main__":
    computer = Composite("PC")
    processor = Equipment("Processor", 1000)
    hard_drive = Equipment("Hard Drive", 250)
    memory = Composite("Memory")
    rom = Equipment("Read only memory", 100)
    ram = Equipment("Random access memory", 75)

    mem = memory.add(rom).add(ram)
    pc = computer.add(processor).add(hard_drive).add(memory)

    print(pc.price)