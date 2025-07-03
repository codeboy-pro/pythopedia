import pyttsx3

engine = pyttsx3.init()

# Set volume to maximum
engine.setProperty('volume', 1.0)

# Print available voices
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name} - {voice.id}")

# Set a voice (optional)
engine.setProperty('voice', voices[0].id)  # You can try voices[1] if available

# Speak the text
engine.say("Hi, I am Pradip Maity. How are you?")
engine.runAndWait()
