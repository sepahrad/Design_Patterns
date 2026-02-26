# The Adapter Design Pattern is a structural pattern that allows objects with incompatible interfaces to work together. 
# It acts as a "translator" or a "bridge" between two pieces of code that weren't originally designed to talk to each other.
# Think of it like a physical power adapter: If you have a US plug (the Client) and a European wall socket (the Service), 
# you don't rewire your laptop or the building. You just plug in an adapter between them.

# You use an Adapter when:
# You want to use an existing class, but its interface doesn't match the one you need.
# You are using a third-party library or a legacy system that you cannot modify.
# You need to standardize several different classes under one common interface.

# The Components
# Target: The interface the Client expects (e.g., your modern application code).
# Client: The code that wants to use the service.
# Adaptee: The "clunky" or "incompatible" class that needs adapting.
# Adapter: The middle-man class that maps the Target's interface to the Adaptee's logic.

# ----------------------------------------------------------------------------------------------------------- #
# In Python, a dataclass is a decorator (introduced in Python 3.7) that automatically generates 
# the "boilerplate" code for a class that primarily exists to store data.
from dataclasses import dataclass

# 3rd party code
@dataclass
class DisplayDataType:
    index: float
    data: str

# for_test = DisplayDataType(1.2, "Hey")
# print(for_test)
# ----------------------------------------------------------------------------------------------------------- #

import xml.etree.ElementTree as ET
import json

# --- The "Target" Interface ---
# This is what the modern part of your app expects to interact with
class DataProvider:
    def get_data(self) -> dict:
        pass

# --- The "Adaptee" (Legacy System) ---
class LegacyWeatherService:
    def fetch_xml_weather(self):
        # In reality, this would be an API call
        return """
        <weather>
            <city>London</city>
            <temperature>15</temperature>
            <condition>Cloudy</condition>
        </weather>
        """

# --- The "Adapter" ---
class WeatherAdapter(DataProvider):
    def __init__(self, legacy_service: LegacyWeatherService):
        self.legacy_service = legacy_service

    def get_data(self) -> dict:
        # 1. Get the incompatible data
        raw_xml = self.legacy_service.fetch_xml_weather()
        
        # 2. Perform real conversion logic
        root = ET.fromstring(raw_xml)
        
        # 3. Translate XML nodes into a Python Dictionary (the Target format)
        adapted_data = {
            "location": root.find('city').text,
            "temp_celsius": int(root.find('temperature').text),
            "summary": root.find('condition').text
        }
        
        return adapted_data

# --- The Client (Your Modern App) ---
def render_dashboard(provider: DataProvider):
    data = provider.get_data()
    print("--- Dashboard Update ---")
    print(f"Location: {data['location']}")
    print(f"Weather: {data['summary']} at {data['temp_celsius']}°C")

# --- Execution ---
legacy_api = LegacyWeatherService()
adapter = WeatherAdapter(legacy_api)

# The dashboard thinks it's talking to a standard DataProvider
render_dashboard(adapter)


