# The Memento Pattern is a behavioral design pattern that allows you to save and restore the 
# previous state of an object without revealing the details of its implementation.

# Think of it as the "Ctrl + Z" (Undo) feature in a text editor or a "Save Point" in a video game. 
# You don't want the game engine to have to remember every single variable yourself; you just want a "snapshot" 
# you can reload if you run into a boss that's too tough.

# 1. The Three Key Players
# To make this work safely, the pattern uses three distinct roles:
# The Originator: The object whose state we want to save (e.g., the Text Editor). It creates the snapshot.
# The Memento: A small, "black box" object that stores the state. It is immutable (cannot be changed once created).
# The Caretaker: The "History" manager. It asks the Originator for a snapshot and stores it, 
# but it never looks inside the snapshot.

# 1. The Memento (The "Snapshot")
class Memento:
    def __init__(self, state: str):
        self._state = state # Encapsulated state

    def get_state(self) -> str:
        return self._state

# 2. The Originator (The "Editor")
class Editor:
    def __init__(self):
        self._content = ""

    def type(self, text: str):
        self._content += text

    def save(self) -> Memento:
        # Creates a snapshot of the current state
        return Memento(self._content)

    def restore(self, memento: Memento):
        # Reloads state from a snapshot
        self._content = memento.get_state()

# 3. The Caretaker (The "History Manager")
class History:
    def __init__(self):
        self._backups = []

    def push(self, memento: Memento):
        self._backups.append(memento)

    def pop(self) -> Memento:
        if not self._backups:
            return None
        return self._backups.pop()

# --- Usage ---
editor = Editor()
history = History()

# Typing and saving
editor.type("Hello ")
history.push(editor.save()) # Save point 1

editor.type("World!")
history.push(editor.save()) # Save point 2

editor.type(" Wait, I don't like this part.")
print(f"Current: {editor._content}")

# Undo!
editor.restore(history.pop()) # Go back to "Hello World!"
print(f"Restored: {editor._content}")
editor.restore(history.pop()) # Go back to "Hello "

print(f"Restored: {editor._content}")