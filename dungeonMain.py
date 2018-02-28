from sys import exit as endGame
from random import randint as randNum
from pygame.locals import *
import pygame
pygame.init()

#Non-Color Variables
displayWidth = 800
displayHeight = 800
gameOver = False
x_box = 0
y_box = 0
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

def getBlockType(blockX, blockY):
	randomVar = randNum(1,3)
	if(blockX == 0 or blockX == 11 or blockY == 0 or blockY == 11):
		return "border"
	if(randomVar == 1): return "path"
	if(randomVar == 2): return "wall"
	return "actionBlock"

def keyDown(event): #Start Movement on Key Press
    global x_change, y_change
    if event.key == K_UP or event.key == K_w:
    	y_box += 1
    elif event.key == K_DOWN or event.key == K_s:
    	y_box -= 1
    elif event.key == K_LEFT or event.key == K_a:
    	x_box += 1
    elif event.key == K_RIGHT or event.key == K_d:
    	x_box -= 1

def keyUp(event): #Stop Movement on Key Lift
    global x_change, y_change
    if event.key in (K_w, K_s, K_DOWN, K_UP):
        y_change = 0
    elif event.key in (K_a, K_d, K_LEFT, K_RIGHT):
        x_change = 0

gameBoard = [["" for x in range(12)] for y in range(12)]
posPath = []

for loopX in range(0,12):
	for loopY in range(0,12):
		blockType = getBlockType(loopX,loopY)
		gameBoard[loopX][loopY] = blockType

screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

for x in range(int(displayWidth/20)):
	for y in range(int(displayHeight/20)):
		if(y % 2 == 0):
			pygame.draw.rect(screen, red, (20, 20, x*20, y*20))
		else:
			pygame.draw.rect(screen, blue, (20, 20, x*20, y*20))

while(gameOver == False): #Main Game Loop
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			gameOver = True
		if(event.type == pygame.KEYUP):
			keyUp(event)
		if(event.type == pygame.KEYDOWN):
			keyDown(event)

	for x in range(int(displayWidth/20)):
		for y in range(int(displayHeight/20)):
			if(y % 2 == 0):
				pygame.draw.rect(screen, red, (20, 20, x*20, y*20))
			else:
				pygame.draw.rect(screen, blue, (20, 20, x*20, y*20))

	screen.fill(green)

	pygame.display.update()
	clock.tick(60)
endGame()