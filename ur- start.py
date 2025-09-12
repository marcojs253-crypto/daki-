import pygame, math  # HVAD: Hent værktøjer udefra
                     # HVORFOR: Vi skal bruge vindue/grafik og cos/sin

pygame.init()        # HVAD: Start pygame
                     # HVORFOR: Skal gøres før pygame virker

# HVAD: Lav et vindue
skaerm = pygame.display.set_mode((640, 480))
# HVORFOR: Vi skal have noget at tegne på

# HVAD: Gør baggrunden hvid
skaerm.fill((255, 255, 255))
# HVORFOR: Så vi kan se vores sorte streger

# HVAD: Bestem hvor urets centrum skal være
centrum_x = 320  # VI bestemmer dette tal (midten af 640)
centrum_y = 240  # VI bestemmer dette tal (midten af 480)

# HVAD: Beregn radius (afstand fra centrum til kant)
radius = 240 - 50  # VI beregner: 190
# HVORFOR: Fordi vores første punkt var (320, 50)

# HVAD: Bestem streg-egenskaber
streg_laengde = 30  # hvor langt ind
streg_tyk = 5       # hvor tyk streg

# HVAD: Lav en funktion (kode-maskine)
def punkt_paa_cirkel(cx, cy, radius, vinkel_fra_kl12_grader):
    # cx og cy er NAVNE på tal som sendes ind senere
    # De er IKKE magiske—vi kunne kalde dem hvad som helst
    
    # HVAD: Konverter vinkel til det math kan forstå
    vinkel_radianer = math.radians(vinkel_fra_kl12_grader - 90)
    # HVORFOR: math.cos/sin bruger radianer, ikke grader
    
    # HVAD: Beregn punkt på cirkel
    x = cx + radius * math.cos(vinkel_radianer)
    y = cy + radius * math.sin(vinkel_radianer)
    # HVORFOR: Det er matematisk formel for cirkel-punkter
    
    # HVAD: Gør til heltal
    return (int(x), int(y))
    # HVORFOR: Skærmpixels skal være hele tal

# HVAD: Gentag 12 gange
for i in range(12):  # i bliver 0, 1, 2, ..., 11
    # HVAD: Beregn vinkel for denne streg
    vinkel_grader = i * 30  # 0, 30, 60, ..., 330
    
    # HVAD: Brug vores funktion til at finde yderpunkt
    start_ude = punkt_paa_cirkel(centrum_x, centrum_y, radius, vinkel_grader)
    #                           320       240      190     0/30/60/...
    # Her bliver cx=320, cy=240 inde i funktionen
    
    # HVAD: Brug samme funktion til inderpunkt
    slut_ind = punkt_paa_cirkel(centrum_x, centrum_y, radius - streg_laengde, vinkel_grader)
    #                          320       240      160              0/30/60/...
    # Her bliver cx=320, cy=240 igen
    
    # HVAD: Tegn streg
    pygame.draw.line(skaerm, (0, 0, 0), start_ude, slut_ind, streg_tyk)
    # HVORFOR: Det tegner fra yderpunkt til inderpunkt

# HVAD: Vis det tegnede
pygame.display.flip()

# HVAD: Hold vindue åbent
koerer = True
while koerer:  # gentag for evigt
    for haendelse in pygame.event.get():  # tjek om noget sker
        if haendelse.type == pygame.QUIT:  # hvis der klikkes luk
            koerer = False  # stop løkken

pygame.quit()  # ryd op
