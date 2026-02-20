# Only one instance
# Single point of access to a resource

# Uses:
# 1. Logging
# 2. Configuration management
# 3. Database connection management
# 4. Thread pools
# 5. Caching
# 6. Utility Classes


# Disadvantages:
# 1. Global state: Singletons can introduce global state into an application, which can make it difficult to manage and test.
# 2. Hidden dependencies: Singletons can create hidden dependencies between classes, making it harder
#    to understand the relationships between different parts of the code.
# 3. Difficulty in testing: Singletons can make unit testing more difficult, as the singleton instance may need to be reset or mocked for each test case.
# 4. Concurrency issues: In multi-threaded applications, singletons can lead to concurrency issues if not implemented correctly, as multiple threads may try to access the singleton instance simultaneously.

import threading
import time

class Singleton:
    _instances = None

    def __new__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super().__new__(cls)
            print("Creating a new instance of Singleton")
        else:
            print("Using the existing instance of Singleton")
        return cls._instances
    
# Example usage
singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1)  # Output: <__main__.Singleton object at 0x7ccbed3e7f20>
print(singleton2)  # Output: <__main__.Singleton object at 0x7ccbed3e7f20>
print(singleton1 is singleton2)  # Output: True

print("######################################################################################")

# Inherit from `type` to convert a class into metaclass
# A metaclass is a class of a class that defines how a class behaves. A class is an instance of a metaclass.
class SingletonClass(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            time.sleep(1)  # Simulate some delay in instance creation
            self._instances[self] = instance
            print("Creating a new instance of Singleton")
        else:
            print("Using the existing instance of Singleton")

        return self._instances[self]
    
# Real world example: Logger class
class NetworkDriver(metaclass=SingletonClass):
    def __init__(self):
        self.connection = self.connect_to_network()

    def connect_to_network(self):
        return f"Connecting to the network {self}..."
    
# Example usage
# driver1 = NetworkDriver()
# driver2 = NetworkDriver()
# print(driver1.connection)  # Output: Network Connection
# print(driver2.connection)  # Output: Network Connection
# print(driver1 is driver2)  # Output: True

th1 = threading.Thread(target=lambda: print(NetworkDriver().connection))
th2 = threading.Thread(target=lambda: print(NetworkDriver().connection))
th1.start()
th2.start()
print("Starting the threads")
th1.join()
th2.join()
print("######################################################################################")

# Thread-safe Singleton implementation using a lock
class ThreadSafeSingletonClass(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(self, *args, **kwargs):
        with self._lock:
            if self not in self._instances:
                instance = super().__call__(*args, **kwargs)
                self._instances[self] = instance
                print("Creating a new instance of Singleton")
            else:
                print("Using the existing instance of Singleton")

        return self._instances[self]
    
# Real world example: Logger class
class ThreadSafeNetworkDriver(metaclass=ThreadSafeSingletonClass):
    def __init__(self):
        self.connection = self.connect_to_network()

    def connect_to_network(self):
        return f"Connecting to the network {self}..."
    

# Example usage
def create_driver():
    driver = ThreadSafeNetworkDriver()
    print(driver.connection)

thread1 = threading.Thread(target=create_driver)
thread2 = threading.Thread(target=create_driver)
thread1.start()
thread2.start()