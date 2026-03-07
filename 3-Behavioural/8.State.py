# The State Pattern is a behavioral design pattern that allows an object to change its behavior when its internal state changes. 
# The object will appear to change its class.

# Think of a Vending Machine:
# If you press the "Dispense" button when it has No Money, it does nothing.
# If you press it when it has Money, it gives you a soda.
# If you press it when it is Out of Stock, it gives you an error.
# The "Machine" is the same object, but its "State" determines how it reacts to the same button press.

# The "Bad" Way
def press_button(self):
    if self.state == "NO_MONEY":
        print("Please insert coin")
    elif self.state == "HAS_MONEY":
        print("Dispensing...")
    elif self.state == "OUT_OF_STOCK":
        print("Error: Empty")

# "----------------------------------------------------------------------------"

from abc import ABC, abstractmethod

# 1. The State Interface
class State(ABC):
    @abstractmethod
    def publish(self):
        pass

# 2. Concrete States
class DraftState(State):
    def publish(self):
        print("Moving from Draft to Moderation...")
        return ModerationState()

class ModerationState(State):
    def publish(self):
        print("Reviewing... Moving to Published.")
        return PublishedState()

class PublishedState(State):
    def publish(self):
        print("Already published! Doing nothing.")
        return self

# 3. The Context (The Document)
class Document:
    def __init__(self):
        # Start in the Draft state
        self.state = DraftState()

    def publish_request(self):
        # Delegate the behavior to the state object
        self.state = self.state.publish()

# --- Usage ---
doc = Document()

doc.publish_request() # Output: Moving from Draft to Moderation...
doc.publish_request() # Output: Reviewing... Moving to Published.
doc.publish_request() # Output: Already published! Doing nothing.