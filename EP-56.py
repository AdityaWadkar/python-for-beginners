# Day-56: AutoHeartbeat (Project 1)

"""
PyAutoGUI lets your Python scripts control the mouse and keyboard
to automate interactions with other applications.

command to install pyautogui
pip install PyAutoGUI
"""

import pyautogui as p
import time
time.sleep(4)
for i in range(10):
        p.typewrite("I Love you")
        p.press("enter")
