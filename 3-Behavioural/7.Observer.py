# The Observer Pattern is a behavioral design pattern that defines a one-to-many dependency between objects. 
# When one object (the Subject) changes its state, all its dependents (Observers) are notified and updated automatically.

# Think of it like a YouTube Channel Subscription:
# The Channel is the Subject.
# The Subscribers are the Observers.
# You don't check the channel every hour to see if there is a new video (that would be inefficient "polling"). 
# Instead, the channel "pushes" a notification to you the moment a video drops.

# 1. The Core Concept
# The pattern relies on two main components:
# The Subject (Publisher): Keeps a list of observers and provides methods to attach, detach, and notify them.
# The Observers (Subscribers): Follow a specific interface (usually an update method) so the Subject knows how to talk to them.

from abc import ABC, abstractmethod

class EventListener(ABC):
    @abstractmethod
    def update(self, event_type: str, file):
        pass

class EventManager:
    def __init__(self, operations):
        self.operations = operations
        self.listener = {}

        for op in operations:
            self.listener[op] = []

    def subscribe(self, event_type: str, listener: EventListener):
        users = self.listener[event_type]
        users.append(listener)

    def unsubscribe(self, event_type: str, listener: EventListener):
        users = self.listener[event_type]
        users.remove(listener)

    def notify(self, event_type, file):
        users = self.listener[event_type]
        [u.update(event_type, file) for u in users]

class Editor:
    events = EventManager(["open", "save"])
    file = None

    def open_file(self, file):
        self.file = file
        print(f"Editor: opening file {file}")
        self.events.notify("open", file)

    def save_file(self):
        print(f"Editor: saving file {self.file}")
        self.events.notify("save", self.file)

class EmailNotificationListener(EventListener):
    def __init__(self, email):
        self.email = email

    def update(self, event_type:str, file):
        print(f"Email to {self.email}: Someone has performed {event_type} operation on the file {file}")

class LogOpenListener(EventListener):
    def __init__(self, log_file):
        self.log_file = log_file

    def update(self, event_type, file):
        print(f"Save to log {self.log_file}: Someone has performed {event_type} operations on the file {file}")


editor = Editor()

email_listener = EmailNotificationListener("test@gmail.com")
log_listener = LogOpenListener("path/to/log/file.txt")

editor.events.subscribe("open", log_listener)
editor.events.subscribe("save", log_listener)
editor.events.subscribe("save", email_listener)

editor.open_file("test.txt")
editor.save_file()
        
print("-----------------------------------------------------------------------------------------------")

# 1. The Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, news: str):
        pass

# 2. The Subject (The News Agency)
class NewsAgency:
    def __init__(self):
        self._subscribers = [] # List of observers
        self._latest_news = None

    def attach(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)

    def detach(self, subscriber: Subscriber):
        self._subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self._latest_news)

    def add_news(self, news: str):
        self._latest_news = news
        print(f"Agency: Breaking News - {news}")
        self.notify()

# 3. Specific Observers (The Outlets)
class EmailAlert(Subscriber):
    def update(self, news: str):
        print(f"Email sent: {news}")

class SMSAlert(Subscriber):
    def update(self, news: str):
        print(f"SMS sent: {news}")

# --- Usage ---
agency = NewsAgency()

email_sub = EmailAlert()
sms_sub = SMSAlert()

agency.attach(email_sub)
agency.attach(sms_sub)

# When news is added, everyone is notified automatically
agency.add_news("Python 3.14 Released!")
agency.add_news("Golang new version Released!")
