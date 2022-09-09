import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 178)
engine.say("Hi, I am JARVIS how may i help you")
engine.runAndWait()