import pygame
import time
import random
pygame.init()

#define variables to be used in the program
display_width = 400
display_height = 600
myfont = pygame.font.SysFont(None, 25)
myclock = pygame.time.Clock()
white = (255,255,255)
green = (0,155,0)
black = (0,0,0)

#create the screen
gameDisplay = pygame.display.set_mode((display_width, display_height))

#give the game a name
pygame.display.set_caption('Lunar')

#Function 1: Allow message to be displayed
def message_to_screen(message, color):
	screen_text = myfont.render(message, True, color)
	gameDisplay.blit(screen_text, [display_width/2, display_height/2])

#intro function
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

        gameDisplay.fill(white)
        message_to_screen("LUNAR", green)
        message_to_screen("Press P to Play or Q to Quit", black)
        pygame.display.update()
        myclock.tick(15)

#Function 3: Game Loop
def gameLoop():
    gameExit = False                        #false condition prevent display before game loop
    gameOver = False                        #false condition prevent display before game loop

    #while user plays game
    while not gameExit:
        for event in pygame.event.get:
            if event.type == game.Quit:     #if user decide to end game
                gameOver = False            #gameover screen is false because the user doesn't lose the game
                gameExit = True             #gameExit screen is true since game is quit




        #specify 15 frame per second
        myclock.tick(30)

    #while user quits game
    pygame.quit()
    quit()



gameIntro()                                 #call the intro screen
gameLoop()                                  #initialize the game loop
