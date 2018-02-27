from sys import exit as endGame
from random import randint as randNum
from pygame.locals import *
import pygame
pygame.init()

global white, grey, black, brown, red, orange, yellow, green, blue, violet
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

#Neutral Colors
white = (255, 255, 255)
grey = (127, 127, 127)
black = (0, 0, 0)
brown = (145, 90, 15)

#Other Colors
red = (255, 0, 0)
orange = (255, 125, 0)
yellow = (255, 255, 0)
green = (0, 210, 0)
blue = (0, 125, 255)
violet = (200, 0, 200)

def isSteppable(funcX, funcY):

def getBlockType(blockX, blockY): #Defining blocks in the grid
	if(blockX == 0 or blockX == 9 or blockY == 0 or blockY == 9):
		if(blockY == 0 and randDoor == blockX):
			return "exit"
		if(blockY == 9 and randDoor == blockX):
			return "entrance"
		return "border"
	randBlock = randNum(1,10)
	if(randBlock <= 7): return "path"
	if(randBlock > 7 and randBlock < 10): return "wall"
	return "actionBlock"

def getColor(tileType): #Coloring the blocks
	if(tileType == "border" or tileType == "wall"):
		return grey
	if(tileType == "exit" or tileType == "entrance"):
		return green
	if(tileType == "path"):
		return yellow
	if(tileType == "actionBlock"):
		return red

def getEntrance():
	for x in range(len(gameBoard)):
		for y in range(10):
			if(gameBoard[x][y] == "entrance"):
				print("x: " + str(x))
				print("y: " + str(y))
				return x, y

def keyDown(event, funcX, funcY): #Start Movement on Key Down
	if(event.key == K_UP or event.key == K_w):
		funcY -= 1
	elif(event.key == K_DOWN or event.key == K_s):
		funcY += 1
	elif(event.key == K_LEFT or event.key == K_a):
		funcX -= 1
	elif(event.key == K_RIGHT or event.key == K_d):
		funcX += 1
	return funcX, funcY

def keyUp(event): #Stop Movement on Key Lift
	pass

#Creates the game board
gameBoard = [["" for x in range(10)] for y in range(10)]
for loopY in range(0,10):
	for loopX in range(0,10):
		blockType = getBlockType(loopX,loopY)
		gameBoard[loopX][loopY] = blockType
	randDoor = randNum(1,8)

#Sets the play position
xBox, yBox = getEntrance()

#Creates the pygame screen
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

while(gameOver == False): #Main Game Loop
	for event in pygame.event.get():
		if(event.type == pygame.KEYUP):
			xBox, yBox = keyDown(event, xBox, yBox)
		if(event.type == pygame.KEYDOWN):
			keyUp(event)
		if(event.type == pygame.QUIT):
			gameOver = True

	screen.fill(white)

	#Prints the two-dimensional array to the screen
	for x in range(len(gameBoard)):
		for y in range(10):
			color = getColor(gameBoard[x][y])
			pygame.draw.rect(screen, color, (x*100, y*100, 100, 100))

	pygame.draw.rect(screen, blue, ((xBox*100)+25, (yBox*100)+25, 50, 50))

	pygame.display.update()
	clock.tick(60)
endGame()