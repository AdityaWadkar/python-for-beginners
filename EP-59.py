# Day-59: NightmareRealm

"""
pygame
Pygame is a set of Python modules designed for writing video games
command to install pygame
pip install pygame

Pyautogui
PyAutoGUI is a Python library for automating mouse and keyboard actions.
command to install pyautogui:
pip install PyAutoGUI
"""


import pygame 
from time import sleep 
import pyautogui
time=0
while time<=50:

    pyautogui.press("volumeup")
    time+=1

    pygame.init()
    window = pygame.display.set_mode ((0,0), pygame.FULLSCREEN)
    pygame.mixer.init()
    pygame.mixer.music.load(r'database/background.mp3')
    pygame.mixer.music.play()
    sleep (6)

    pygame.mixer.music.load(r'database/game_over.mp3')
    pygame.mixer.music.play()
    sleep (3)

    image = pygame.image.Load(r'database/main_screen.jpg')
    window.blit(image, (0,0))

    pygame.display.update()
    pygame.mixer.music.load(r'database/intro_sound.mp3')
    pygame.mixer.music.play(-1)
    sleep (2)

    image = pygame.image.load(r'database/welcome.jpg')
    window.blit(image, (0,0))
    pygame.display.update()
    sleep (2)

    pygame.quit()
