# Day-57: HydrateHero

"""
pyttsx3 is a text-to-speech conversion library in Python. 
It allows your Python programs to speak to you by using the capabilities of 
text-to-speech engines on your computer.

command to install pyttsx3
pip install pyttsx3

Plyer is a Python library for accessing features commonly found in various 
platforms like desktops, mobile devices, etc. 
It provides a unified interface for accessing features like notifications, 
vibration, etc.

command to install Plyer
pip install plyer
"""

import pyttsx3 
from plyer import notification

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 

def speak(audio):
  engine.say (audio)
  engine.runAndWait ()
  
notification.notify(
    title="Please drink water",
    message =
    "you have not drink water since half hour. so kindly drink it",
    app_icon = "C:\\Users\\Admin\\Desktop\\water Notification\\water.ico",
    timeout = 5
)
speak ("!Aditya ! please drink water and stay hydrated")
