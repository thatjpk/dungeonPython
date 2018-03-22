from sys import exit as endGame
from random import randint as randNum
from pygame.locals import *
import pygame
pygame.init()

global white, grey, red, yellow, green, blue
global randDoor, randBlock

#Non-Color Variables
displayWidth = 1000
displayHeight = 1000
gameOver = False
xBox = 0
yBox = 0
imageType = None
firstTime = True
randDoor = randNum(1,8)
randBlock = randNum(1,10)
gameBoard = []
entrancePos = []
posPath = []

#Images
playerImg = pygame.transform.scale(pygame.image.load("pixelChar.png"), (75, 75))
path = pygame.transform.scale(pygame.image.load("path.png"), (100,100))
crackedPath = pygame.transform.scale(pygame.image.load("crackedPath.png"), (100,100))
flowerPath = pygame.transform.scale(pygame.image.load("flowerPath.png"), (100,100))
crackedFlowerPath = pygame.transform.scale(pygame.image.load("crackedFlowerPath.png"),(100,100))

#Colors
white = (255, 255, 255)
grey = (125, 125, 125)

red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 210, 0)
blue = (0, 125, 255)

def getBlockType(blockX, blockY, blockKind): #Defining blocks in the grid
	global entrancePos
	if(blockKind == "origPath"):
		randBlock = randNum(1,5)
		if(randBlock <= 4): return "path"
		return "actionBlock"
	if(blockKind == "other"):
		if(blockX == 0 or blockX == 9 or blockY == 0 or blockY == 9):
			if(blockY == 9 and randDoor == blockX):
				entrancePos = [randDoor,blockY]
				return "entrance"
			return "border"
		randBlock = randNum(1,25)
		if(randBlock <= 9): return "path"
		if(randBlock > 9 and randBlock < 24): return "wall"
		return "actionBlock"

def getArt(blockKind):
	print(blockKind)
	if(blockKind == "path"):
		randomVar = randNum(1,4)
		if(randomVar == 1): return 'path'
		if(randomVar == 2): return 'crackedPath'
		if(randomVar == 3): return 'flowerPath'
		if(randomVar == 4): return 'crackedFlowerPath'
	if(blockKind == "border"): return 'borderArt'
	if(blockKind == "wall"): return 'wallArt'
	if(blockKind == "actionBlock"): return 'actionBlock'
	if(blockKind == "entrance"): return 'entranceArt'
	if(blockKind == "exit"): return 'exitArt'

def getDir(entrancePos): #Creating the random path
	global posPath
	blockX = entrancePos[0]
	blockY = entrancePos[1]
	while(blockY-1 != 0):
		randomVar = randNum(1,3)
		if(randomVar == 1 and gameBoard[blockX-1][blockY][0] != "border"): #Left
			blockX -= 1
		if(randomVar == 2 and gameBoard[blockX][blockY-1][0] != "border"): #Up
			blockY -= 1
		if(randomVar == 3 and gameBoard[blockX+1][blockY][0] != "border"): #Right
			blockX += 1
		posPath.append([blockX, blockY])
	exitPos = [blockX, blockY-1]
	for x in range(len(posPath)):
		gameBoard[posPath[x][0]][posPath[x][1]] = [getBlockType(posPath[x][0],posPath[x][1],"origPath")]
	gameBoard[exitPos[0]][exitPos[1]] = ["exit"]

def keyUp(event, funcX, funcY): #Start Movement on Key Down
	if(event.key == K_UP or event.key == K_w):
		if(funcY-1 >= 0 and funcY-1 <= 9):
			if(gameBoard[funcX][funcY-1][0] != "wall" and gameBoard[funcX][funcY-1][0] != "border"):
				funcY -= 1
	elif(event.key == K_DOWN or event.key == K_s):
		if(funcY+1 >= 0 and funcY+1 <= 9):
			if(gameBoard[funcX][funcY+1][0] != "wall" and gameBoard[funcX][funcY+1][0] != "border"):
				funcY += 1
	elif(event.key == K_LEFT or event.key == K_a):
		if(funcX-1 >= 0 and funcX-1 <= 9):
			if(gameBoard[funcX-1][funcY][0] != "wall" and gameBoard[funcX-1][funcY][0] != "border"):
				funcX -= 1
	elif(event.key == K_RIGHT or event.key == K_d):
		if(funcX+1 >= 0 and funcX+1 <= 9):
			if(gameBoard[funcX+1][funcY][0] != "wall" and gameBoard[funcX+1][funcY][0] != "border"):
				funcX += 1
	return funcX, funcY

#Createing the game board
gameBoard = [[[""] for x in range(10)] for y in range(10)]
for loopY in range(0,10):
	for loopX in range(0,10):
		blockType = getBlockType(loopX,loopY,"other")
		gameBoard[loopX][loopY][0] = blockType
	randDoor = randNum(1,8)

getDir(entrancePos)

#Making art for the game after the path is generated
for loopY in range(0,10):
	for loopX in range(0,10):
		art = getArt(gameBoard[loopX][loopY][0])
		gameBoard[loopX][loopY].append(art)

#Sets the player's position
xBox, yBox = entrancePos

#Creates the pygame screen
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

while(gameOver == False): #Main Game Loop
	for event in pygame.event.get():
		if(event.type == pygame.KEYUP):
			xBox, yBox = keyUp(event, xBox, yBox)
		if(event.type == pygame.QUIT):
			gameOver = True
	screen.fill(white)

	#Prints the two-dimensional array to the screen
	for x in range(len(gameBoard)):
		for y in range(10):
			if(gameBoard[x][y][1][len(gameBoard[x][y][1])-4:len(gameBoard[x][y][1])].lower() == "path"):
				screen.blit(pygame.transform.scale(pygame.image.load(str(gameBoard[x][y][1]) + ".png"), (100,100)),(x*100, y*100))
			if(gameBoard[x][y][1] == "borderArt"): pygame.draw.rect(screen, grey, (x*100, y*100, 100, 100))
			if(gameBoard[x][y][1] == "wallArt"): pygame.draw.rect(screen, grey, (x*100, y*100, 100, 100))
			if(gameBoard[x][y][1] == "actionBlock"): pygame.draw.rect(screen, red, (x*100, y*100, 100, 100))
			if(gameBoard[x][y][1] == "entrance"): pygame.draw.rect(screen, green, (x*100, y*100, 100, 100))
			if(gameBoard[x][y][1] == "exit"): pygame.draw.rect(screen, green, (x*100, y*100, 100, 100))

	screen.blit(playerImg,(xBox*100+12, yBox*100+12))

	pygame.display.update()
	clock.tick(60)
endGame()