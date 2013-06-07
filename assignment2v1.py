# Name: Graydon Armstrong
# Date: June 5th, 2013
# Source File: assignment2v1.py
# Last Modified By: Graydon Armstrong
# Date Last Modified: June 5th, 2013
# Program description: A slot machine game where the player can bet money and win
# Revision History: Version 1 is drawing a temporary GUI for the slot machine to try out pygame

#I - Import and initialize
import pygame
pygame.init()

def main():
    #D - Display configuration
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Hello, world!")
    x_pos = 200
    y_pos = 200
    
    #E - Entities (just background for now)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 255))
    
    box = []
    box_x = [100,220,340]
    box_y = [100,100,100]

    for i in range(3):
        box.append(pygame.Surface((100,100)))
        box[i] = box[i].convert()
        box[i].fill((50,50,50))
    
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print pygame.mouse.get_pos()
                coordinates = list(pygame.mouse.get_pos())
                x_pos = coordinates[0]
                y_pos = coordinates[1]
    
        #R - Refresh display
        screen.blit(background, (0, 0))
        for i in range(3):
            screen.blit(box[i],(box_x[i],box_y[i]))
        pygame.display.flip()

    
# run the main class        
if __name__ == "__main__": main()
