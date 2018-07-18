#*********URGENT**********
#-------------------------
#FILE I/O WITH TXT FILES |
#POSSIBLE UI TYPING???   |
#SEARCH FUNCTIONS        |
#SETTINGS MENU           |
#ALERT MENU              |
#-------------------------
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
####################################################################
#SCREEN STUFF AND CONSTANTS
screenWidth = 640
screenHeight = 640
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREY = (111,111,111)
screen = display.set_mode((screenWidth,screenHeight))#screen size (16:9 iOS ratios)
#######################################################################
#ALL FUNCTIONS 
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
    draw.rect(screen,BLACK, finishRect, 2)
    screen.blit(finishText, (finishRect[0] + finishRect[2]/2 - finishText.get_width()/2, finishRect[1]))  
    screen.blit(finishText2, (finishRect[0] + finishRect[2]/2 - finishText2.get_width()/2, finishRect[1]+finishRect[3]/2))
    screen.blit(wildfire, (disasterRects[0][0] + 2, disasterRects[0][1] + 2))
    screen.blit(storm, (disasterRects[1][0] + 2 , disasterRects[1][1] + 2))
    screen.blit(earthquake, (disasterRects[2][0] + 2 , disasterRects[2][1] + 2))
    screen.blit(flood, (disasterRects[3][0] + 2 , disasterRects[3][1] + 2))
    screen.blit(avalanche, (disasterRects[4][0] + 2 , disasterRects[4][1] + 2))
    screen.blit(hurricane, (disasterRects[5][0] + 2 , disasterRects[5][1] + 2))

def drawFire():
    screen.blit(wildfireText, (screenWidth/2 - wildfireText.get_width()/2, 0))
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))
    count  = 0
    for data in wildfireData:
        temp = ralewayRegular24.render(str(count + 1) + ". " + data, True, BLACK)
        screen.blit(temp, (0,200 + count*25))
        count += 1
    

def drawStorm():
    screen.blit(stormText, (screenWidth/2 - stormText.get_width()/2, 0))
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))
    count  = 0
    for data in stormData:
        temp = ralewayRegular24.render(str(count + 1) + ". " + data, True, BLACK)
        screen.blit(temp, (0,200 + count*25))
        count += 1
        

def drawearthquake():
    screen.blit(earthquakeText, (screenWidth/2 - earthquakeText.get_width()/2, 0))
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))
    count  = 0
    for data in earthquakeData:
        temp = ralewayRegular24.render(str(count + 1) + ". " + data, True, BLACK)
        screen.blit(temp, (0,200 + count*25))
        count += 1

def drawFlood():
    screen.blit(floodText, (screenWidth/2 - floodText.get_width()/2, 0))
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))
    count  = 0
    for data in floodData:
        temp = ralewayRegular24.render(str(count + 1) + ". " + data, True, BLACK)
        screen.blit(temp, (0,200 + count*25))
        count += 1

def drawAvalanche():
    screen.blit(avalancheText, (screenWidth/2 - avalancheText.get_width()/2, 0))
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))
    count  = 0
    for data in avalancheData:
        temp = ralewayRegular24.render(str(count + 1) + ". " + data, True, BLACK)
        screen.blit(temp, (0,200 + count*25))
        count += 1

def drawHurricane():
    screen.blit(hurricaneText, (screenWidth/2 - hurricaneText.get_width()/2, 0))
    draw.rect(screen, BLACK, backRect, 2)
    screen.blit(backPic, (backRect[0], backRect[1]))
    count  = 0
    for data in hurricaneData:
        temp = ralewayRegular24.render(str(count + 1) + ". " + data, True, BLACK)
        screen.blit(temp, (0,200 + count*25))
        count += 1
#-------------------------------------------------------------------

####################################################################
#DATA HANDLING I/O
wildfireFile = open("data/wildfire.txt")
wildfireData = wildfireFile.readlines()
wildfireData.append("ADD NEW")
wildfireFile.close()
stormFile = open("data/storm.txt")
stormData = stormFile.readlines()
stormData.append("ADD NEW")
stormFile.close()
earthquakeFile = open("data/earthquake.txt")
earthquakeData = earthquakeFile.readlines()
earthquakeData.append("ADD NEW")
earthquakeFile.close()
floodFile = open("data/flood.txt")
floodData = floodFile.readlines()
floodData.append("ADD NEW")
floodFile.close()
avalancheFile = open("data/avalanche.txt")
avalancheData = avalancheFile.readlines()
avalancheData.append("ADD NEW")
avalancheFile.close()
hurricaneFile = open("data/hurricane.txt")
hurricaneData = hurricaneFile.readlines()
hurricaneData.append("ADD NEW")
hurricaneFile.close()


#-------------------------------------------------------------------
#ORGANIZING DATA RECTS
wildfireRects = []
stormRects = []
earthquakeRects = []
floodRects = []
avalancheRects = []
hurricaneRects= []
count = 0
for data in wildfireData:
    wildfireRects.append(Rect(0, 200 + count*25, screenWidth, 25))
    count += 1
count = 0
for data in stormData:
    stormRects.append(Rect(0, 200 + count*25, screenWidth, 25))
    count += 1
count = 0
for data in earthquakeData:
    earthquakeRects.append(Rect(0, 200 + count*25, screenWidth, 25))
    count += 1
count = 0
for data in floodData:
    floodRects.append(Rect(0, 200 + count*25, screenWidth, 25))
    count += 1
count = 0
for data in avalancheData:
    avalancheRects.append(Rect(0, 200 + count*25, screenWidth, 25))
    count += 1
count = 0
for data in hurricaneData:
    hurricaneRects.append(Rect(0, 200 + count*25, screenWidth, 25))
    count += 1
#####################################################################
#LAUCH SEQUENCE ITEMS
logo = image.load("images/logo.jpg")
infile = open("setup.txt")
hoes = infile.readline()
print(hoes) #Checks which launch sequence to go through
infile.close()

screenFill(WHITE)
screen.blit(logo,(screenWidth/2 - logo.get_width()/2,screenHeight/2 - logo.get_height()/2))
display.flip()

running = True
screenPosition = "start"
time.wait(1000)
#####################################################################
#FONTS
font.init()
ralewayBold60 = font.Font("raleway/Raleway-Bold.ttf",60)
ralewayRegular48 = font.Font("raleway/Raleway-Regular.ttf", 48)
ralewayMedium36 = font.Font("raleway/Raleway-Medium.ttf", 36)
ralewayRegular24 = font.Font("raleway/Raleway-Regular.ttf", 24)
testText =ralewayBold60.render("B-Safe", True, BLACK)
testTextX,testTextY = ralewayBold60.size("B-Safe")
####################################################################
#MENU RESOURCES AND RECTANGLES
setupRect = Rect(screenWidth/2 - 100, screenHeight/2, 200, 50)
setupText = ralewayRegular48.render("Setup", True, BLACK)
startText = ralewayMedium36.render("The Natural Disaster Survival App", True, GREY)
startText2 = ralewayRegular48.render("Start", True, BLACK)
backRect = Rect(0,screenHeight - 100, screenWidth/4, 100)
backPic = image.load("images/back.png")
backPic = transform.scale(backPic, (int(screenWidth/4), 100))
finishText = ralewayMedium36.render("End", True, BLACK)
finishText2 = ralewayMedium36.render("Setup", True, BLACK)
finishRect = Rect(screenWidth - screenWidth/4, screenHeight - 100, int(screenWidth/4), 100)
###################################################################
#MENU ICONS AND TEXT
flood = image.load("images/flood.png")
flood = transform.scale(flood, (118,118))
floodText = ralewayBold60.render("Flood", True, BLACK)
avalanche = image.load("images/avalanche.png")
avalanche = transform.scale(avalanche, (118,118))
avalancheText = ralewayBold60.render("Avalanche", True, BLACK)
wildfire = image.load("images/wildfire.png")
wildfire = transform.scale(wildfire, (118,118))
wildfireText = ralewayBold60.render("Wildfire", True, BLACK)
earthquake = image.load("images/landslide.jpg")
earthquake = transform.scale(earthquake, (118,118))
earthquakeText = ralewayBold60.render("Earthquake", True, BLACK)
hurricane = image.load("images/hurricane.png")
hurricane = transform.scale(hurricane, (118,118))
hurricaneText = ralewayBold60.render("Hurricane", True, BLACK)
storm = image.load("images/storm.png")
storm = transform.scale(storm, (118,118))
stormText = ralewayBold60.render("Severe Storm", True, BLACK)
#-------------------------------------------------------------------
#ORGANIZING THE MENU LAYOUT
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
#SETUP LOOP
if hoes == "true": 
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
                        screenPosition = "earthquake"
                        print("earthquake")
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
            if (finishRect.collidepoint(mx,my) and leftClick):
                hoes = "false"

        if screenPosition == "wildfire":
            screenFill(WHITE)
            drawFire()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
            if (wildfireRects[-1].collidepoint(mx,my) and leftClick):
                print("Click")
                
        if screenPosition == "severe storm":
            screenFill(WHITE)
            drawStorm()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
            if (stormRects[-1].collidepoint(mx,my) and leftClick):
                print("Click")
                
        if screenPosition == "earthquake":
            screenFill(WHITE)
            drawearthquake()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
            if (earthquakeRects[-1].collidepoint(mx,my) and leftClick):
                print("Click")
                
        if screenPosition == "flood":
            screenFill(WHITE)
            drawFlood()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
            if (floodRects[-1].collidepoint(mx,my) and leftClick):
                print("Click")
                
        if screenPosition == "avalanche":
            screenFill(WHITE)
            drawAvalanche()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
            if (avalancheRects[-1].collidepoint(mx,my) and leftClick):
                print("Click")
                
        if screenPosition == "hurricane":
            screenFill(WHITE)
            drawHurricane()
            if (backRect.collidepoint(mx,my) and leftClick):
                screenPosition = "disasters"
            if (hurricaneRects[-1].collidepoint(mx,my) and leftClick):
                print("Click")
        display.flip()
#########################################################################
#USAGE LOOP
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
