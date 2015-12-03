import pygame
import random

def bark():
    rand = int(random.random() * 8 + 1)
    filename = "sounds/bark" + str(rand) + ".mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy() == True) :
        continue
