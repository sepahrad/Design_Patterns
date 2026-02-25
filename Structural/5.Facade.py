# The Facade Pattern is a structural design pattern that provides a simplified interface to a library, a framework, 
# or any other complex set of classes.
# Think of it like a Universal Remote Control. A home theater has a TV, a Soundbar, a DVD player, and smart lights. 
# To watch a movie, you’d usually have to turn each one on separately. A Facade is the "Watch Movie" button 
# that talks to all those complicated devices for you.

# Why use it?
# Simplifies Complexity: It hides the "messy" inner workings of a complex system from the user.
# Decoupling: If you decide to replace your "Soundbar" class with a different library later, you only have 
# to change the Facade code, not the code using the Facade.
# Ease of Use: It provides a "best-practice" entry point for common tasks.

# --- Complex Subsystem Classes ---
class VideoFile:
    def __init__(self, filename):
        self.filename = filename

class BitrateReader:
    def read(self, file: VideoFile):
        print("Reading bitrate...")

class AudioMixer:
    def fix(self, file: VideoFile, bit: BitrateReader, codec: str):
        print(f"Fixing audio on {file} with bit {bit} and codec: {codec}")

# --- The Facade ---
class VideoConverter:
    """This is the Facade. It provides one simple method to the user."""
    def convert(self, filename, format):
        file = VideoFile(filename)
        bit_reader = BitrateReader()
        bit_reader = bit_reader.read(file)
        mixer = AudioMixer()
        
        print(f"Facade is coordinating the conversion of {filename} to {format}...")
        mixer.fix(file, bit_reader, "codec_data")
        
        print("File converted successfully!")

# --- The Client (You) ---
# Without the facade, you'd have to initialize 3 classes yourself.
# With the facade, it's just one line:
converter = VideoConverter()
converter.convert("funny_cat.mp4", "avi")