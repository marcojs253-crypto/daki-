import random
import pygame
from opensimplex import OpenSimplex
from queue import PriorityQueue
import time  # til animation

screen_size = [1000, 800]
felt_størrelse = 10


class Kort:
    def __init__(self, screen):
        self.screen = screen
        self.seed = 0
        self.felt_data = []

    def definere_kortet(self, seed):
        self.felt_data = []
        gen = OpenSimplex(seed)
        for y in range(screen_size[1] // felt_størrelse):
            række_for_x_værdierne = []
            for x in range(screen_size[0] // felt_størrelse):
                v = gen.noise2(x * 0.075, y * 0.075)
                if v < -0.5:
                    felt_dictionary = {'bevægels_pris': 3, 'farve': (0, 0, 180), 'felt_koordinat': (x, y)}
                elif v < 0.3:
                    felt_dictionary = {'bevægels_pris': 1, 'farve': (51, 255, 51), 'felt_koordinat': (x, y)}
                elif v <= 0.75:
                    felt_dictionary = {'bevægels_pris': 5, 'farve': (64, 64, 64), 'felt_koordinat': (x, y)}
                else:
                    felt_dictionary = {'bevægels_pris': 1000, 'farve': (255, 70, 0), 'felt_koordinat': (x, y)}
                række_for_x_værdierne.append(felt_dictionary)
            self.felt_data.append(række_for_x_værdierne)

    def tegn_kortet(self):
        for y in range(screen_size[1] // felt_størrelse):
            for x in range(screen_size[0] // felt_størrelse):
                farve = self.felt_data[y][x]['farve']
                rect = (x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse)
                pygame.draw.rect(self.screen, farve, rect)


class CirkelerPåKortet(Kort):
    @staticmethod
    def registre_klik(event, liste_af_højre__klik, liste_af_venstre__klik):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                liste_af_højre__klik = [pygame.mouse.get_pos()]
            if event.button == 1:
                liste_af_venstre__klik = [pygame.mouse.get_pos()]
        return liste_af_højre__klik, liste_af_venstre__klik

    @staticmethod
    def tegn_cirkel(screen, liste_af_højre__klik, liste_af_venstre__klik):
        if liste_af_højre__klik:
            pygame.draw.circle(screen, (158, 115, 178), liste_af_højre__klik[-1], felt_størrelse // 2)
        if liste_af_venstre__klik:
            pygame.draw.circle(screen, (255, 255, 255), liste_af_venstre__klik[-1], felt_størrelse // 2)


def randomisere_seed(event, kort, seed, liste_af_højre__klik, liste_af_venstre__klik, total_terræn_bevægelse_pris):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            seed = random.randint(1, 100)
            liste_af_højre__klik = []
            liste_af_venstre__klik = []
            total_terræn_bevægelse_pris = 0
            kort.definere_kortet(seed)
    return seed, liste_af_højre__klik, liste_af_venstre__klik, total_terræn_bevægelse_pris


class AStar:
    @staticmethod
    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    @staticmethod
    def find_naboer(kort, nuvarande_position):
        nuvarande_x, nuvarande_y = nuvarande_position
        nabo_liste = []
        mulige_veje = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for dx, dy in mulige_veje:
            nx, ny = nuvarande_x + dx, nuvarande_y + dy
            if 0 <= nx < (screen_size[0] // felt_størrelse) and 0 <= ny < (screen_size[1] // felt_størrelse):
                nabo_liste.append((nx, ny))
        return nabo_liste

    @staticmethod
    def terræn_bevægelse_pris(kort, position):
        x, y = position
        return kort.felt_data[y][x]['bevægels_pris']

    @staticmethod
    def Algoritmen_rute_beringer(kort, start, målet):
        uudforskede_positioner  = PriorityQueue()
        uudforskede_positioner .put((0, start))
        hvor_man_kom_fra = {start: None}
        terræn_bevægelse_pris_so_far = {start: 0}

        while not uudforskede_positioner .empty():
            _, nuværende_position  = uudforskede_positioner .get()
            if nuværende_position  == målet:
                break
            for next_pos in AStar.find_naboer(kort, nuværende_position ):
                new_terræn_bevægelse_pris = terræn_bevægelse_pris_so_far[nuværende_position ] + AStar.terræn_bevægelse_pris(kort, next_pos)
                if next_pos not in terræn_bevægelse_pris_so_far or new_terræn_bevægelse_pris < terræn_bevægelse_pris_so_far[next_pos]:
                    terræn_bevægelse_pris_so_far[next_pos] = new_terræn_bevægelse_pris
                    estimeret_total_pris = new_terræn_bevægelse_pris + AStar.heuristic(målet, next_pos)
                    uudforskede_positioner .put((estimeret_total_pris, next_pos))
                    hvor_man_kom_fra[next_pos] = nuværende_position 
        return hvor_man_kom_fra, terræn_bevægelse_pris_so_far

######################chat gpt#######################
# Animation og felt-tælling
def tegn_algoritme_sti_animated(screen, hvor_man_kom_fra, start, målet, kort):
    nuværende_position  = målet
    tæller = {'hav': 0, 'græs': 0, 'bjerg': 0, 'lava': 0}
    while nuværende_position  != start:
        x, y = nuværende_position 
        pris = kort.felt_data[y][x]['bevægels_pris']
        if pris == 3:
            tæller['hav'] += 1
        elif pris == 1:
            tæller['græs'] += 1
        elif pris == 5:
            tæller['bjerg'] += 1
        else:
            tæller['lava'] += 1

        pygame.draw.rect(screen, (0, 0, 0), (x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse))
        pygame.display.flip()
        time.sleep(0.01)
        nuværende_position  = hvor_man_kom_fra[nuværende_position ]
    return tæller


def vis_felt_tælling(screen, tæller):
    font = pygame.font.Font(None, 24)
    tekst = f"Hav: {tæller['hav']}  Græs: {tæller['græs']}  Bjerg: {tæller['bjerg']}  Lava: {tæller['lava']}"
    billede = font.render(tekst, True, (0, 0, 0))
    screen.blit(billede, (10, 40))
#####################################

def tegn_total_pris(screen, total_terræn_bevægelse_pris):
    font = pygame.font.Font(None, 32)
    tekst = font.render(f"Pris for ruten: {total_terræn_bevægelse_pris}", True, (0, 0, 0))
    screen.blit(tekst, (screen_size[0] - tekst.get_width() - 10, 10))


def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
    pygame.display.set_caption("kort_spillet")
    seed = 0

    liste_af_venstre__klik = []
    liste_af_højre__klik = []
    kort = Kort(screen)
    kort.definere_kortet(seed)
    total_terræn_bevægelse_pris = 0

    while True:
        screen.fill((255, 255, 255))
        kort.tegn_kortet()

        for event in pygame.event.get():
            seed, liste_af_højre__klik, liste_af_venstre__klik, total_terræn_bevægelse_pris = randomisere_seed(
                event, kort, seed, liste_af_højre__klik, liste_af_venstre__klik, total_terræn_bevægelse_pris
            )
            liste_af_højre__klik, liste_af_venstre__klik = CirkelerPåKortet.registre_klik(
                event, liste_af_højre__klik, liste_af_venstre__klik
            )
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if liste_af_højre__klik and liste_af_venstre__klik:
            start_postion = liste_af_venstre__klik[-1]
            slut_postion = liste_af_højre__klik[-1]
            start = (start_postion[0] // felt_størrelse, start_postion[1] // felt_størrelse)
            slut = (slut_postion[0] // felt_størrelse, slut_postion[1] // felt_størrelse)

            hvor_man_kom_fra, terræn_bevægelse_pris_so_far = AStar.Algoritmen_rute_beringer(kort, start, slut)
            total_terræn_bevægelse_pris = terræn_bevægelse_pris_so_far[slut]

            tæller = tegn_algoritme_sti_animated(screen, hvor_man_kom_fra, start, slut, kort)
            vis_felt_tælling(screen, tæller)

        tegn_total_pris(screen, total_terræn_bevægelse_pris)
        CirkelerPåKortet.tegn_cirkel(screen, liste_af_højre__klik, liste_af_venstre__klik)

        pygame.display.flip()


if __name__ == '__main__':
    main()
