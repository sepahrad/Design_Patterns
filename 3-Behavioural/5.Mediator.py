# The Mediator Pattern is a behavioral design pattern that reduces chaotic dependencies between objects. 
# It restricts direct communication between objects and forces them to collaborate only via a mediator object.

# Think of an Airport Control Tower:
# The Pilots (the objects) don't talk directly to each other to decide who lands first. 
# If they did, with 50 planes in the sky, it would be total radio chaos.

# Instead, every Pilot talks only to the Control Tower (the Mediator). The Tower coordinates the timing and safety, 
# then tells each Pilot what to do.

# 1. The Problem: The "Spaghetti" Mess
# Without a mediator, every class needs to know about every other class to stay in sync. 
# This creates Tight Coupling. If you change how one class works, five others might break.

# 2. The Solution: The Hub
# The Mediator acts as a "Router." When something happens in Object A, it doesn't tell Object B. 
# It just tells the Mediator: "Hey, I just clicked this button." The Mediator then decides: "Okay, if that button was clicked, 
# I need to disable Object B and refresh Object C."

from abc import ABC, abstractmethod

# 1. The Mediator Interface
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: object, event: str):
        pass

# 2. The Components (Objects that need to stay in sync)
class Component:
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

class Checkbox(Component):
    def check(self):
        print("UI: 'Away Mode' checked.")
        self._mediator.notify(self, "away_on")

class Thermostat(Component):
    def set_temp(self, temp):
        print(f"Thermostat: Setting temperature to {temp}°C.")

class SmartLight(Component):
    def turn_off(self):
        print("Lights: Powering down.")

# 3. The Concrete Mediator (The "Brain")
class HomeMediator(Mediator):
    def __init__(self, checkbox, thermo, light):
        self.checkbox = checkbox
        self.checkbox._mediator = self
        self.thermo = thermo
        self.light = light

    def notify(self, sender, event):
        if event == "away_on":
            # The mediator coordinates the multiple actions
            self.thermo.set_temp(16)
            self.light.turn_off()

# --- Usage ---
cb = Checkbox()
th = Thermostat()
li = SmartLight()

# Connect them all via the mediator
mediator = HomeMediator(cb, th, li)

# The user only interacts with the checkbox
cb.check() 
# Result: Both the Thermostat and Light react without knowing about the Checkbox!