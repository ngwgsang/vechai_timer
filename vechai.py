import time
from datetime import datetime
import pygame


pygame.mixer.init()
pygame.mixer.music.load('./pop.mp3')

while True:
    now = datetime.now()
    sec = int(now.strftime("%S"))
    if (sec % 5 == 0):
        print("Giây thứ:", sec)
        if (sec == 55):
            print("Dump Dump, 5 giây nữa lụm ve chai")
            pygame.mixer.music.play()
        time.sleep(4)


        
        
        






