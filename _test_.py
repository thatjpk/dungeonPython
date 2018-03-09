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
randDoor = randNum(1,8)
randBlock = randNum(1,10)
gameBoard = []
entrancePos = []
posPath = []

#Images
playerImg = pygame.transform.scale(pygame.image.load("pixelChar.png"), (75, 75))

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

def getDir(entrancePos): #Creating the random path
	global posPath
	blockX = entrancePos[0]
	blockY = entrancePos[1]
	while(blockY-1 != 0):
		randomVar = randNum(1,3)
		if(randomVar == 1 and gameBoard[blockX-1][blockY] != "border"): #Left
			blockX -= 1
		if(randomVar == 2 and gameBoard[blockX][blockY-1] != "border"): #Up
			blockY -= 1
		if(randomVar == 3 and gameBoard[blockX+1][blockY] != "border"): #Right
			blockX += 1
		posPath.append([blockX, blockY])
	exitPos = [blockX, blockY-1]
	for x in range(len(posPath)):
		gameBoard[posPath[x][0]][posPath[x][1]] = getBlockType(posPath[x][0],posPath[x][1],"origPath")
	gameBoard[exitPos[0]][exitPos[1]] = "exit"

def keyUp(event, funcX, funcY): #Start Movement on Key Down
	if(event.key == K_UP or event.key == K_w):
		if(funcY-1 >= 0 and funcY-1 <= 9):
			if(gameBoard[funcX][funcY-1] != "wall" and gameBoard[funcX][funcY-1] != "border"):
				funcY -= 1
	elif(event.key == K_DOWN or event.key == K_s):
		if(funcY+1 >= 0 and funcY+1 <= 9):
			if(gameBoard[funcX][funcY+1] != "wall" and gameBoard[funcX][funcY+1] != "border"):
				funcY += 1
	elif(event.key == K_LEFT or event.key == K_a):
		if(funcX-1 >= 0 and funcX-1 <= 9):
			if(gameBoard[funcX-1][funcY] != "wall" and gameBoard[funcX-1][funcY] != "border"):
				funcX -= 1
	elif(event.key == K_RIGHT or event.key == K_d):
		if(funcX+1 >= 0 and funcX+1 <= 9):
			if(gameBoard[funcX+1][funcY] != "wall" and gameBoard[funcX+1][funcY] != "border"):
				funcX += 1
	return funcX, funcY

def getColor(tileType): #Coloring the blocks
	if(tileType == "border" or tileType == "wall"):
		return grey
	if(tileType == "exit" or tileType == "entrance"):
		return green
	if(tileType == "path"):
		return yellow
	if(tileType == "actionBlock"):
		return red

#Createing the game board
gameBoard = [["" for x in range(10)] for y in range(10)]
for loopY in range(0,10):
	for loopX in range(0,10):
		blockType = getBlockType(loopX,loopY,"other")
		gameBoard[loopX][loopY] = blockType
	randDoor = randNum(1,8)

getDir(entrancePos)

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
			color = getColor(gameBoard[x][y])
			pygame.draw.rect(screen, color, (x*100, y*100, 100, 100))

	screen.blit(playerImg,(xBox*100+12, yBox*100+12))

	pygame.display.update()
	clock.tick(60)
endGame()