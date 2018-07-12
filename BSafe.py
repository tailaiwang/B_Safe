#B Safe
#B House Design
#Engineering Team
#Nader St. Amant (President)
#Tailai Wang (VP and Software Lead)
#Alex Bae (Software and Design Engineering)
#Sarah Foster (Sofrtware and Design Engineering)
from pygame import* #all pygame files require this 
from pygame.locals import* #Positions and "tings"
from random import* #shuffle and randint and such things
from math import* #funnily enough i dont think i used this...?
import tkinter as tk #TKINTER stuff for dialog boxes
from tkinter import filedialog
import pygame 
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16,2,2048) #sound 
 

root = tk.Tk() #tkinter
root.withdraw()

#-------------------------------------------------------------------
def screenFill(c): #Where c is a color
    draw.rect(screen,(c), (0,0,screenWidth,screenHeight))
#-------------------------------------------------------------------
logo = image.load("images/logo.jpg")
####################################################################
screenWidth = 640
screenHeight = 1136
BLACK = (0,0,0)
WHITE = (255,255,255)
screen = display.set_mode((screenWidth,screenHeight))#screen size (16:9 iOS ratios)
#####################################################################
screenFill(WHITE)
screen.blit(logo,(screenWidth/2 - logo.get_width()/2,screenHeight/4))
display.flip()

running = True
screenPosition = "menu"
time.wait(1000)
#####################################################################
font.init()
#####################################################################
while running:
    leftClick = False #leftClick and rightClick are used to prevent accidental drag
    rightClick = False
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        if evt.type == KEYDOWN:
            if evt.key == K_ESCAPE:
                running = False #shuts program on ESC
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                leftClick = True
#---------------------------------------------------------------------
    mx,my = mouse.get_pos() #Mouse position
#---------------------------------------------------------------------
    if screenPosition == "menu":
        screenFill(BLACK)
        screen.blit(logo,(screenWidth/2 - logo.get_width()/2,screenHeight/4))
    display.flip()       
quit() #<---the worst thing ever
