# Day-58: BirthdayMate

"""
programming language
        python version 3.7 or above

required packages 

pandas  
pandas is a powerful data manipulation and analysis library for Python. 

command to install pandas 
pip install pandas

datetime  
The datetime module in Python provides classes and functions for working with dates and times. 
No need for installation as it is a built-in module in Python.

plyer
plyer provides a unified interface for accessing features like notifications, vibration, etc.
command to install Plyer 
pip install plyer

pyttsx3
pyttsx3 allows your Python programs to speak to you by using the capabilities
of text-to-speech engines on your computer.
command to install pyttsx3 
pip install pyttsx3

For database
        You just have to create new excel file, and follow all commands
        for creating file as mentioned in video (https://www.youtube.com/watch?v=_W4_FQGZo7w)
for icon
        you can download icon of you choice from this website :- https://www.flaticon.com/search?word=birthday
        take minimum size possible for icon
"""


import pandas as pd
import datetime
from plyer import notification
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices[1].id')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def notification1(title,msg):
    notification.notify(
        title=title
        message = msg
        app_icon = "You icon path here"
        timeout = 5
    )
        
        
df = pd.read_excel("excel path here")
today = datetime.datetime.now().strftime("%d-%m")
for index,item in df.itterrows():
    bd = item["birthday"]
    if today == bd:
        a = item["name"]
        notification1("birthday Alert","It's"+a+"'s birthday today.")
        speak(f"It's {a}'s birthday today!!..")

