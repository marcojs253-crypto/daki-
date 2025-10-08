import sys
import pygame
import math  #  Hent værktøjer udefra
from datetime import datetime


pygame.init()        # Start pygame


# HVAD: Lav et vindue
skaerm = pygame.display.set_mode((840, 680))
# HVORFOR: Vi skal have noget at tegne på


# dette er mit font, en font er en slags skrift type. jeg definere variablen. 
star_wars_font = pygame.font.Font("Starjedi.ttf", 22)
star_wars_font_lille = pygame.font.Font("Starjedi.ttf", 12)



# nu definere jeg mine variable
ur_tik =pygame.time.Clock()
centrum_x, centrum_y = 840//2, 680//2
radius = 210              # 240 - 50 i din opsætning
streg_laengde_T = 30        # hvor langt ind fra ydercirklen
streg_tykkelse_T = 6        # linjetykkelse i pixels
streg_laengde_M = 10        
streg_tykkelse_M = 1 
streg_tykkelse_Viser_sekundt = 1
streg_tykkelse_Viser_minute = 3
streg_tykkelse_Viser_time = 5
ANTAL_T = 12
ANTAL_M = 60
Antal_tal= 4
VINKEL_grad = 360 // ANTAL_T  # 30 grader
vinkel_grad_min =360 // ANTAL_M
vinkel_grad_tal = 360 // Antal_tal
off_set_radius_ydre_ring=35
off_set_radius_urskive = 1
farve_god = (255, 255, 255)
farve_ond = (0, 0, 0)
# HVAD: Gør baggrunden hvid
skaerm.fill(farve_god)

# jeg sprugte generativ AI om der var en måde at lave lysende streger i pygame, og det var dens bud
#jeg har kun brugt det i forhold til mine lyssværd
def tegn_additiv_glow(skaerm, start, slut, glow_color, thickness):
    glow_surf = pygame.Surface(skaerm.get_size(), pygame.SRCALPHA)
    # tegner lysstrålen
    pygame.draw.line(glow_surf, glow_color, start, slut, thickness)
    # additiv blending
    skaerm.blit(glow_surf, (0,0), special_flags=pygame.BLEND_ADD)
# brug af AI slut

# 4) programmet køre indtil at der sker sker en hendelse som er at lukke programmet via krydset i hjørnet og så bliver køre tilsandende falsk
kører = True
while kører:
    for hændelse in pygame.event.get():
        if hændelse.type == pygame.QUIT:
             kører = False

# da vi nu er inde i vores while loop skal den hele tiden hente tiden, så det gør vi nu via datetime.now
    nu = datetime.now()
    sekunder = nu.second
    microsekund = nu.microsecond
    minute = nu.minute
    tid_time = nu.hour
# for at gøre mit ur mere personligt har jeg valgt en nem feature som at det skal skifte udsende når man skal gå i seng, for ellers bliver man trært og sur
# og surhed føre til den mørke side af kraften

# jeg har skrevet kommentar i jedi koden til at starte med og så kopierede jeg det og lagde det her op så jeg har nogle af de samme kommentar flere gange
# men jeg har skrevet nogle nye her i sith delen
    if 22 <= tid_time or tid_time < 6:  # Sith tema fra 22:00 til 06:00

# her tegnes ur skiven og baggrunden
        pygame.draw.circle(skaerm, (0, 0, 0), (centrum_x, centrum_y), radius + off_set_radius_ydre_ring) #sort
        pygame.draw.circle(skaerm, (255,0,0), (centrum_x, centrum_y), radius) #
        pygame.draw.circle(skaerm, (255,0,0), (centrum_x, centrum_y), radius-31)
        pygame.draw.circle(skaerm, (0, 0, 0), (centrum_x, centrum_y), radius-32)
        
    

        # 3) Tegn tids indikatorerne

# her bruger vi et for loop der gentager sig selv 12 gange, så det vil sige at vi tenger timerne
# jeg syntes at det var sejere at tegne stregerne ude fra og ind så derfor har jeg både udregnet en star og slut x og y værdi
        for i in range (ANTAL_T):
            vinkel = i * VINKEL_grad
            vinkel_rad = math.radians(vinkel)  # omregn til radianer
            x_start = centrum_x + radius * math.sin(vinkel_rad)      # x-koordinat for startpunkt
            y_start = centrum_y + radius * math.cos(vinkel_rad)      # y-koordinat for startpunkt
            start_punkt = (x_start, y_start)
            x_slut = centrum_x + (radius-streg_laengde_T) * math.sin(vinkel_rad) # y-koordinat for startpunkt
            y_slut = centrum_y + (radius-streg_laengde_T) * math.cos(vinkel_rad) # y-koordinat for startpunkt
            slut_punkt = (x_slut, y_slut)
            pygame.draw.line(skaerm, (farve_ond), start_punkt, slut_punkt, streg_tykkelse_T)
# det samme gør sig gældende for timerne da da da jeg skulle også have lavet en for løkke til at tegne minutterne
        for i in range (ANTAL_M):
            vinkel = i * vinkel_grad_min
            vinkel_rad = math.radians(vinkel)  # omregn til radianer
            x_start = centrum_x + radius * math.sin(vinkel_rad)      # x-koordinat for startpunkt
            y_start = centrum_y + radius * math.cos(vinkel_rad)      # y-koordinat for startpunkt
            start_punkt = (x_start, y_start)
            x_slut = centrum_x + (radius-streg_laengde_T) * math.sin(vinkel_rad) # y-koordinat for startpunkt
            y_slut = centrum_y + (radius-streg_laengde_T) * math.cos(vinkel_rad) # y-koordinat for startpunkt
            slut_punkt = (x_slut, y_slut)
            pygame.draw.aaline(skaerm, farve_ond, start_punkt, slut_punkt, streg_tykkelse_M)    

            # Tegn talene 12, 3, 6, 9, og vi bruger star_wars_fonten så den ved at den skal skrive tallene med den font
            
        tal_liste = ["xii", "iii", "vi", "ix"]
        star_wars_font
        
        for i in range(4):
            # Beregn position for hvert tal
            if i == 0:  #hvis det er første gang at for loopet køre så tegner den et 12 tal øverst
                vinkel_rad = math.radians(0)  # 0 grader = øverst
            elif i == 1:  # 3 til højre  
                vinkel_rad = math.radians(90)  # 90 grader = højre
            elif i == 2:  # 6 nederst
                vinkel_rad = math.radians(180)  # 180 grader = nederst
            else:  # 9 til venstre
                vinkel_rad = math.radians(270)  # 270 grader = venstre
            
            # Beregn position
            x_tal = centrum_x + (radius+ off_set_radius_ydre_ring//2) * math.sin(vinkel_rad)
            y_tal = centrum_y - (radius + off_set_radius_ydre_ring//2) * math.cos(vinkel_rad)  # Minus fordi pygame y-aksen er omvendt
            
            # Lav teksten og centrer den
            tal_tekst = str(tal_liste[i]) # her tages der et tal fra listen og den laves om til en string, så den fungere som et bogstav, 
            tal_billede = star_wars_font.render(tal_tekst, True, (255,0,0))
            tal_bredde = tal_billede.get_width()
            tal_højde = tal_billede.get_height()
            
            # Placer teksten centreret på positionen
            skaerm.blit(tal_billede, (x_tal - tal_bredde//2, y_tal - tal_højde//2))
        # nulaves der et digitalt ur i midten af uret
        digital_tid_tekst = nu.strftime("%H:%M:%S")
        digital_billede =  star_wars_font_lille.render(digital_tid_tekst, True, (255, 0, 0))
        # Centrer teksten
        tekst_bredde = digital_billede.get_width()
        tekst_hoejde = digital_billede.get_height()
        skaerm.blit(digital_billede, (centrum_x - tekst_bredde//2, centrum_y - 140))
# her laver jeg en sjov lille detalje med teksten under uret, hvor man nu kan se at man skal i seng fordi man er kommet på den mørke side
        digital_tid_tekst = "sith odDER"
        digital_billede = star_wars_font.render(digital_tid_tekst, True, (255, 0, 0))
        # Centrer teksten
        tekst_bredde = digital_billede.get_width()
        tekst_hoejde = digital_billede.get_height()
        skaerm.blit(digital_billede, (centrum_x - tekst_bredde//2, centrum_y + 120))

        #sekunder
        #her bruger jeg en combination af microsekunder og sekunder for at det ligner at der er en gliende bevægelse.
        #  jeg deler dem med en halv af samme grund som minutterne ved time bliver delt med 2 
# jeg gange også sekunder timer og mitterne med en eskilerings faktor for at de bliver mindre.
        vinkel_grad_sekunder = math.radians(microsekund//100000*0.5+sekunder*6-90)       # 60 sekunder gange 6 = 360 grader
        x_min_slut = centrum_x + radius*0.7 * math.cos(vinkel_grad_sekunder)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + radius*0.7 * math.sin(vinkel_grad_sekunder)      # y-koordinat for startpunkt
        tegn_additiv_glow(skaerm, (centrum_x, centrum_y), (x_min_slut, y_min_slut), (255,0,0), streg_tykkelse_Viser_sekundt)
        x_min_slut = centrum_x + (radius*0.55)*0.2 * math.cos(vinkel_grad_sekunder)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + (radius*0.55)*0.2 * math.sin(vinkel_grad_sekunder)      # y-koordinat for startpunkt
        pygame.draw.line(skaerm, (50,50,50), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_sekundt+2)
        # nu defineres en længde som viser hvor talene skal være plaseret

        #minutter

        vinkel_grad_minute = math.radians(minute*6-90)       # 60 minutter gange 6 = 360 grader
        x_min_slut = centrum_x + radius*0.55 * math.cos(vinkel_grad_minute)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + radius*0.55 * math.sin(vinkel_grad_minute)      # y-koordinat for startpunkt
        tegn_additiv_glow(skaerm, (centrum_x, centrum_y), (x_min_slut, y_min_slut), (255,0,0), streg_tykkelse_Viser_minute)

        x_min_slut = centrum_x + (radius*0.55)*0.2 * math.cos(vinkel_grad_minute)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + (radius*0.55)*0.2 * math.sin(vinkel_grad_minute)      # y-koordinat for startpunkt
        pygame.draw.line(skaerm, (30,30,30), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_minute+2)

        #timer
        
        vinkel_grad_time = math.radians(tid_time*30+minute*0.5-90)       # 30 timer gange 30*12 = 360 grader, men der
        # bliver også lagt halvdelen af minutterne til fordi at vi gerne vil have at klokken viser hvor langt den er imellem timerne 
        x_min_slut = centrum_x + radius*0.37 * math.cos(vinkel_grad_time)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + radius*0.37 * math.sin(vinkel_grad_time)      # y-koordinat for startpunkt
        tegn_additiv_glow(skaerm, (centrum_x, centrum_y), (x_min_slut, y_min_slut), (255,0,0), streg_tykkelse_Viser_time)

        x_min_slut = centrum_x + (radius*0.55)*0.2 * math.cos(vinkel_grad_time)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + (radius*0.55)*0.2 * math.sin(vinkel_grad_time)      # y-koordinat for startpunkt
        pygame.draw.line(skaerm, (30,30,50), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_time+5)
    

        
# her tegnes cirklen der er i mitten af viserne 
        pygame.draw.circle(skaerm, (0, 0, 0), (centrum_x, centrum_y), 5)
        # sådan som jeg har forset det er hvor mange gange den opdatere per sekundt så 120
        ur_tik.tick(120)
        #det viser bare at skærmen bliver opdateret
        pygame.display.flip()
    

          # her køre uret så igen fordi at hvis klokken ikke  er mellem 22 og 6 så skal den vise at det er dag og man er en jedi  
    
    else:
        pygame.draw.circle(skaerm, (101, 67, 33), (centrum_x, centrum_y), radius + off_set_radius_ydre_ring)

        pygame.draw.circle(skaerm, (0, 0, 255), (centrum_x, centrum_y), radius+ off_set_radius_urskive)
        pygame.draw.circle(skaerm, (101, 67, 33), (centrum_x, centrum_y), radius)
        pygame.draw.circle(skaerm, (0, 0, 255), (centrum_x, centrum_y), radius-31)
        pygame.draw.circle(skaerm, (101, 67, 33), (centrum_x, centrum_y), radius-32)
 
    

        # 3) Tegn tids indikatorerne


        for i in range (ANTAL_T):
            vinkel = i * VINKEL_grad
            vinkel_rad = math.radians(vinkel)  # omregn til radianer
            x_start = centrum_x + radius * math.sin(vinkel_rad)      # x-koordinat for startpunkt
            y_start = centrum_y + radius * math.cos(vinkel_rad)      # y-koordinat for startpunkt
            start_punkt = (x_start, y_start)
            x_slut = centrum_x + (radius-streg_laengde_T) * math.sin(vinkel_rad) # y-koordinat for startpunkt
            y_slut = centrum_y + (radius-streg_laengde_T) * math.cos(vinkel_rad) # y-koordinat for startpunkt
            slut_punkt = (x_slut, y_slut)
            pygame.draw.line(skaerm, (farve_god), start_punkt, slut_punkt, streg_tykkelse_T)

        for i in range (ANTAL_M):
            vinkel = i * vinkel_grad_min
            vinkel_rad = math.radians(vinkel)  # omregn til radianer
            x_start = centrum_x + radius * math.sin(vinkel_rad)      # x-koordinat for startpunkt
            y_start = centrum_y + radius * math.cos(vinkel_rad)      # y-koordinat for startpunkt
            start_punkt = (x_start, y_start)
            x_slut = centrum_x + (radius-streg_laengde_T) * math.sin(vinkel_rad) # y-koordinat for startpunkt
            y_slut = centrum_y + (radius-streg_laengde_T) * math.cos(vinkel_rad) # y-koordinat for startpunkt
            slut_punkt = (x_slut, y_slut)
            pygame.draw.aaline(skaerm, farve_god, start_punkt, slut_punkt, streg_tykkelse_M)    

            # Tegn talene 12, 3, 6, 9
        tal_liste = ["xii", "iii", "vi", "ix"]
        star_wars_font
        
        for i in range(4):
            # Beregn position for hvert tal
            if i == 0:  #hvis det er f'rste gang at for loopet køre så tegner den et 12 tal øverst
                vinkel_rad = math.radians(0)  # 0 grader = øverst
            elif i == 1:  # 3 til højre  
                vinkel_rad = math.radians(90)  # 90 grader = højre
            elif i == 2:  # 6 nederst
                vinkel_rad = math.radians(180)  # 180 grader = nederst
            else:  # 9 til venstre
                vinkel_rad = math.radians(270)  # 270 grader = venstre
            
            # Beregn position
            x_tal = centrum_x + (radius+ off_set_radius_ydre_ring//2) * math.sin(vinkel_rad)
            y_tal = centrum_y - (radius + off_set_radius_ydre_ring//2) * math.cos(vinkel_rad)  # Minus fordi pygame y-aksen er omvendt
            
            # Lav teksten og centrer den
            tal_tekst = str(tal_liste[i]) # her tages der et tal fra listen og den laves om til en string, så den fungere som et bogstav, 
            tal_billede = star_wars_font.render(tal_tekst, True, (255, 255, 255))
            tal_bredde = tal_billede.get_width()
            tal_højde = tal_billede.get_height()
            
            # Placer teksten centreret på positionen
            skaerm.blit(tal_billede, (x_tal - tal_bredde//2, y_tal - tal_højde//2))




        nu = datetime.now()
        sekunder = nu.second
        microsekund = nu.microsecond
        minute = nu.minute
        tid_time = nu.hour


        
        digital_tid_tekst = nu.strftime("%H:%M:%S")
        digital_billede =  star_wars_font_lille.render(digital_tid_tekst, True, (255, 255, 255))
        # Centrer teksten
        tekst_bredde = digital_billede.get_width()
        tekst_hoejde = digital_billede.get_height()
        skaerm.blit(digital_billede, (centrum_x - tekst_bredde//2, centrum_y - 140))

        digital_tid_tekst = "JEDi oDDER"
        digital_billede = star_wars_font.render(digital_tid_tekst, True, (255, 255, 255))
        # Centrer teksten
        tekst_bredde = digital_billede.get_width()
        tekst_hoejde = digital_billede.get_height()
        skaerm.blit(digital_billede, (centrum_x - tekst_bredde//2, centrum_y + 120))

        #sekunder
        #her bruger jeg en combination af microsekunder og sekunder for at det ligner at der er en gliende bevægelse.
        #  jeg deler dem med en halv af samme grund som minutterne ved time bliver delt med 2 

        vinkel_grad_sekunder = math.radians(microsekund//100000*0.5+sekunder*6-90)       # 60 sekunder gange 6 = 360 grader
        x_min_slut = centrum_x + radius*0.7 * math.cos(vinkel_grad_sekunder)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + radius*0.7 * math.sin(vinkel_grad_sekunder)      # y-koordinat for startpunkt
        tegn_additiv_glow(skaerm, (centrum_x, centrum_y), (x_min_slut, y_min_slut), (115, 15, 240), streg_tykkelse_Viser_sekundt)
        x_min_slut = centrum_x + (radius*0.55)*0.2 * math.cos(vinkel_grad_sekunder)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + (radius*0.55)*0.2 * math.sin(vinkel_grad_sekunder)      # y-koordinat for startpunkt
        pygame.draw.line(skaerm, (0,0,0), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_sekundt+2)
        # nu defineres en længde som viser hvor talene skal være plaseret

        #minutter

        vinkel_grad_minute = math.radians(minute*6-90)       # 60 sekunder gange 6 = 360 grader
        x_min_slut = centrum_x + radius*0.55 * math.cos(vinkel_grad_minute)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + radius*0.55 * math.sin(vinkel_grad_minute)      # y-koordinat for startpunkt
        tegn_additiv_glow(skaerm, (centrum_x, centrum_y), (x_min_slut, y_min_slut), (0,140,255), streg_tykkelse_Viser_minute)

        x_min_slut = centrum_x + (radius*0.55)*0.2 * math.cos(vinkel_grad_minute)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + (radius*0.55)*0.2 * math.sin(vinkel_grad_minute)      # y-koordinat for startpunkt
        pygame.draw.line(skaerm, (0,0,0), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_minute+2)

        #timer
        
        vinkel_grad_time = math.radians(tid_time*30+minute*0.5-90)       # 60 sekunder gange 6 = 360 grader
        x_min_slut = centrum_x + radius*0.37 * math.cos(vinkel_grad_time)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + radius*0.37 * math.sin(vinkel_grad_time)      # y-koordinat for startpunkt
        tegn_additiv_glow(skaerm, (centrum_x, centrum_y), (x_min_slut, y_min_slut), (0,255,140), streg_tykkelse_Viser_time)

        x_min_slut = centrum_x + (radius*0.55)*0.2 * math.cos(vinkel_grad_time)      # x-koordinat for startpunkt
        y_min_slut = centrum_y + (radius*0.55)*0.2 * math.sin(vinkel_grad_time)      # y-koordinat for startpunkt
        pygame.draw.line(skaerm, (0,0,0), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_time+5)
       

   

        pygame.draw.circle(skaerm, (255, 255, 255), (centrum_x, centrum_y), 5)
        ur_tik.tick(120)
        pygame.display.flip()
    
          
