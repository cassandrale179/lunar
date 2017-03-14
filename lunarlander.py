#rocket can kinda move across screen 

import pygame
import time
import random
pygame.init()

#define variables to be used in the program
display_width = 400
display_height = 600
myclock = pygame.time.Clock()
white = (255,255,255)
green = (0,155,0)
black = (0,0,0)
introimg = pygame.image.load("C:\\Users\\lengu\\Desktop\\Pygame\\700862.jpg")
introimg2 = pygame.transform.scale(introimg, (1100,600))
rocket = pygame.image.load("C:\\Users\\lengu\\Desktop\\Pygame\\rocket.png")
rocket2 = pygame.transform.scale(rocket, (100, 100))
asteroid = pygame.image.load("C:\\Users\\lengu\\Desktop\\Pygame\\asteroid.png")
asteroid2 = pygame.transform.scale(asteroid, (30,30))
asteroid3 = pygame.transform.rotate(asteroid2, -90)

#create the screen
gameDisplay = pygame.display.set_mode((display_width, display_height))

#give the game a name
pygame.display.set_caption('Lunar')

#Function 1: Allow message to be displayed
def message_to_screen(message, color, widthdis, heightdis, fontsize):
	myfont = pygame.font.SysFont(None, fontsize)
	screen_text = myfont.render(message, True, color)
	gameDisplay.blit(screen_text, [widthdis, heightdis])

#Function 2: Intro Screen
def gameIntro():
	intro = True;
	while (intro):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_p:
					intro = False

		gameDisplay.blit(introimg2, (-50,0))
		gameDisplay.blit(rocket2, (150, 500))
		message_to_screen("LUNAR LANDER", white, 90, 20, 40)
		message_to_screen("Developed by M. Le", white, 120, 60, 20)
		message_to_screen("Instructions:", white, 20, 240, 20)
		message_to_screen("1. You have 150 protection", white, 30, 260, 20)
		message_to_screen("2. Rock hit = -10 points", white, 30, 275, 20)
		message_to_screen("3. Press <- to move left, -> to move right", white, 30, 290, 20)
		message_to_screen("4. Press P to play, Q to quit", white, 30, 305, 20)
		pygame.display.update()
		myclock.tick(15)



#Function 3: Game Loop
def gameLoop():
	gameExit = False
	gameOver = False
	xroc = 150
	yroc = 500
	xroc_change = 0
	yroc_cahnge = 0

	#while user plays game
	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_RIGHT:
					xroc_change = 5
				if event.key == pygame.K_LEFT:
					xroc_change = -5


		#allow moving until user releases from keyboard
		xroc += xroc_change

		#prevent rocket to disappear from screen
		if xroc > 325: xroc = 325
		if xroc < -20: xroc = -20

		#blitting out images
		gameDisplay.blit(introimg2, (0,0))
		gameDisplay.blit(rocket2, (xroc, yroc))
		gameDisplay.blit(asteroid3, (0, 0))
		position = asteroid3.get_rect()
		gameDisplay.blit(asteroid3, position)
		pygame.display.update()


		for x in range(100):
			gameDisplay.blit(introimg2, position, position)
			position = position.move(5, 5)
			gameDisplay.blit(asteroid3, position)
			pygame.display.update()
			#pygame.time.delay(100)

		myclock.tick(30)

	#while user quits game
	pygame.quit()
	quit()


#Part 4: Calling all the created function
gameIntro()
gameLoop()


