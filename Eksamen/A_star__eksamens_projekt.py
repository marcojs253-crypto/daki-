import random
import pygame
from opensimplex import OpenSimplex
from queue import PriorityQueue


#globalt scope så man hurtigt og nemt kan ændre skærm størrelse og felt størrelse
screen_size = [1400, 800]
felt_størrelse = 20


class Kort :
    def __init__(self, screen):
        self.screen = screen
        self.seed = 0
        self.felt_data = []   # 2D liste med alle felter

     
    def definere_kortet(self, seed):
        # Initialiserer OpenSimplex-generatoren med det ønskede seed
        gen = OpenSimplex(seed)
        for y in range(screen_size[1] // felt_størrelse):
            række_for_x_værdierne = []
            for x in range(screen_size[0] // felt_størrelse):
                 # noise2() giver et tal mellem -1 og 1
                v = gen.noise2(x * 0.075, y * 0.075) #højere værdi(OCTAV) mere ugroperet---Expressions
                if v < -0.6:
                    felt_dictionary = {
                        'type': 'hav',
                        'bevægels_pris': 14,
                        'farve': (10, 10, 180),
                        'felt_koordinat': (x, y)
                    }
                elif v < -0.4:
                    felt_dictionary = {
                        'type': 'hav',
                        'bevægels_pris': 14,
                        'farve': (0, 0, 220),
                        'felt_koordinat': (x, y)
                    }
                elif v < 0.2:
                    felt_dictionary = {
                        'type': 'græs',
                        'bevægels_pris': 10,
                        'farve': (51, 255, 51),
                        'felt_koordinat': (x, y)
                    }
                elif v <= 0.72:
                    felt_dictionary = {
                        'type': 'bjerg',
                        'bevægels_pris': 15,
                        'farve': (70, 70, 60),
                        'felt_koordinat': (x, y)}
                elif v <= 0.76:
                    felt_dictionary = {
                        'type': 'bjerg',
                        'bevægels_pris': 15,
                        'farve': (35, 35, 30),
                        'felt_koordinat': (x, y)
                    }
                else:
                    felt_dictionary = {
                        'type': 'lava',
                        'bevægels_pris': 1000,
                        'farve': (255, 70, 0),
                        'felt_koordinat': (x, y)
                    }            
                række_for_x_værdierne.append(felt_dictionary)
            self.felt_data.append(række_for_x_værdierne)

    # Denne metode tegner kortet på skærmen baseret på felt_data, for at ungå side efekts.
    def tegn_kortet(self,screen):
            for y in range(screen_size[1] // felt_størrelse):
                for x in range(screen_size[0] // felt_størrelse):
                    farve = self.felt_data[y][x]['farve']
                    rect = (x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse)
                    pygame.draw.rect(screen, farve, rect)
                    #void retunere = ingenting, tenger kun

class cirkeler_på_kortet(Kort):#supclass
    def __init__(self, screen):
         # Kalder parent-klassens (Kort) __init__ metode, så vi får alle Kort's attributter
        super().__init__(screen)
        # Tilføj ekstra attributter som kun denne klasse har
        self.liste_af_højre__klik = []
        self.liste_af_venstre__klik = []


    def registre_klik(self,event ):
        
         # Tjek om det var et museklik
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                self.liste_af_højre__klik=[pygame.mouse.get_pos()]
            if event.button == 1:
                self.liste_af_venstre__klik=[pygame.mouse.get_pos()]

            
        

    def tegn_cirkel(self, screen):
         # Tjek om der er et højreklik gemt og at listen ikke er tom
        if self.liste_af_højre__klik and len(self.liste_af_højre__klik) > 0:
            # Konverter pixel-koordinater til grid-koordinater
            mus_x, mus_y = self.liste_af_højre__klik[-1]
            grid_x = mus_x // felt_størrelse
            grid_y = mus_y // felt_størrelse
            rect = ( grid_x * felt_størrelse, grid_y * felt_størrelse, felt_størrelse, felt_størrelse)
            pygame.draw.rect(screen, (158, 115, 178), rect)
        if self.liste_af_venstre__klik and len(self.liste_af_venstre__klik) > 0:
            mus_x, mus_y = self.liste_af_venstre__klik[-1]
            grid_x = mus_x // felt_størrelse
            grid_y = mus_y // felt_størrelse
            rect = ( grid_x * felt_størrelse, grid_y * felt_størrelse, felt_størrelse, felt_størrelse)
            pygame.draw.rect(screen, (255, 255, 255), rect)



def nutstil_kortet(event, seed, kort, cirkler, hvor_man_kom_fra, start, slut, total_terræn_bevægelse_pris):
      #funktion til at randomisere seed og nulstille variabler via mellemrumstasten,
    # så kortet kan tegnes på ny, og spilleren kan vælge nye start og slut
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            seed = random.randint(1, 100)
            cirkler.liste_af_højre__klik = []
            cirkler.liste_af_venstre__klik = []
            total_terræn_bevægelse_pris = 0
            kort.felt_data = []         
            kort.definere_kortet(seed)
            # opdatere stien så 
            hvor_man_kom_fra = None
            start = None
            slut = None

    return seed, hvor_man_kom_fra, start, slut, cirkler.liste_af_højre__klik, cirkler.liste_af_venstre__klik, total_terræn_bevægelse_pris


class A_star:
    # Denne klasse får kun kortets reference - den skal bruge det til at kigge på terræn-priser
    def __init__(self, kort):
        self.kort = kort
        self.terræn_tæller = { 
            'hav': 0,
            'græs': 0,
            'bjerg': 0,
            'lava': 0}
        self.terræn_typer_i_stien = set()
    def heuristik(self, a, b):   
        dx = abs(a[0] - b[0])
        dy = abs(a[1] - b[1])
        return max(dx, dy) + (1.414 - 1) * min(dx, dy)#--------- fejl -----Octile distances
        

    def find_naboer(self,nuvarande_position):
         # Pak positionen ud
        nuvarande_x, nuvarande_y = nuvarande_position
        nabo_liste  = [] 
        retning_for_naboer_liste=[]
        mulige_veje= [(-1,1),   (0,1),   (1,1),
                    (-1,0),            (1,0),
                    (-1,-1),  (0,-1),  (1,-1)]
        
        # for loop der går gennem hver mulig retning
        for forskydning_x, forskydning_y in mulige_veje:
            # Beregn naboens position
            nabo_x = nuvarande_x + forskydning_x
            nabo_y = nuvarande_y + forskydning_y
            # finder retningen ved at trække nuværende position fra nabo positionen
            retning = (nabo_x-nuvarande_x, nabo_y-nuvarande_y)
        # Tjekker er nabo_x mellem 0 og bredden og  nabo_y mellem 0 og højden og så tilføjer vi dem der er 
            if 0<= nabo_x <(screen_size[0] // felt_størrelse) and 0<= nabo_y <(screen_size[1] // felt_størrelse):
                nabo_liste.append((nabo_x, nabo_y))
                retning_for_naboer_liste.append(retning)
        return nabo_liste,retning_for_naboer_liste
    
    def er_dirgonal(self,retning):
        skrå_veje = [(1,1),
                    (-1,1),
                    (-1,-1),
                    (1,-1)]
        if retning in skrå_veje:
            return True
        else:
            return False

    def terræn_bevægelse_pris(self, næste_position, retning):
        x, y  = næste_position
        pris = self.kort.felt_data[y][x]['bevægels_pris']
        
        if self.er_dirgonal(retning): # Tjekker om er_dirgonal returener True
             # Hvis ja, gang pris med kvadratroden af 2 (ca. 1.414) 
           pris *= 1.414 
        return pris
        

    def  Algoritmen_rute_beringer(self, start, målet):
         # Priority queue: holder steder vi skal besøge, sorteret efter laveste pris i en tuple (pris, position) som en kø
        uudforskede_positioner  = PriorityQueue()
        # Tilføj startpunktet til køen med pris 0
        uudforskede_positioner.put((0, start))
        # Dictionary der holder styr på hvor vi kom fra
        # Key = position, Value = forrige position
        hvor_man_kom_fra_dict = dict()
        # Dictionary der holder styr på den billigste pris til hver position
        # Key = position, Value = billigste pris hidtil
        bevægelse_pris_hidtil_dict = dict()
        # Start positionens har ingen forrige position og pris 0
        hvor_man_kom_fra_dict[start] = None
        bevægelse_pris_hidtil_dict[start] = 0

        # Så længe der er positioner at undersøge, skal vi fortsætte
        while not uudforskede_positioner.empty():
            # Hent den position med LAVESTE estimerede total pris
            # PriorityQueue giver os automatisk den billigste først
            estimeret_total_pris, nuværende_position  = uudforskede_positioner.get()
            if nuværende_position  == målet:
                break
            # Find alle naboer og retninger til den nuværende position
            naboer_liste, retninger_liste = self.find_naboer(nuværende_position )

            # Gå gennem hver nabo og dens retning, zip bruges til at parre dem sammen
            for næste_nabo,retning in zip(naboer_liste,retninger_liste): 
                # her finder man den nye pris ved at tage prisen for den nuværnde position
                # og lægge prisen for at gå til den næste nabo
                ny_terræn_bevægelse_pris = bevægelse_pris_hidtil_dict[nuværende_position ] + self.terræn_bevægelse_pris(næste_nabo, retning)
                # hvis næste_babo ikke har været der før eller den nye pris er billigere, så sker denne branching
                if næste_nabo not in bevægelse_pris_hidtil_dict or ny_terræn_bevægelse_pris < bevægelse_pris_hidtil_dict[næste_nabo]:
                    # gemmer nye billigste pris til næste_nabo
                    bevægelse_pris_hidtil_dict[næste_nabo] = ny_terræn_bevægelse_pris
                    # Beregn den estimerede total pris = ny pris + gæt
                    estimeret_total_pris = ny_terræn_bevægelse_pris + self.heuristik(målet, næste_nabo)
                    # Tilføj naboen til køen med dens estimerede total pris
                    uudforskede_positioner.put((estimeret_total_pris, næste_nabo))
                    # Opdater hvor vi kom fra så det indkludere næste_nabo
                    hvor_man_kom_fra_dict[næste_nabo] = nuværende_position 

        return hvor_man_kom_fra_dict, bevægelse_pris_hidtil_dict


    def tegn_algoritme_sti(self,screen, hvor_man_kom_fra, start, målet):
        # går baglends og tegner stien fra målet til start
        if hvor_man_kom_fra is None or start is None or målet is None:
            return  # Tegn ikke noget hvis ingen sti
        nuværende_position  = målet
        while nuværende_position  != start:
            x, y = nuværende_position 
            pygame.draw.rect(screen, (0, 0, 0),(x * felt_størrelse, y * felt_størrelse, felt_størrelse, felt_størrelse))
            #pga hvor_man_kom_fra er en dictionary bruges at finde den forrige position,
            # da det er value for key nuværende_position
            nuværende_position  = hvor_man_kom_fra[nuværende_position ]
            

    
    
    def tegn_pris (self, screen, total_terræn_bevægelse_pris,):
        # Skrifttype = størrelse 42
        font = pygame.font.Font(None, 42)
        
        # Lav teksten og .1f = 1 decimal)
        tekst = font.render(f"Pris for ruten: {total_terræn_bevægelse_pris:.1f}", True, (0, 0, 0))
        pris_bredde = tekst.get_width()
        # screen_size[0] = 1000 (højre kant), minus bredde, minus 10 pixels margin
        screen.blit(tekst, (screen_size[0] - pris_bredde - 10, 10))
            
    def definere_terræn_tælling(self, hvor_man_kom_fra=None, start=None, målet=None): #default parameters 
        self.terræn_tæller = {
                'hav': 0,
                'græs': 0,
                'bjerg': 0,
                'lava': 0
            }
             # Set til at gemme hvilke typer vi møder.
             # et set kan kun indeholde hver værdi ÉN gang
        self.terræn_typer_i_stien = set()  # Tom mængde
        if hvor_man_kom_fra is not None and start is not None and målet is not None:

            nuværende_position = målet
            while nuværende_position != start:
                x, y = nuværende_position
                terræn_type = self.kort.felt_data[y][x]['type']
                #ligger 1 til dictionaryet for den fundne terræn type
                self.terræn_tæller[terræn_type] += 1
                self.terræn_typer_i_stien.add(terræn_type)  # ← Tilføj type til set
                nuværende_position = hvor_man_kom_fra[nuværende_position]
        return self.terræn_tæller, self.terræn_typer_i_stien
    
    def tegn_sum_af_terræn (self, screen,terræn_typer_i_stien):
        font = pygame.font.Font(None, 42)
        # unikt for sets = man kan tilføje n antal af x og y
        # men længden forbliver 2 (x og y)
        antal_typer = len(terræn_typer_i_stien)
        stat_tekst = font.render(f"Terræn-typer: {antal_typer}", True, (0, 0, 0))
        stat_bredde = stat_tekst.get_width()
        screen.blit(stat_tekst, (screen_size[0] - stat_bredde - 10, 60))
    def tegn_terræn_antal(self, screen,terræn_tæller):
        font = pygame.font.Font(None, 42) 
        #hvor langt nede teksten skal tegnes
        y_offset = 100
        #.items() er en metode der konverterer en dictionary til en liste af (key, value) par.
        # så her går loopet gennem hvert key (terræn) og value(antal) i listen
        for terræn, antal in terræn_tæller.items():
            # hvis der mere 0 af en terræn type, så tegnes den
            if antal > 0:
                stat_tekst = font.render(f"{terræn}: {antal}", True, (0, 0, 0))
                stat_bredde = stat_tekst.get_width()
                screen.blit(stat_tekst, (screen_size[0] - stat_bredde - 10, y_offset))
                # opdater y_offset så næste tekst tegnes under den forrige
                y_offset += 40
    def tegn_info(self, screen, total_terræn_bevægelse_pris, hvor_man_kom_fra=None, start=None, målet=None):

       self.terræn_tæller, self.terræn_typer_i_stien = self.definere_terræn_tælling(hvor_man_kom_fra, start, målet)

       self.tegn_terræn_antal(screen,self.terræn_tæller)
       self.tegn_pris(screen, total_terræn_bevægelse_pris)
       self.tegn_sum_af_terræn(screen, self.terræn_typer_i_stien)    


        
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
    pygame.display.set_caption("kort_spillet")
    seed = 0
    total_terræn_bevægelse_pris= 0

    # Initialiser kort, cirkeler og A* algoritme
    kort = Kort(screen)
    Cirkeler = cirkeler_på_kortet(screen)
    vejviser = A_star(kort)
    # tegn kort én gang
    kort.definere_kortet(seed)
    hvor_man_kom_fra = None
    start = None
    slut = None
    
    while True:
        kort.tegn_kortet(screen)
        # Tjek om brugeren har klikket BÅDE højre OG venstre (= valgt start OG slut)
        if len(Cirkeler.liste_af_højre__klik)>0 and len(Cirkeler.liste_af_venstre__klik) > 0:
            start_postion=Cirkeler.liste_af_venstre__klik[-1]
            slut_postion=Cirkeler.liste_af_højre__klik[-1]
            start = (start_postion[0]//felt_størrelse, start_postion[1]//felt_størrelse)
            slut = (slut_postion[0]//felt_størrelse, slut_postion[1]//felt_størrelse)
            hvor_man_kom_fra, terræn_bevægelse_pris_so_far = vejviser.Algoritmen_rute_beringer(start, slut)
            total_terræn_bevægelse_pris = terræn_bevægelse_pris_so_far[slut]
            vejviser.tegn_algoritme_sti(screen, hvor_man_kom_fra, start, slut)

        vejviser.tegn_info(screen, total_terræn_bevægelse_pris, hvor_man_kom_fra, start, slut)
        Cirkeler.tegn_cirkel(screen,)
        pygame.display.flip()
        for event in pygame.event.get():            
            seed, hvor_man_kom_fra, start, slut, Cirkeler.liste_af_højre__klik, Cirkeler.liste_af_venstre__klik, total_terræn_bevægelse_pris = (
             nutstil_kortet(event, seed, kort, Cirkeler,hvor_man_kom_fra, start, slut, total_terræn_bevægelse_pris))
                
            
            Cirkeler.registre_klik(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  

if __name__ == '__main__':
    main()
