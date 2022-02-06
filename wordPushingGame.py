from tkinter import *
from tkinter.messagebox import *
import copy, string, time, sys
import pygame
from PIL import Image, ImageTk

images = []  # to hold the newly created image
def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        cv.create_image(x1, y1, image=images[-1], anchor='nw')
    cv.create_rectangle(x1, y1, x2, y2, **kwargs)

root = Tk()
root.title("WordPushingGame - Space to Restart")

pygame.init()
#Load music
bgm = "music/Equinoxe.mp3"
moveBox = "music/moveBox.mp3"
walk = "music/walk.mp3"
melting = "music/melting.mp3"
pygame.mixer.init()
pygame.mixer.music.load(bgm)
pygame.mixer.Channel(0).play(pygame.mixer.Sound(bgm))

letters=list(string.ascii_uppercase)
walls=['W2','A2','L2','S2','N2','D2']
ice=['I3','C3','E3']

allLetters=dict()
for i in letters:
    allLetters[i]=PhotoImage(file=f"image/UpperLetterImages-White/{i}.png")

for i in walls:
    allLetters[i]=PhotoImage(file=f"image/specialBlocks/{i}.png")

for i in ice:
    allLetters[i]=PhotoImage(file=f"image/specialBlocks/{i}.png")

allLetters['0']=PhotoImage(file="image/Black.png")
allLetters['I4']=PhotoImage(file="image/specialBlocks/I4.png")

i4s = [PhotoImage(file=("image/specialBlocks/I4.gif"),format = 'gif -index %i' % (i)) for i in range(2)]

# Original Map
mapList1 = [
    ['0', 'W2', 'A2', 'L2', 'L2', 'S2', '0'], 
    ['W2', '0', '0', '0', '0', '0', 'W2'], 
    ['A2', '0', 'M', '0', 'L', '0', 'A2'], 
    ['L2', '0', 'Y', '0', 'I', '0', 'L2'], 
    ['L2', '0', '0', '0', 'K', '0', 'L2'], 
    ['S2', '0', 'H', '0', 'E', '0', 'S2'], 
    ['A2', '0', 'E', '0', '0', '0', 'I3'], 
    ['N2', '0', 'A', '0', 'F', '0', 'C3'], 
    ['D2', '0', 'R', '0', 'R', '0', 'E3'], 
    ['W2', '0', 'T', '0', 'O', '0', 'W2'], 
    ['A2', '0', '0', '0', 'Z', '0', 'A2'], 
    ['L2', '0', 'I4', '0', 'E', '0', 'L2'], 
    ['L2', '0', 'S', '0', 'N', '0', 'L2'], 
    ['S2', '0', '0', '0', '0', '0', 'S2'], 
    ['0', 'W2', 'A2', 'L2', 'L2', 'S2', '0']]

#Letters = boxes
#Letters2 = wall
#Letters3 = ice
#Letters4 = player

mapLength, mapWidth = len(mapList1),len(mapList1[0])

def updateIce(): 
    global icy
    create_rectangle(325, 325, 475, 375, fill='black', alpha= 0.2)
    icy = root.after(100,updateIce)

trigger = 0
# Paint the landscape
def drawGameImage():
    global posX, posY
    cv.delete('all')
    for row in range(mapLength):
        for col in range(mapWidth):
            if mapList[row][col] == 'I4':
                # Player's position
                posX = row  
                posY = col
            img = allLetters[mapList[row][col]]
            cv.create_image((row * 50+50, col * 50+50), image=allLetters['0'])
            cv.create_image((row * 50+50, col * 50+50), image=img)
            cv.pack()

def update(ind):
    i4 = i4s[ind]
    ind += 1
    if ind >= 2:
        ind = 0
    allLetters['I4'] = i4
    if trigger!=1: drawGameImage()
    root.after(200, update, ind)

def callback(event):  # Keyboard Control
    global posX, posY, mapList, trigger
    keyPressed = event.keysym
    #Player's current position(posX,y)
    positionDict = {
        "Up" : [0,-1,0,-2],
        "Down" : [0,1,0,2],
        "Left" : [-1,0,-2,0],
        "Right" : [1,0,2,0],
    }
    
    if keyPressed in positionDict:
        moveScale = positionDict[keyPressed]
        x1 = posX+moveScale[0]
        y1 = posY+moveScale[1]
        x2 = posX+moveScale[2]
        y2 = posY+moveScale[3]
        coordinateMove(x1, y1, x2, y2) 
    
    elif keyPressed == "space": # Press SPACE
        print("Press Space", event.char)
        trigger = 0
        mapList = copy.deepcopy(mapList1) # Reset the map
        drawGameImage()

# Determine whether position is within the frame
def validArea(row, col):
    return (row >= 0 and row < mapLength and col >= 0 and col < mapWidth)


def coordinateMove(x1, y1, x2, y2):
    global posX, posY, trigger, icy
    moveTo = None
    behindeMoveTo = None
    if validArea(x1, y1): 
        moveTo = mapList[x1][y1] 
    if validArea(x2, y2):
        behindeMoveTo = mapList[x2][y2]
    if moveTo == '0':  # Able to move to moveTo
        MoveMan(posX, posY) 
        posX = x1 
        posY = y1 
        mapList[x1][y1] = 'I4' 
        pygame.mixer.music.load(walk)
        pygame.mixer.music.play(loops = 0, start=0.0, fade_ms=0)


    if (moveTo in walls) or not validArea(x1, y1):
        # moveTo is wall or out of the game area
        return 
    if moveTo in letters:  # moveTo has a letter
        if (behindeMoveTo in walls) or not validArea(x1, y1) or behindeMoveTo in letters:  ##behindeMoveTo is wall or out of the game area
            return 
    if moveTo in letters and behindeMoveTo == '0':
        MoveMan(posX, posY) 
        posX = x1 
        posY = y1 
        mapList[x2][y2] = moveTo 
        mapList[x1][y1] = 'I4'
        pygame.mixer.music.load(moveBox)
        pygame.mixer.music.play(loops = 0, start=0.0, fade_ms=0)

    if trigger == 0 and triggerEffect() == True:
        pygame.mixer.music.load(melting)
        pygame.mixer.music.play(loops = 0, start=0.0, fade_ms=0)
        trigger += 1
        updateIce()
        
    elif trigger == 1:
        root.after_cancel(icy)
        trigger += 1
        mapList[6][6] = '0'
        mapList[7][6] = '0'
        mapList[8][6] = '0'

    if IsFinish():
        showinfo(message = "You've Passed the First Task! ")
        pygame.mixer.music.stop()
        pygame.mixer.Channel(0).stop()
    drawGameImage()
    
def MoveMan(posX, posY):
    if mapList[posX][posY] == 'I4':
        mapList[posX][posY] = '0' 

## Whether HEAT/FIRE is created
def triggerEffect():
    target = ["HEAT","FIRE"]
    for col in range(len(mapList[0])):
        for row in range(len(mapList)-3):
            secret = ""
            secret += mapList[row][col] + mapList[row+1][col] + mapList[row+2][col] + mapList[row+3][col]
            if secret in target:
                return True
    return False

def IsFinish():  # Whether finish
    bFinish = False 
    if(mapList[6][6] == 'I4' or
    mapList[7][6] == 'I4'or
    mapList[8][6] == 'I4'):
        bFinish = True
    return bFinish

cv = Canvas(root, bg='black', width=800, height=400)
mapList = copy.deepcopy(mapList1)
drawGameImage()
cv.bind("<KeyPress>", callback)
cv.pack()
cv.focus_set()  # Focus on cv
root.after(0, update, 0)
root.update
root.mainloop()
#Gameover stop the music
pygame.mixer.music.stop()
pygame.mixer.Channel(0).stop()