# The Iterator Pattern is a behavioral design pattern that lets you traverse elements of a 
# complex collection (like a list, tree, or graph) without exposing the underlying structure.

# Think of it as a Remote Control for a playlist: You have a Next button. You don't need to know 
# if the songs are stored in an array, a linked list, or a database. You just know that pressing Next gives you the next track.

# 1. Why use it?
# Uniformity: You can write a loop that works on a List, a Tree, or a Stack without changing your code.
# Encapsulation: The collection's internal data storage remains hidden.
# Multiple Traversals: You can have multiple iterators running on the same collection at the same time (e.g., two people scanning the same list).

# 2. The Core Components
# Iterator Interface: Defines methods like __next__ and __iter__.
# Concrete Iterator: Implements the actual traversal logic (keeping track of the current position).
# Collection (Aggregate): The container (like a custom List) that creates the iterator.


# The power comes when the structure is not a simple list. Imagine you have a Binary Tree. To iterate through it, 
# you need to navigate branches (Left, Root, Right). The user of your Tree doesn't want to know about the Tree's nodes; 
# they just want to write for node in my_tree:. The Iterator pattern hides that complex "tree-walking" logic inside the __next__ method.

# Why Python chose the Exception (StopIteration)
# You might think has_next() is "cleaner," but Python's way is actually more powerful for three reasons:
# Atomicity (Thread Safety): In a multi-threaded program, has_next() might return True, but by the time you call next(), 
# another thread might have stolen the last item. By just calling next(), the operation is "all or nothing."
# Performance on Infinite Streams: If you are reading data from a network or a sensor, you often don't know if there is 
# more data until you actually try to read it. has_next() would force the computer to wait for data twice (once to check, once to get).

# Simplicity for the Caller: Most people use for x in collection:. If we used has_next(), every single for loop in 
# Python would be slightly slower because it would have to make two function calls per item instead of one.
    
class Alphabet:
    """A custom collection that stores letters."""
    def __init__(self):
        self._letters = ["A", "B", "C", "D"]

    def __iter__(self):
        # This returns the Iterator object
        return AlphabetIterator(self._letters)

class AlphabetIterator:
    """The logic to traverse the collection."""
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __next__(self):
        if self._index < len(self._data):
            value = self._data[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration

# --- Usage ---
collection = Alphabet()
for letter in collection:
    print(letter) # Automatically calls __iter__ and __next__

# Or
my_alphabet = Alphabet()
iterator = iter(my_alphabet)

while True:
    try:
        letter = next(iterator)
        print(f"Got letter: {letter}")
    except StopIteration:
        print("Reached the end of the chain.")
        break