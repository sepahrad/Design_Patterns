# The Command Pattern is a behavioral design pattern that turns a request into a stand-alone object.
# Think of a Waiter in a restaurant:
# You (the Client) give an order to the Waiter (the Invoker).
# The Waiter writes the order on a Check (the Command).
# The Waiter puts the check on the kitchen counter.
# The Chef (the Receiver) reads the check and cooks the meal.
# The Waiter doesn't need to know how to cook; they just need to know how to pass the "Command object" to the person who does.

# Why use it?
# Decoupling: The object triggering the command doesn't need to know anything about the object executing it.
# *** In software engineering, decoupling is the process of separating two or more parts of a system so they can 
# function, change, and be tested independently. ***

# Undo/Redo: Since the command is an object, you can store it in a list (history) and reverse it.
# Queueing: You can schedule commands to happen later (like a task queue).

from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, command_id: int):
        self.command_id = command_id

    @abstractmethod
    def execute(self):
        pass

class OrderAndCommand(Command):
    def execute(self):
        print(f"Adding order with ID: {self.command_id}")

    
class OrderPayCommand(Command):
    def execute(self):
        print(f"Paying for order with id {self.command_id}")
    

class CommandProcessor:
    queue = []

    def add_to_queue(self, command: Command):
        self.queue.append(command)

    def process_commands(self):
        [item.execute() for item in self.queue]
        self.queue = []
    
processor = CommandProcessor()
processor.add_to_queue(OrderAndCommand(1))
processor.add_to_queue(OrderAndCommand(2))
processor.add_to_queue(OrderAndCommand(1))
processor.add_to_queue(OrderAndCommand(2))

processor.add_to_queue(OrderPayCommand(1))
processor.add_to_queue(OrderPayCommand(2))
processor.add_to_queue(OrderPayCommand(1))
processor.add_to_queue(OrderPayCommand(2))

processor.process_commands()