from sys import exit as endGame
from pygame.locals import *
import pygame
pygame.init()

#Non-Color Variables
displayWidth = 800
displayHeight = 600
gameOver = False
x_change = 0
y_change = 0
x = 0
y = 0

#Neatral Colors
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

screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Dungeon Game")
clock = pygame.time.Clock()

#Image/Shape Declarations
boxImg = pygame.image.load("square.png")
boxImg = pygame.transform.scale(boxImg, (200, 200))

def keyDown(event): #Start Movement on Key Press
    global x_change, y_change
    
    if event.key == K_UP or event.key == K_w:
    	y_change = -5
    elif event.key == K_DOWN or event.key == K_a:
    	y_change = 5
    elif event.key == K_LEFT or event.key == K_s:
    	x_change = -5
    elif event.key == K_RIGHT or event.key == K_d:
    	x_change = 5

def keyUp(event): #Stop Movement on Key Lift
    global x_change, y_change

    if event.key in (K_w, K_s, K_DOWN, K_UP):
        y_change = 0
    elif event.key in (K_a, K_d, K_LEFT, K_RIGHT):
        x_change = 0

while(gameOver == False): #Main Game Loop
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			gameOver = True
		if(event.type == pygame.KEYUP):
			keyUp(event)
		if(event.type == pygame.KEYDOWN):
			keyDown(event)

	if(x + x_change >= 0 or x + x_change <= displayWidth-200):
		x += x_change
	if(y + y_change >= 0 or y + y_change <= displayHeight-200):
		y += y_change

	screen.fill(green)
	screen.blit(boxImg, (x,y))
	pygame.draw.rect(screen, red, (x+75, y+75, 50, 50))

	pygame.display.update()
	clock.tick(60)
endGame()