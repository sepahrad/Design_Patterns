# The Builder Design Pattern is a creational pattern used to construct complex objects step-by-step. 
# While the Factory pattern creates an object in one single shot, the Builder allows you to "compose" the object by calling specific methods in a specific order
# In some languages (like Java), the Builder is used to avoid "telescoping constructors" (constructors with 10+ arguments). 
# In Python, we have named arguments, so we use the Builder primarily when:
# The creation process involves many steps.
# The object should only be "finished" after certain configurations are met.
# You want to create different representations of the same object using the same construction process.

class NetworkService:
    def __init__(self):
        self.components = {}

    def add(self, key: str, value: str):
        self.components[key] = value
    
    def show(self):
        print(self.components)

class NetworkServiceBuilder:
    def __init__(self):
        self._service = NetworkService()

    def add_target_url(self, url: str):
        self._service.add("URL", url)
    
    def add_auth(self, auth: str):
        self._service.add("Authorization", auth)

    def add_caching(self, cache: int):
        self._service.add("Cache-Control", cache)
    
    def build(self) -> NetworkService:
        service = self._service
        self._service = NetworkService()

        return service
    
builder = NetworkServiceBuilder()
builder.add_target_url("google.com")

service1 = builder.build()
service1.show()

builder.add_target_url("yahoo.com")
builder.add_auth("abc123")
builder.add_caching(60000)

service2 = builder.build()
service2.show()

class NetworkServicePython:
    def __init__(self, url: str = "", auth: str = "", cache: int = 0):
        self.components = {}

        if url:
            self.components["URL"] = url
        
        if auth:
            self.components["Authorization"] = auth

        if cache:
            self.components["Cache-Control"] = cache

    def show(self):
        print(self.components)
    
service1 = NetworkServicePython("Youtube.com", "abc123", "12000")
service1.show()

service2 = NetworkServicePython("MSN.com")
service2.show()


    