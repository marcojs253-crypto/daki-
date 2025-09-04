import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (0, 0, 0), (100, 380), (540, 380)) # Draw a black line
pygame.draw.line(screen, (0, 0, 0), (100, 378), (540, 378)) #bunden af huset
# Draw the ground
pygame.draw.line(screen, (0, 255, 0), (0, 380), (600, 380))#jorden
# Draw the bottom of the house

# Draw two walls
pygame.draw.line(screen, (0, 0, 0), (100, 380), (100, 30))
pygame.draw.line(screen, (0, 0, 0), (540, 380), (540, 30))
# Draw the roof
pygame.draw.line(screen, (0, 0, 0), (320, 0), (100, 30))
pygame.draw.line(screen, (0, 0, 0), (320, 0), (540, 30))
#loft
pygame.draw.line(screen, (0, 0, 0), (100, 30), (540, 30))

# dør
pygame.draw.rect(screen, (255, 0, 0), (320, 300, 45, 80))
#pool
pygame.draw.rect(screen, (0, 0, 255), (540, 380, 330, 378))

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears