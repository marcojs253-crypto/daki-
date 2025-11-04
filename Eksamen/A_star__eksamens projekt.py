import random
import pygame
import math
import random
from opensimplex import OpenSimplex

screen_size =[1000,800]
felt_størrelse = 20

def randomisere_seed(event, seed):
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                seed=random.randint(1,100)
    return seed


def draw_grid(screen,seed):
    gen = OpenSimplex(seed)
    for y in range(screen_size[1]//felt_størrelse ):
        for x in range(screen_size[0]//felt_størrelse ):
            v = gen.noise2(x*0.075, y*0.075)
            if v < -0.5:
                color = (0, 0, 180)      # Hav
            elif v < 0.3:
                color = (51, 255, 51)  # græs
            elif v <= 0.75:
                color = (64, 64, 64)  # bjerg
            else:
                color = (255, 70, 0)   # Lava
            rect= ((x*felt_størrelse), (y*felt_størrelse), felt_størrelse, felt_størrelse)
            pygame.draw.rect(screen, color, rect)

def mousse_locading(event, position_højere, position_venstre):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                position_højere = pygame.mouse.get_pos()
            if event.button == 1:
                position_venstre=pygame.mouse.get_pos()
        return position_højere, position_venstre

def mouse_dot_draw (screen, position_venstre, position_højere ):
    if position_højere is not None:
        pygame.draw.circle(screen, (158,115,178), position_højere, 5)
    if position_venstre is not None:
        pygame.draw.circle(screen, (255,255,255), position_venstre, 5)


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
    
    pygame.display.set_caption("Maze Visualizer")
    position_højere = None
    position_venstre = None
    run_flag = True
    seed = 0
    old_seed = seed
    while run_flag is True:
        draw_grid (screen, seed)
        
        for event in pygame.event.get():
            seed = randomisere_seed(event, seed)  # ← Gem returnværdien
            
            if seed != old_seed:  # ← Hvis seed ændrer sig
                position_højere = None
                position_venstre = None
                old_seed = seed
            
            position_højere, position_venstre = mousse_locading(event, position_højere, position_venstre)
            
            if event.type == pygame.QUIT:
                run_flag = False
        
        mouse_dot_draw(screen, position_venstre, position_højere)
        pygame.display.flip()
        

if __name__ == '__main__':
    main ()


    # class kort():
    # def __init__ (self, screen_size):
    #     self.screen_size = screen_size
    #     def draw_grid(self,screen):
    #         for y in range(screen_size[0]):
    #             for x in range(screen_size[1]):
    #                 v = gen.noise2(x, y)
    #                 if v < 0.3:
    #                     color = (0, 0, 180)      # Hav

    #                 elif v < 0.6:
    #                     color = (51, 255, 51)  # græs
    #                 elif v < 0.9:
    #                     color = (64, 64, 64)  # bjerg
    #                 else:
    #                     color = (255, 0, 0)   # Lava
    #                 screen.set_at((x, y), color)