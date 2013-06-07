# Name: Graydon Armstrong
# Date: June 5th, 2013
# Source File: assignment2v1.py
# Last Modified By: Graydon Armstrong
# Date Last Modified: June 5th, 2013
# Program description: A slot machine game where the player can bet money and win
# Revision History: Version 2 is putting together a end version GUI

#I - Import and initialize
import pygame, random
pygame.init()

def mouseWithin(obj_x, obj_y, obj_width, obj_height):
    coordinates = list(pygame.mouse.get_pos())
    mouse_x = coordinates[0]
    mouse_y = coordinates[1]
    if (mouse_x >= obj_x and mouse_x <= obj_x+obj_width and 
        mouse_y >= obj_y and mouse_y <= obj_y+obj_height):
        return True
    else:
        return False
        
def main():
    #D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Slots!")
    x_pos = 200
    y_pos = 200
    
    #E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 255))
    
    #pull a picture
    reelImages = [pygame.image.load("blank.jpg"),
                  pygame.image.load("bar.jpg"),
                  pygame.image.load("seven.jpg"),
                  pygame.image.load("bell.jpg"),
                  pygame.image.load("grape.jpg"),
                  pygame.image.load("orange.jpg"),
                  pygame.image.load("cherry.jpg"),]
    for i in range (len(reelImages)):
        reelImages[i].convert()
    
    #Put a label on the screen
    myFont = pygame.font.SysFont("arial",30)
    moneyLabel = myFont.render("Money: 100", 1, (255,255,255))
    spinLabel = myFont.render("Spin!", 1, (255,255,255))
    
    #the spin button
    spinButton_x = 100
    spinButton_y = 270
    spinButton_width = 490
    spinButton_height = 40
    spinButton_clicked = False
    spinButton = pygame.Surface((spinButton_width,spinButton_height))
    spinButton = spinButton.convert()
    spinButton.fill((50,50,50))
    
    #bet buttons
    num_bets = 3
    betButton = []
    betButton_x = [100, 170, 240]
    betButton_y = [330, 330, 330]
    betButton_width = 50
    betButton_height = 50
    for i in range(num_bets):
        betButton.append(pygame.Surface((betButton_width,betButton_height)))
        betButton[i] = betButton[i].convert
        betButton[i].fill((50,50,50))
    
    #the reels
    num_reels = 3
    reel = []
    reel_x = [100,270,440]
    reel_y = [100,100,100]
    for i in range(num_reels):
        reel.append(reelImages[0])
        reel[i] = reel[i].convert()
    
    #A - Action (broken into ALTER steps)
    
        #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
    
        #L - Set up main loop
    while keepGoing:
    
        #T - Timer to set frame rate
        clock.tick(30)
    
        #E - Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if (mouseWithin(spinButton_x, spinButton_y, spinButton_width, spinButton_height)):
                    for i in range(num_reels):
                        rand = random.randint(0,6)
                        reel[i] = reelImages[rand]
                    #spinReels() - This is where the spin the reels will happen onClick
                    spinButton_clicked = True
                spinButton.fill((50,50,50))               
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (mouseWithin(spinButton_x, spinButton_y, spinButton_width, spinButton_height)):
                    spinButton.fill((200,200,200))
                    spinButton_clicked = False
                    
    
        #R - Refresh display
        screen.blit(background, (0, 0))
        for i in range(num_reels):
            screen.blit(reel[i],(reel_x[i],reel_y[i]))
        for i in range(num_bets):
            screen.blit(betButton[i],(betButton_x[i],betButton_y[i]))
        screen.blit(spinButton, (spinButton_x,spinButton_y))
        screen.blit(spinLabel, (spinButton_x+spinButton_width/2-20,spinButton_y))
        screen.blit(moneyLabel, (250,50))
        pygame.display.flip()

    
# run the main class        
if __name__ == "__main__": main()