# The Interpreter Pattern is a behavioral design pattern used to define a grammar for a simple 
# language and an interpreter that uses that grammar to evaluate sentences.

# Think of it like a Scientific Calculator. When you type (5 + 2) * 3, the calculator doesn't just see a 
# string of text. It breaks it down into a tree of "Grammar Rules" (Addition, Multiplication, Numbers) and executes them in order.

# 1. When do you use it?
# You use this pattern when you have a problem that repeats often and can be expressed as a simple language. 
# Common examples include:

# SQL Parsers: Translating text into database commands.
# Regular Expressions (Regex): Matching patterns in text.
# Formatters: Like a tool that converts Markdown into HTML.

# 2. The Core Components
# Context: Contains information that is global to the interpreter (like a dictionary of variables).
# Abstract Expression: An interface for all nodes in the "Grammar Tree."
# Terminal Expression: A "leaf" node that represents a fixed value (like a number 5).
# Non-Terminal Expression: A "branch" node that represents a rule (like + or -) and points to other expressions.

from abc import ABC, abstractmethod

# 1. The Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self, context: dict) -> int:
        pass

# 2. Terminal Expression (The Numbers)
class Number(Expression):
    def __init__(self, value: int):
        self.value = value

    def interpret(self, context: dict) -> int:
        return self.value

# 3. Non-Terminal Expressions (The Rules)
class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: dict) -> int:
        return self.left.interpret(context) + self.right.interpret(context)

class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self, context: dict) -> int:
        return self.left.interpret(context) - self.right.interpret(context)

# --- Usage (Evaluating: 10 + 5 - 2) ---
# We build a tree: Subtract(Add(10, 5), 2)
sentence = Subtract(
    Add(Number(10), Number(5)), 
    Number(2)
)

result = sentence.interpret(context={})
print(f"Result: {result}")  # Output: 13