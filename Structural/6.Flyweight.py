# The Flyweight Pattern is a structural design pattern that lets you fit more objects into the available amount of RAM 
# by sharing common parts of state between multiple objects.
# Instead of keeping identical data in every single object, you keep it in a single "Flyweight" object and have many 
# objects point to it.

# The Problem: Memory Bloat
# Imagine you are building a Forest in a video game. You want to render 1,000,000 trees. Each tree has:
# Intrinsic State: Data that never changes (Mesh, Texture, Color).
# Extrinsic State: Data that changes for every tree (X, Y coordinates).

# If you store the 10MB texture inside every one of those 1,000,000 objects, your game will crash because it needs 10 Terabytes of RAM.
# The Solution: Shared State
# The Flyweight pattern splits the object into two parts:
# The Flyweight: Stores the heavy, shared data (the "Intrinsic" part).
# The Context: Stores the unique data (the "Extrinsic" part) and refers to the Flyweight.

from abc import ABC, abstractmethod
import random
import sys
import psutil
import os

def get_actual_ram():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / (1024 * 1024) # Convert to MB

class Sprite(ABC):
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod
    def move(self, x: int, y: int):
        pass

class FighterRank:
    private = 0
    sergeant = 1
    major = 2


class Fighter(Sprite):
    def __init__(self, rank: FighterRank):
        self.rank = rank
        self.data = " " * (1024 * 1024) # Add 1MB of dummy data to each object
    
    def draw(self):
        print(f"Drawing fighter {self}")

    def move(self, x: int, y: int):
        print(f"Moving fighter {self} to position {x}, {y}")

class FighterFactory:
    def __init__(self):
        self.fighters = {}
    
    def get_fighter(self, rank: FighterRank):
        if rank not in self.fighters:
            self.fighters[rank] = Fighter(rank)
        return self.fighters[rank]

class Army:
    def __init__(self):
        self.army = []
        self.factory = FighterFactory()

    def spawn_fighter(self, rank: FighterRank):
        #fighter = self.factory.get_fighter(rank)  # Reuses cached Fighter
        fighter = Fighter(rank)
        self.army.append(fighter)

    def draw_army(self):
        for fighter in self.army:
            if fighter.rank == FighterRank.major:
                print("M ", end="")
            elif fighter.rank == FighterRank.sergeant:
                print("S ", end="")
            else:
                print("P ", end="")
    

if __name__ == "__main__":
    print(f"RAM before: {get_actual_ram():.2f} MB")
    
    army_size = 10000
    army = Army() 

    for i in range(army_size):
        r = random.randrange(3)
        army.spawn_fighter(r)

    print(f"RAM after spawning {army_size} fighters: {get_actual_ram():.2f} MB")
