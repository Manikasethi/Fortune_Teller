from random import choice
import pyttsx3

#initializing tts engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if "english" in voice.name.lower() and "british" in voice.name.lower():
        engine.setProperty('voice', voice.id)  # Select British English voice
        break

engine.setProperty('rate', 150)  # Set speaking rate (slower for intellectual tone)
engine.setProperty('volume', 1.0)  # Set volume level

fortunes= [ "The harder you work, the luckier you get.",
            "Love is just around the corner—if you dare to look.",
            "Your heart will lead you to your greatest treasure.",
            "Someone is thinking of you fondly right now.",
            "You are braver than you believe and stronger than you seem",
            "Your smile will be your greatest charm today.",
            "Success is a journey, not a destination. Enjoy the ride."]

# Function to read fortune
def speak_fortune():
    fortune = choice(fortunes)
    print(f"Fortune: {fortune}")
    engine.say(f"Here is your fortune: {fortune}")
    engine.runAndWait()

# Run the assistant
speak_fortune()