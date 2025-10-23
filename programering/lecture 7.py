import pygame
import math
import random

# def draw():
#     run_flag = True
#     while run_flag is True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run_flag = False
        # pygame.display.flip() 

def grid():
    
    def gentag():
         liste_af_0er =[]
         for tal in range(6):
            liste_af_0er.append(0)
         return  liste_af_0er
    x = gentag()
    liste_af_lister = []
    for tal in range(4):
        x = gentag()
        liste_af_lister.append(x)
    return liste_af_lister
    
tal_grid = grid()
print(tal_grid)

# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((640, 480))
#     screen.fill((255, 255, 255))
#     draw()


# main()







