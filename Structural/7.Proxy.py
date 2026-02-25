# The Proxy Pattern is a structural design pattern that lets you provide a substitute or placeholder for another object. 
# A proxy controls access to the original object, allowing you to perform something either before or after the request 
# reaches the original object.
# Think of it like a Credit Card. The credit card is a proxy for the cash in your bank account. It represents the "real" money 
# and can be used for the same transactions, but it adds a layer of security (pin codes) and convenience.

# Why use it?
# Lazy Initialization (Virtual Proxy): Don't create a "heavy" object (like a massive database connection) until 
# someone actually needs to use it.
# Access Control (Protection Proxy): Check if a user has the right permissions before letting them call a sensitive method.
# Logging/Caching: Automatically log every time a service is called without changing the service's code.

# Similar to facade, except the proxy has the same interface
# Similar to decorator, except the proxy manages the lifecycle of its object

from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        print(f"Real Image: loading {filename}")

    def display(self):
        print(f"Displaying Real Image: {self.filename}", end="\n\n")
    
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        print(f"Displaying Proxy Image: {self.filename}")
        
        if not self.real_image:
            print("From Disk")
            self.real_image =  RealImage(self.filename)
        else:
            print("From cache")
        
        self.real_image.display()

if __name__ == "__main__":
    image = ProxyImage("test.png")

    image.display()
    image.display()