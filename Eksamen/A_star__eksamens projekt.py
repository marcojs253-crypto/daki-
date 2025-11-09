import random
import pygame
import math
from opensimplex import OpenSimplex

from queue import PriorityQueue

screen_size = [1000, 800]
felt_størrelse = 40

def teng_algoritmen(start, goal, graph, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current_priority, current = frontier.get()
        if current == goal:
            break
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put((priority, next))
                came_from[next] = current
    return came_from, cost_so_far

def randomisere_seed(event, seed, højre_position, venstre_position):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            seed = random.randint(1, 100)
            venstre_position = None
            højre_position = None
    return seed, højre_position, venstre_position

def tegn_kortet(screen, seed):
    gen = OpenSimplex(seed)
    for y in range(screen_size[1] // felt_størrelse):
        for x in range(screen_size[0] // felt_størrelse):
            v = gen.noise2(x * 0.075, y * 0.075)
            if v < -0.5:
                felt_dictionary = {
                    'type': ["hav"],
                    'bevægels_pris': [3],
                    'farve': (0, 0, 180)
                }
            elif v < 0.3:
                felt_dictionary = {
                    'type': ["græs"],
                    'bevægels_pris': [1],
                    'farve': (51, 255, 51)
                }
            elif v <= 0.75:
                felt_dictionary = {
                    'type': ["bjerg"],
                    'bevægels_pris': [5],
                    'farve': (64, 64, 64)
                }
            else:
                felt_dictionary = {
                    'type': ["Lava"],
                    'bevægels_pris': [1000],
                    'farve': (255, 70, 0)
                }
            rect = (x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse)
            pygame.draw.rect(screen, felt_dictionary['farve'], rect)

def registre_klik(event, position_højere, position_venstre):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3:
            position_højere = pygame.mouse.get_pos()
        if event.button == 1:
            position_venstre = pygame.mouse.get_pos()
    return position_højere, position_venstre

def teng_cirkel(screen, position_højere, position_venstre):
    if position_højere is not None:
        pygame.draw.circle(screen, (158, 115, 178), position_højere, 5)
    if position_venstre is not None:
        pygame.draw.circle(screen, (255, 255, 255), position_venstre, 5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
    pygame.display.set_caption("kort_spillet")
    seed = 0
    venstre_position = None
    højre_position = None
    run_flag = True
    while run_flag:
        tegn_kortet(screen, seed)
        teng_cirkel(screen, højre_position, venstre_position)
        for event in pygame.event.get():
            seed, højre_position, venstre_position = randomisere_seed(event, seed, højre_position, venstre_position)
            højre_position, venstre_position = registre_klik(event, højre_position, venstre_position)
            if event.type == pygame.QUIT:
                run_flag = False
        pygame.display.flip()

if __name__ == '__main__':
    main()
