from operator import index
import pygame
from time import sleep

print("DISCLAMER :")
print("THIS TOOL FOR EDUCATION PORPOUS")
#This is main function
pygame.init()
window = pygame.display.set_mode ((0,0) ,pygame.FULLSCREEN)
sleep(100)
#WHILE LOOP
i = 1
while True:
    print(i)
    i = i +1 
    feedback =  input(" IF YOU ARE STILE  ALIVE THEN SHARE YOUR  EXPERIENCE  (good,bad:")
    if feedback == "good" :
        print("THANK YOU")
    elif feedback == "bad" :
        print("THANKS FOR YOUR SHARING EXPERIENCE")
    else:
         print("YOU ARE STILE ALIVE ")
         

   





