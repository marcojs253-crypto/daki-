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

# HVORFOR: Det hjælper os med at se centrum
# 2) Ur-geometri (som angivet)
centrum_x, centrum_y = 320, 240
radius = 190              # 240 - 50 i din opsætning
streg_laengde = 30        # hvor langt ind fra ydercirklen
streg_tykkelse = 5        # linjetykkelse i pixels
ANTAL_TIMER = 12
VINKEL_TRIN = 360 // ANTAL_TIMER  # 30 grader

pygame.draw.circle(skaerm, (0, 0, 255), (centrum_x, centrum_y), 210)
pygame.draw.circle(skaerm, (0, 0, 0), (centrum_x, centrum_y), 5)

def punkt_fra_top(centrum_x, centrum_y, radius, vinkel_fra_kl12_grader):
    """
    Beregn et punkt på cirklen givet vinkel målt fra 'kl. 12' (opad).
    Bruges konventionen: x = r*sin(θ) og y = r*cos(θ), hvor θ er i radianer.
    """
    theta = math.radians(vinkel_fra_kl12_grader)  # grader -> radianer
    x = centrum_x + radius * math.sin(theta)      # vandret (Opposite)
    y = centrum_y + radius * math.cos(theta)      # lodret  (Adjacent)
    return int(x), int(y)

# 3) Tegn 12 time-streger i 30°-trin, fra ydercirklen og ind
for i in range(ANTAL_TIMER):
    vinkel_grader = i * VINKEL_TRIN            # 0,30,60,...,330
    yderpunkt = punkt_fra_top(centrum_x, centrum_y, radius, vinkel_grader)
    inderpunkt = punkt_fra_top(centrum_x, centrum_y, radius - streg_laengde, vinkel_grader)
    pygame.draw.line(skaerm, (0, 0, 0), yderpunkt, inderpunkt, streg_tykkelse)  # tegn streg

pygame.display.flip()

# 4) Event-loop: luk pænt ved klik på kryds
koerer = True
while koerer:
    for haendelse in pygame.event.get():
        if haendelse.type == pygame.QUIT:
            koerer = False
