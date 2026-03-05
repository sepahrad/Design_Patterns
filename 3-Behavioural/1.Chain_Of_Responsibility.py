# The Chain of Responsibility pattern is a behavioral design pattern that allows you to pass a request along a "chain" of 
# potential handlers. Each handler in the chain has a simple choice: process the request or pass it to the next handler.

# Think of it like a Company Support Line:
# You call Level 1 Support (automated bot). If it can't fix your issue, it transfers you to...
# Level 2 Support (human technician). If they can't help, they escalate to...
# Level 3 Support (specialist engineer).

# The "Chain" stops as soon as someone successfully handles the request.
# 1. Key Components
# Handler Interface: Defines a method for building the chain (setting the "successor") and a method for handling requests.
# Concrete Handlers: The actual classes that contain the logic to handle specific requests.
# Client: The code that initiates the request to the first link in the chain.

# Chain of Responsibility vs. Middleware
# You may have heard of "Middleware" in web frameworks like Django or Flask. 
# Middleware is essentially the Chain of Responsibility pattern with a twist:
# Pure Chain of Responsibility: Only one handler usually processes the request. Once handled, it stops.
# Middleware: Every handler usually processes the request (e.g., logging -> auth -> compression) before passing it along.

from abc import ABC, abstractmethod

class HandlerChain(ABC):
    def __init__(self, input_header):
        self.next_header = input_header

    @abstractmethod
    def add_header(self, input_header: str):
        pass

    def do_next(self, input_header: str):
        if self.next_header:
            return self.next_header.add_header(input_header)
        
        return input_header
    
class AuthenticationHeader(HandlerChain):
    def __init__(self, token: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.token = token

    def add_header(self, input_header: str):
        h = f"{input_header}\nAuthorization: {self.token}"
        return self.do_next(h)
    
class ContentTypeHeader(HandlerChain):
    def __init__(self, content_type: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.content_type = content_type

    def add_header(self, input_header: str):
        h = f"{input_header}\nContentType: {self.content_type}"
        return self.do_next(h)
    
class BodyPayloadHeader(HandlerChain):
    def __init__(self, body: str, next_header: HandlerChain = None):
        super().__init__(next_header)
        self.body = body

    def add_header(self, input_header: str):
        h = f"{input_header}\n{self.body}"
        return self.do_next(h)
    
authentication_header = AuthenticationHeader("123456789")
content_type_header = ContentTypeHeader("json")
body_header = BodyPayloadHeader("Body: {\"username\" = \"John\"}")

authentication_header.next_header = content_type_header
content_type_header.next_header = body_header

message_with_authentication = authentication_header.add_header("Header with authentication")
message_without_authentication = content_type_header.add_header("Header without authentication")

print(message_with_authentication)
print("------")
print(message_without_authentication)

print("----------------------------------------------------------------")

class Handler(ABC):
    """The base interface for the chain"""
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler  # Allows chaining like h1.set_next(h2).set_next(h3)

    @abstractmethod
    def handle(self, amount):
        if self._next_handler:
            return self._next_handler.handle(amount)
        print("End of chain: No one could handle the remaining amount.")
        return None

class Dispenser100(Handler):
    def handle(self, amount):
        if amount >= 100:
            num = amount // 100
            remainder = amount % 100
            print(f"Dispensing {num} x $100 notes")
            if remainder > 0:
                return super().handle(remainder)
        else:
            return super().handle(amount)

class Dispenser20(Handler):
    def handle(self, amount):
        if amount >= 20:
            num = amount // 20
            remainder = amount % 20
            print(f"Dispensing {num} x $20 notes")
            if remainder > 0:
                return super().handle(remainder)
        else:
            return super().handle(amount)

# --- Usage ---
d100 = Dispenser100()
d20 = Dispenser20()

# Link the chain: 100 -> 20
d100.set_next(d20)

print("Requesting $240:")
d100.handle(240)