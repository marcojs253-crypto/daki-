import random
import pygame
from opensimplex import OpenSimplex

from queue import PriorityQueue

screen_size = [1000, 800]
felt_størrelse = 10


class Kort :
    def __init__(self, screen):
        self.screen = screen
        self.seed = 0
        self.felt_data = []   # 2D liste med alle felter
        


        ####################################
    def definere_kortet(self, seed):
        # Initialiserer OpenSimplex-generatoren med det ønskede seed
        gen = OpenSimplex(seed)
        for y in range(screen_size[1] // felt_størrelse):
            række_for_x_værdierne = []
            for x in range(screen_size[0] // felt_størrelse):
                 # Beregner en støj-værdi for dette felt, så landskabet bliver varieret men kontinuerligt 
                v = gen.noise2(x * 0.08, y * 0.08) #højere værdi mere ugroperet
                if v < -0.5:
                    felt_dictionary = {
                        # type = hav
                        'bevægels_pris': 3,
                        'farve': (0, 0, 180),
                        'felt_koordinat': (x, y)
                    }
                elif v < 0.3:
                    felt_dictionary = {
                        # type = græs
                        'bevægels_pris': 1,
                        'farve': (51, 255, 51),
                        'felt_koordinat': (x, y)
                    }
                elif v <= 0.75:
                    felt_dictionary = {
                        # type = bjerg
                        'bevægels_pris': 5,
                        'farve': (64, 64, 64),
                        'felt_koordinat': (x, y)
                    }
                else:
                    felt_dictionary = {
                        # type = lava
                        'bevægels_pris': 1000,
                        'farve': (255, 70, 0),
                        'felt_koordinat': (x, y)
                    }            
                række_for_x_værdierne.append(felt_dictionary)
            self.felt_data.append(række_for_x_værdierne)

    # laver ny funktion for at ungå side efekts.
    def tegn_kortet(self,screen):
            for y in range(screen_size[1] // felt_størrelse):
                for x in range(screen_size[0] // felt_størrelse):
                    farve = self.felt_data[y][x]['farve']
                    rect = (x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse)
                    pygame.draw.rect(screen, farve, rect)

class cirkeler_på_kortet(Kort):#supclass
    def __init__(self, screen):
        super().__init__(screen)
    def registre_klik(event, liste_af_højre__klik, liste_af_venstre__klik):
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            if event.button == 3:
                liste_af_højre__klik=[pygame.mouse.get_pos()]

            if event.button == 1:
                liste_af_venstre__klik=[pygame.mouse.get_pos()]

            
        return liste_af_højre__klik, liste_af_venstre__klik

    def tegn_cirkel(screen, liste_af_højre__klik, liste_af_venstre__klik):
        if liste_af_højre__klik and len(liste_af_højre__klik) > 0:
            pygame.draw.circle(screen, (158, 115, 178), liste_af_højre__klik[-1], felt_størrelse // 2)
        if liste_af_venstre__klik and len(liste_af_venstre__klik) > 0:
            pygame.draw.circle(screen, (255, 255, 255), liste_af_venstre__klik[-1], felt_størrelse // 2)



def randomisere_seed(event, kort, seed, liste_af_højre__klik, liste_af_venstre__klik, total_terræn_bevægelse_pris):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            seed = random.randint(1, 100)
            liste_af_højre__klik = []
            liste_af_venstre__klik = []
            total_terræn_bevægelse_pris = 0
            kort.felt_data = []          # <-- ryd tidligere kort
            kort.definere_kortet(seed)
    return seed, liste_af_højre__klik, liste_af_venstre__klik, total_terræn_bevægelse_pris

class A_star:
    def __init__(self, nuvarande_position, nabo_liste, pris, totaal_pris, hvor_man_kom_fra, terræn_bevægelse_pris_so_far):
        self.nuværende_position= nuvarande_position
        self.nabo_liste = nabo_liste
        self.pris = pris
        self.totaal_pris = totaal_pris
        self.hvor_man_kom_fra = hvor_man_kom_fra
        self.terræn_bevægelse_pris_so_far = terræn_bevægelse_pris_so_far

    def heuristic(a, b):     
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)
        

    def neighbors(kort,nuvarande_position):
        nuvarande_x, nuvarande_y = nuvarande_position
        nabo_liste  = []
        retning_liste=[]
        mulige_veje= [(-1,1),   (0,1),   (1,1),
                    (-1,0),            (1,0),
                    (-1,-1),  (0,-1),  (1,-1)]
        
        # laver en løkke der tjekke alle retningeer
        for forskydning_x, forskydning_y in mulige_veje:
            nabo_x,nabo_y = nuvarande_x + forskydning_x, nuvarande_y + forskydning_y
            retning = (nuvarande_x-nabo_x, nuvarande_y- nabo_y)
        #Vi tjekker er nabo_x mellem 0 og bredden og  nabo_y mellem 0 og højden og så tilføjer vi dem der er 
            if 0<= nabo_x <(screen_size[0] // felt_størrelse) and 0<= nabo_y <(screen_size[1] // felt_størrelse):
                nabo_liste.append((nabo_x, nabo_y))
                retning_liste.append(retning)
        return nabo_liste,retning_liste
    
    def er_dirgonal(retning):
        skrå_veje = [(1,1),
                    (-1,1),
                    (-1,-1),
                    (1,-1)]
        if retning in skrå_veje:
            return True
        else:
            return False

    def terræn_bevægelse_pris(kort,næste_position,retning):
        x,y  = næste_position
        pris = kort.felt_data[y][x]['bevægels_pris']
        if A_star.er_dirgonal(retning):
           pris *= 1.414 
        return pris
        

    def  Algoritmen_rute_beringer(kort,start, målet):
         # Priority queue: holder steder vi skal besøge, sorteret efter laveste pris
        uudforskede_positioner  = PriorityQueue()
        uudforskede_positioner .put((0, start))
        hvor_man_kom_fra = dict()
        terræn_bevægelse_pris_so_far = dict()
        hvor_man_kom_fra[start] = None
        terræn_bevægelse_pris_so_far[start] = 0

        while not uudforskede_positioner .empty():
            estimeret_total_pris, nuværende_position  = uudforskede_positioner.get()
            if nuværende_position  == målet:
                break
            naboer,retninger = A_star.neighbors(kort, nuværende_position )
            
            for næste_nabo,retning in zip(naboer,retninger): 
                new_terræn_bevægelse_pris = terræn_bevægelse_pris_so_far[nuværende_position ] + A_star.terræn_bevægelse_pris(kort, næste_nabo, retning)
                if næste_nabo not in terræn_bevægelse_pris_so_far or new_terræn_bevægelse_pris < terræn_bevægelse_pris_so_far[næste_nabo]:
                    terræn_bevægelse_pris_so_far[næste_nabo] = new_terræn_bevægelse_pris
                    estimeret_total_pris = new_terræn_bevægelse_pris + A_star.heuristic(målet, næste_nabo)
                    uudforskede_positioner .put((estimeret_total_pris, næste_nabo))
                    hvor_man_kom_fra[næste_nabo] = nuværende_position 
        return hvor_man_kom_fra, terræn_bevægelse_pris_so_far


    def tegn_algoritme_sti(screen, hvor_man_kom_fra, start, målet):
        nuværende_position  = målet
        # 2. Gå baglæns gennem hvor_man_kom_fra og tegn felter
        while nuværende_position  != start:
            x, y = nuværende_position 
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse)
            )
            nuværende_position  = hvor_man_kom_fra[nuværende_position ]


        if len(hvor_man_kom_fra) == 0 or målet not in hvor_man_kom_fra:
            return#det er måde man kan gå ud af en funktion hvis en betingelse er opfyldt
        nuværende_position  = målet
        while nuværende_position  != start:
            x, y = nuværende_position 
            pygame.draw.rect(screen, (0, 0, 0), (x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse))
            nuværende_position  = hvor_man_kom_fra.get(nuværende_position )


    def tegn_total_pris(screen, total_terræn_bevægelse_pris):
        font = pygame.font.Font(None, 42)
        tekst = font.render(f"Pris for ruten: {total_terræn_bevægelse_pris:.1f}", True, (255, 255, 255))
        pris_bredde = tekst.get_width()
        screen.blit(tekst, (screen_size[0] - pris_bredde - 10, 10))
        
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
    pygame.display.set_caption("kort_spillet")
    seed = 0

    liste_af_venstre__klik = []
    liste_af_højre__klik = []
    kort = Kort(screen)
    # tegn kort én gang
    kort.definere_kortet(seed)
    # global total_terræn_bevægelse_pris
    total_terræn_bevægelse_pris= 0
    
    while True:

        
        kort.tegn_kortet(screen)
        if len(liste_af_højre__klik)>0 and len(liste_af_venstre__klik) > 0:
            start_postion=liste_af_venstre__klik[-1]
            slut_postion=liste_af_højre__klik[-1]
            start = (start_postion[0]//felt_størrelse, start_postion[1]//felt_størrelse)
            slut = (slut_postion[0]//felt_størrelse, slut_postion[1]//felt_størrelse)
            hvor_man_kom_fra, terræn_bevægelse_pris_so_far = A_star.Algoritmen_rute_beringer(kort,start, slut)
            total_terræn_bevægelse_pris = terræn_bevægelse_pris_so_far[slut]

            A_star.tegn_algoritme_sti(screen, hvor_man_kom_fra, start, slut)
        A_star.tegn_total_pris (screen,total_terræn_bevægelse_pris)
        cirkeler_på_kortet.tegn_cirkel(screen, liste_af_højre__klik, liste_af_venstre__klik)
        pygame.display.flip()
        for event in pygame.event.get():
            
            
            seed, liste_af_højre__klik, liste_af_venstre__klik,total_terræn_bevægelse_pris =(
            randomisere_seed(event,kort, seed, liste_af_højre__klik, liste_af_venstre__klik,total_terræn_bevægelse_pris))
            

            liste_af_højre__klik, liste_af_venstre__klik = cirkeler_på_kortet.registre_klik(event, liste_af_højre__klik, liste_af_venstre__klik)

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        
        
    
if __name__ == '__main__':
    main()


