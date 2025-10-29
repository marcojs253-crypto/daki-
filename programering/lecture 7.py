import sys
import pygame
import math
import random


def grid():
    # Opretter en 64x48 grid (liste af lister) fyldt med 0'er
    def gentag():
        liste_af_0er = []
        for tal in range(64):
            liste_af_0er.append(0)
        return liste_af_0er

    liste_af_lister = []
    for tal in range(48):
        x = gentag()
        liste_af_lister.append(x)
    return liste_af_lister


def grid_line(grid, start_coord, end_coord):
    # Tegner horisontale eller vertikale linjer (af 1-taller) i grid
    x1, y1 = start_coord
    x2, y2 = end_coord

    # Hvorfor bruge min() og max() i range?
    # For at sikre, at vi altid går fra den mindste til den største værdi,
    # uanset om start- eller slutkoordinat er størst, og at slutværdien inkluderes i loopet.

    if y1 == y2:  # Horisontal linje
        # Hvordan fungerer for x in range(...) løkken?
        # range(start, stop) genererer en sekvens af tal fra start til stop - 1,
        # og vi inkluderer slutpunktet ved at skrive stop + 1.
        for x in range(min(x1, x2), max(x1, x2) + 1):
            # Hvordan opdateres grid-celler til 1 for at tegne linjer?
            # grid[y][x] = 1 ændrer en enkelt celle i 2D-listen.
            # Når det gøres i et loop, kan man ændre mange celler på én gang og dermed tegne en linje.
            grid[y1][x] = 1

    elif x1 == x2:  # Vertikal linje
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] = 1
    else:
        raise ValueError("det er en diagonal linje")  # Kun horisontale eller vertikale linjer tilladt

    return grid


def draw_grid(screen, grid):
    block_size = 10  # Hver celle bliver tegnet som en 10x10 pixels firkant

    # Hvad er enumerate og hvordan bruges det i loop?
    # enumerate bruges til at få både indeks og element, når man gennemgår en liste.
    # Her får vi både række-nummer (y) og selve rækken (row),
    # og inde i det næste loop får vi kolonne-nummer (x) og celle-værdien (cell).
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # Farve: hvid for 0 (tomt), blå for 1 (væg/linje)
            color = (255, 255, 255) if cell == 0 else (0, 0, 255)

            # Hvorfor skriver vi pygame.Rect med stort R og ikke pygame.rect?
            # Rect er en klasse i pygame og skal kaldes med stort begyndelsesbogstav.
            # rect med lille r er et modul og kan derfor ikke kaldes som funktion.
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(screen, color, rect)


def maze(grid):
    # Ydre ramme (top, sider og bund)
    grid_line(grid, (0, 0), (63, 0))   # Top
    grid_line(grid, (0, 0), (0, 47))   # Venstre side
    grid_line(grid, (63, 0), (63, 47)) # Højre side
    grid_line(grid, (0, 47), (63, 47)) # Bund

    # Indre vægge (horisontale og vertikale)
    grid_line(grid, (10, 0), (10, 35))
    grid_line(grid, (20, 12), (40, 12))
    grid_line(grid, (40, 12), (40, 40))
    grid_line(grid, (30, 40), (50, 40))

    grid_line(grid, (15, 20), (30, 20))
    grid_line(grid, (15, 20), (15, 40))
    grid_line(grid, (25, 25), (45, 25))
    grid_line(grid, (45, 25), (45, 47))
    grid_line(grid, (50, 15), (50, 35))

    grid_line(grid, (55, 5), (55, 15))
    grid_line(grid, (35, 5), (55, 5))
    grid_line(grid, (35, 5), (35, 25))
    
    # Blokke (forhindringer inde i maze - ‘vildspor’)
    for y in range(15, 20):
        for x in range(25, 30):
            grid[y][x] = 1

    for y in range(30, 35):
        grid[y][15] = 1

    for y in range(5, 10):
        for x in range(45, 50):
            grid[y][x] = 1

    for y in range(38, 43):
        for x in range(10, 15):
            grid[y][x] = 1

    return grid


def main():
    # Korrekt brug af main-funktionen og hvor man tester funktioner i koden:
    # main() er programmets startpunkt, hvor alt samles og køres.
    # Det sikrer, at koden kun bliver kørt, når filen afvikles direkte — ikke når den importeres.
    tal_grid = grid()

    # Tegn maze ind i grid
    tal_grid = maze(tal_grid)

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Maze Visualizer")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Sort baggrund
        draw_grid(screen, tal_grid)  # Tegn grid’et (maze)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()

'''
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
         for tal in range(64):
            liste_af_0er.append(0)
         return  liste_af_0er
    x = gentag()
    liste_af_lister = []
    for tal in range(48):
        x = gentag()
        liste_af_lister.append(x)
                         
    return liste_af_lister
def grid_line(grid, start_coord, end_coord):
    x1, y1 = start_coord
    x2, y2 = end_coord
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] = 1
    elif x1==x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] = 1
    else:
         raise ValueError ("det er en dirgonal linje")        
    return grid

def draw_grid(screen, grid):
    block_size =10
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color = (255, 255, 255) if cell == 0 else (0, 0, 255)
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(screen, color, rect)



def main():
    tal_grid = grid()
    # print("Hele grid før ændring:")
    # print(tal_grid)  # Print hele grid'et, meget stort output!

    # print("\nRække 2 før ændring:")
    # print(tal_grid[2])  # Kun række 2

#top
    tal_grid = grid_line(tal_grid, (0, 0), (30, 0))
    tal_grid = grid_line(tal_grid, (32, 0), (63, 0))
#sides
    tal_grid = grid_line(tal_grid, (0, 0), (0, 47))
    tal_grid = grid_line(tal_grid, (63, 0), (63, 47))
#bunden
    tal_grid = grid_line(tal_grid, (0, 47), (30, 47))
    tal_grid = grid_line(tal_grid, (32, 47), (63, 47))




    


    # print("\nHele grid efter ændring:")
    # print(tal_grid)  # Grid med linjer sat ind

    # print("\nRække 2 efter ændring:")
    # print(tal_grid[2])  # Række 2 med linje

    print("\nKolonne 5 efter ændring:")
    print([row[5] for row in tal_grid])  # Kolonne 5 med linje

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Grid Visualizer")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # sort baggrund
        draw_grid(screen, tal_grid)  # tegn grid’et
        pygame.display.flip()

    pygame.quit()
main
'''





