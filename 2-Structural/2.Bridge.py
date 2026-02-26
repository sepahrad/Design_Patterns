# The Bridge Pattern is a structural design pattern that separates a large class or a set of closely related classes 
# into two separate hierarchies—Abstraction and Implementation—which can be developed independently.
# Think of it like a Universal Remote Control (the Abstraction) and the Electronic Devices (the Implementation) it controls. 
# You can update the remote's interface without changing how the TV works, and you can buy a new TV without needing a different remote.

# The Problem: The "Class Explosion"
# Imagine you are building an app with Shapes (Circle, Square) and Colors (Red, Blue). Without a Bridge, you end up 
# with 4 classes: RedCircle, BlueCircle, RedSquare, BlueSquare.
# If you add a third color (Green), you now need 6 classes. If you add a third shape (Triangle), you need 9. 
# This is a Cartesian Product nightmare.

# The Solution: The Bridge
# Instead of using inheritance to combine shapes and colors, you use Composition. You "Bridge" the Shape to a Color object.
# Abstraction: The "High-level" logic (The Shape).
# Implementation: The "Low-level" platform or detail (The Color).

# In programming, Composition is a design principle where one class contains an instance of another class as a part of its state. 
# Instead of saying a class is something (Inheritance), you say a class has something.
# Think of it like a Car: A car is not "a type of Engine" (Inheritance); rather, a car has an Engine, has Wheels, and has Seats.

# Key Differences: Bridge vs. Adapter
# People often confuse these two because both use composition to wrap an object. 
# The difference is the timing of when they are used: FeatureAdapter / PatternBridge Pattern
# When to use?: After code is written (Fixing a mismatch) / Before code is written (Upfront design)
# Goal: Make incompatible things work together / Keep hierarchies separate so they can grow
# Intent: Compatibility / Flexibility and Scalability

from abc import ABC, abstractmethod

class Device(ABC):
    volume = 0

    @abstractmethod
    def get_name(self) -> str:
        pass

class Radio(Device):
    def get_name(self) -> str:
        return f"Radio {self}"
    
class TV(Device):
    def get_name(self):
        return f"TV {self}"

class Remote(ABC):
    @abstractmethod
    def volume_up(self):
        pass

    @abstractmethod
    def volume_down(self):
        pass

class BasicRemote(Remote):
    def __init__(self, device: Device):
        self.device = device

    def volume_up(self):
        self.device.volume += 1
        print(f"{self.device.get_name()} Volume up: {self.device.volume}")

    def volume_down(self):
        self.device.volume -= 1
        print(f"{self.device.get_name()} Volume down: {self.device.volume}")

if __name__ == "__main__":
    radio = Radio()
    tv = TV()

    radio_remote = BasicRemote(radio)
    tv_remote = BasicRemote(tv)

    radio_remote.volume_up()
    tv_remote.volume_up()
    tv_remote.volume_down()

