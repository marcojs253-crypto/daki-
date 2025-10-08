import pygame

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

start_punkt= (100,100)
kvadrat_str= (25,25)
for kvadrat in range(0,10):
    pygame.draw.rect(screen,(0,0,0), (start_punkt[0]+kvadrat*30,start_punkt[1])+kvadrat_str)



run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears