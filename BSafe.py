#URGENT
#FILE I/O WITH TXT FILES

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

def drawStartSetup():
    screen.blit(testText, (screenWidth/2 - testTextX/2, screenHeight/32))
    screen.blit(startText, (screenWidth/2 - startText.get_width()/2, screenHeight/8))
    draw.rect(screen, BLACK, setupRect, 2)
    screen.blit(setupText, (setupRect[0] + setupRect[2]/6, setupRect[1] - setupText.get_height()/8))

def drawStart():
    screen.blit(testText, (screenWidth/2 - testTextX/2, screenHeight/32))
    screen.blit(startText, (screenWidth/2 - startText.get_width()/2, screenHeight/8))
    draw.rect(screen, BLACK, setupRect, 2)
    screen.blit(startText2, (setupRect[0] + setupRect[2]/4, setupRect[1] - startText2.get_height()/16))

def drawDisasters():
    for i in disasterRects:
        draw.rect(screen, BLACK, i, 2)
    screen.blit(disasterText, (screenWidth/2 - disasterText.get_width()/2, 0))
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))

def drawFire():
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))

def drawStorm():
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))

def drawLandslide():
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))

def drawFlood():
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))

def drawAvalanche():
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))

def drawHurricane():
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))
#-------------------------------------------------------------------
logo = image.load("images/logo.jpg")
infile = open("setup.txt")
hoes = infile.readline()
print(hoes)
infile.close()
####################################################################
screenWidth = 640
screenHeight = 640
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREY = (111,111,111)
screen = display.set_mode((screenWidth,screenHeight))#screen size (16:9 iOS ratios)
#####################################################################
screenFill(WHITE)
screen.blit(logo,(screenWidth/2 - logo.get_width()/2,screenHeight/2 - logo.get_height()/2))
display.flip()

running = True
screenPosition = "start"
time.wait(1000)
#####################################################################
font.init()
ralewayBold60 = font.Font("raleway/Raleway-Bold.ttf",60)
ralewayRegular48 = font.Font("raleway/Raleway-Regular.ttf", 48)
ralewayMedium36 = font.Font("raleway/Raleway-Medium.ttf", 36)
testText =ralewayBold60.render("B-Safe", True, BLACK)
testTextX,testTextY = ralewayBold60.size("B-Safe")
####################################################################
setupRect = Rect(screenWidth/2 - 100, screenHeight/2, 200, 50)
setupText = ralewayRegular48.render("Setup", True, BLACK)
startText = ralewayMedium36.render("The Natural Disaster Survival App", True, GREY)
startText2 = ralewayRegular48.render("Start", True, BLACK)
backRect = Rect(0,screenHeight - 100, screenWidth/4, 100)
backPic = image.load("images/back.png")
backPic = transform.scale(backPic, (int(screenWidth/4), 100))
#-------------------------------------------------------------------
disasterRects = []
xCount = 0
yCount = 0
c = 0
for i in range (3):
    disasterRects.append(Rect(screenWidth/6, screenHeight/8 + 140*i, 120, 120))
for i in range(3):
    disasterRects.append(Rect(screenWidth/2 + screenWidth/8, screenHeight/8 + 140*i, 120, 120))
disasterText = ralewayBold60.render("Disaster Type", True, BLACK)
####################################################################
if hoes == "true": #SETUP LOOP
    print("Aye")
    while running:
        leftClick = False #leftClick and rightClick are used to prevent accidental drag
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
        if screenPosition == "start":
            screenFill(WHITE)
            drawStartSetup()
            if (setupRect.collidepoint(mx,my) and (leftClick)):
                draw.rect(screen, RED, setupRect, 1)
                screenPosition = "disasters"

        if screenPosition == "disasters":
            screenFill(WHITE)
            drawDisasters()
            for i in disasterRects:
                if (i.collidepoint(mx,my) and (leftClick)):
                    if (i == disasterRects[0]):
                        screenPosition = "wildfire"
                        print("Fire")
                    elif (i == disasterRects[1]):
                        screenPosition = "severe storm"
                        print("Storm")
                    elif (i == disasterRects[2]):
                        screenPosition = "landslide"
                        print("Landslide")
                    elif (i == disasterRects[3]):
                        screenPosition = "flood"
                        print("Flood")
                    elif (i == disasterRects[4]):
                        screenPosition = "avalanche"
                        print("Avalanche")
                    elif (i == disasterRects[5]):
                        screenPosition = "hurricane"
                        print("Hurricane")
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "start"

        if screenPosition == "wildfire":
            screenFill(WHITE)
            drawFire()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
                
        if screenPosition == "severe storm":
            screenFill(WHITE)
            drawStorm()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
                
        if screenPosition == "landslide":
            screenFill(WHITE)
            drawLandslide()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
                
        if screenPosition == "flood":
            screenFill(WHITE)
            drawFlood()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
                
        if screenPosition == "avalanche":
            screenFill(WHITE)
            drawAvalanche()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
                
        if screenPosition == "hurricane":
            screenFill(WHITE)
            drawHurricane()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
        display.flip()
else:
    while running:
        leftClick = False #leftClick and rightClick are used to prevent accidental drag
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
        if screenPosition  == "start":
            screenFill(WHITE)
            screenFill(WHITE)
            drawStart()
            if (setupRect.collidepoint(mx,my) and (leftClick)):
                draw.rect(screen, RED, setupRect, 1)
                screenPosition = "disasters"
            
#outfile = open("setup.txt", "w")
#outfile.write("false")
quit() #<---the worst thing ever
