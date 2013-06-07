# Name: Graydon Armstrong
# Date: June 5th, 2013
# Source File: assignment2v1.py
# Last Modified By: Graydon Armstrong
# Date Last Modified: June 5th, 2013
# Program description: A slot machine game where the player can bet money and win
# Revision History: Version 3 is adding functionality to the game

#I - Import and initialize
import pygame, random
pygame.init()

#method to find out if the mouse is within the area of an object
def mouseWithin(obj_x, obj_y, obj_width, obj_height):
    coordinates = list(pygame.mouse.get_pos())
    mouse_x = coordinates[0]
    mouse_y = coordinates[1]
    if (mouse_x >= obj_x and mouse_x <= obj_x+obj_width and 
        mouse_y >= obj_y and mouse_y <= obj_y+obj_height):
        return True
    else:
        return False

#calculate the money won from the spin and whether the jacpot was won
def calculateSpin(reelValue, reelMultipliers, bet):
    moneyWon = bet*reelMultipliers[reelValue[0]]*reelMultipliers[reelValue[1]]*reelMultipliers[reelValue[2]]
    moneyWon = int(moneyWon)
    jackpot = False
    
    #if all the reels are the same image its a jackpot
    if (reelValue[0] == reelValue[1] and reelValue[0] == reelValue[2]):
        #you have to get three cherrys bells or sevens to win the jackpot
        if reelValue[0] == 4 or reelValue[0] == 5 or reelValue[0] == 6:
            jackpot = True
    else:
        jackpot = False
        
    return moneyWon, jackpot 

#calculate a reel value with some harder to get than others
def getReelValue():
    randNum = random.randint(0,99)
    if randNum < 40:
        value = 0
    elif randNum <60:
        value = 1
    elif randNum < 75:
        value = 2
    elif randNum < 85:
        value = 3
    elif randNum < 92:
        value = 4
    elif randNum < 97:
        value = 5
    elif randNum < 100:
        value = 6
    return value
        
def main():
    #D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Slots!")
    x_pos = 200
    y_pos = 200
    
    #E - Entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 255))
    
    #Game Variables
    money = 100
    bet = 1
    jackpot = 500
    
    #load the reel images
    reelImages = [pygame.image.load("blank.jpg"),
                  pygame.image.load("bar.jpg"),
                  pygame.image.load("grape.jpg"),
                  pygame.image.load("orange.jpg"),
                  pygame.image.load("cherry.jpg"),
                  pygame.image.load("bell.jpg"),
                  pygame.image.load("seven.jpg"),]
    for i in range (len(reelImages)):
        reelImages[i].convert()
        
    #set the reel multipliers
    reelMultipliers = [0,1.1,1.2,1.4,1.8,2.6,4.2]
    
    #Create labels for different variables to show the user
    myFont = pygame.font.SysFont("arial",30)
    moneyLabel = myFont.render("Money: " + str(money), 1, (255,255,255))
    betLabel = myFont.render("Bet: " + str(bet), 1, (255,255,255))
    jackpotLabel = myFont.render("Jackpot: " + str(jackpot), 1, (255,255,255))
    
    #the spin button
    spinButton_x = 100
    spinButton_y = 270
    spinButton_width = 490
    spinButton_height = 40
    spinButton_clicked = False
    spinButton = pygame.Surface((spinButton_width,spinButton_height))
    spinButton = spinButton.convert()
    spinButton.fill((50,50,50))
    spinLabel = myFont.render("Spin!", 1, (255,255,255))
    
    #reset button
    resetButton_x = 310
    resetButton_y = 330
    resetButton_width = 130
    resetButton_height = 50
    resetButton = pygame.Surface((resetButton_width,resetButton_height))
    resetButton = resetButton.convert()
    resetButton.fill((50,50,50))
    resetLabel = myFont.render("Reset", 1, (255,255,255))
    
    #quit button
    quitButton_x = 460
    quitButton_y = 330
    quitButton_width = 130
    quitButton_height = 50
    quitButton = pygame.Surface((quitButton_width,quitButton_height))
    quitButton = quitButton.convert()
    quitButton.fill((50,50,50))
    quitLabel = myFont.render("Quit", 1, (255,255,255))
    
    #bet buttons
    num_bets = 3
    betButton = []
    betButton_label = [myFont.render("1", 1, (255,255,255)),
                       myFont.render("5", 1, (255,255,255)),
                       myFont.render("10", 1, (255,255,255))]
    betButton_x = [100, 170, 240]
    betButton_y = [330, 330, 330]
    betButton_width = 50
    betButton_height = 50
    for i in range(num_bets):
        betButton.append(pygame.Surface((betButton_width,betButton_height)))
        betButton[i] = betButton[i].convert()
        betButton[i].fill((50,50,50))
    
    #the reels
    num_reels = 3
    reelSprite = []
    reelValue = [0,0,0]
    reel_x = [100,270,440]
    reel_y = [100,100,100]
    for i in range(num_reels):
        reelSprite.append(reelImages[0])
        reelSprite[i] = reelSprite[i].convert()
    
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
            #quit event
            if event.type == pygame.QUIT:
                keepGoing = False
                
            #mouseup events
            elif event.type == pygame.MOUSEBUTTONUP:
                #mouse event for the spin button
                if (mouseWithin(spinButton_x, spinButton_y, spinButton_width, spinButton_height)):
                    for i in range(num_reels):
                        reelValue[i] = getReelValue()
                        reelSprite[i] = reelImages[reelValue[i]]
                    spinButton_clicked = True
                    moneyWon, isJackpot = calculateSpin(reelValue, reelMultipliers, bet)
                    if (isJackpot == True):
                        money += moneyWon + jackpot
                        jackpot = 500
                    else:
                        if (moneyWon > 0):
                            money += moneyWon
                        else:
                            money -= bet
                            jackpot += bet
                    moneyLabel = myFont.render("Money: " + str(money), 1, (255,255,255))
                    jackpotLabel = myFont.render("Jackpot: " + str(jackpot), 1, (255,255,255))  
                spinButton.fill((50,50,50))
                
                #mouse event for the change bet buttons
                if (mouseWithin(betButton_x[0], betButton_y[0], betButton_width, betButton_height)):
                    bet = 1
                elif (mouseWithin(betButton_x[1], betButton_y[1], betButton_width, betButton_height)):
                    bet = 5
                elif (mouseWithin(betButton_x[2], betButton_y[2], betButton_width, betButton_height)):
                    bet = 10
                betLabel = myFont.render("Bet: " + str(bet), 1, (255,255,255))
                
                #mouse event for reset button
                if (mouseWithin(resetButton_x, resetButton_y, resetButton_width, resetButton_height)):
                    #reset all variables to defaults
                    bet = 1
                    money = 100
                    jackpot = 500
                    #change the reels back to blanks
                    for i in range(num_reels):
                        reelSprite[i] = reelImages[0]
                        reelValue[i] = 0
                    #update the lables with the default variables
                    moneyLabel = myFont.render("Money: " + str(money), 1, (255,255,255))
                    betLabel = myFont.render("Bet: " + str(bet), 1, (255,255,255))
                    jackpotLabel = myFont.render("Jackpot: " + str(jackpot), 1, (255,255,255))
                    
                #mouse event for quit button
                if (mouseWithin(quitButton_x, quitButton_y, quitButton_width, quitButton_height)):
                    keepGoing = False
                    
            #mousedown events                 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #mouse event for the spin button
                if (mouseWithin(spinButton_x, spinButton_y, spinButton_width, spinButton_height)):
                    spinButton.fill((200,200,200))
                    spinButton_clicked = False                    
    
        #R - Refresh display
        
        #draw background
        screen.blit(background, (0, 0))
        
        #draw reels
        for i in range(num_reels):
            screen.blit(reelSprite[i],(reel_x[i],reel_y[i]))
            
        #draw bet buttons and their labels
        for i in range(num_bets):
            screen.blit(betButton[i],(betButton_x[i],betButton_y[i]))
            screen.blit(betButton_label[i], (betButton_x[i]+10,betButton_y[i]+8))
        
        #draw spin button and label
        screen.blit(spinButton, (spinButton_x,spinButton_y))
        screen.blit(spinLabel, (spinButton_x+spinButton_width/2-20,spinButton_y))
        
        #draw reset button and label
        screen.blit(resetButton, (resetButton_x,resetButton_y))
        screen.blit(resetLabel, (resetButton_x+resetButton_width/2-30,resetButton_y+8))
        
        #draw quit button and label
        screen.blit(quitButton, (quitButton_x,quitButton_y))
        screen.blit(quitLabel, (quitButton_x+quitButton_width/2-20,quitButton_y+8))
        
        #draw money, bet, and jackpot labels on screen
        screen.blit(moneyLabel, (250,50))
        screen.blit(betLabel, (100,50))
        screen.blit(jackpotLabel, (450,50))
        
        #flip the image to the display
        pygame.display.flip()
    
# run the main class        
if __name__ == "__main__": main()