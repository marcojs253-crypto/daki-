import pygame
import math  # HVAD: Hent værktøjer udefra
from datetime import datetime
import time

pygame.init()        # HVAD: Start pygame
# HVAD: Lav et vindue
skaerm = pygame.display.set_mode((640, 480))
# HVORFOR: Vi skal have noget at tegne på

# HVAD: Gør baggrunden hvid
skaerm.fill((0, 0, 0))
# HVORFOR: Så vi kan se vores sorte streger

# HVORFOR: Det hjælper os med at se centrum
# 2) Ur-geometri (som angivet)
ur_tik =pygame.time.Clock()
centrum_x, centrum_y = 320, 240
radius = 210              # 240 - 50 i din opsætning
streg_laengde_T = 30        # hvor langt ind fra ydercirklen
streg_tykkelse_T = 6        # linjetykkelse i pixels
streg_laengde_M = 10        
streg_tykkelse_M = 1 
streg_tykkelse_Viser_sekundt = 1
streg_tykkelse_Viser_minute = 3
streg_tykkelse_Viser_time = 6
ANTAL_T = 12
ANTAL_M = 60
VINKEL_grad = 360 // ANTAL_T  # 30 grader
vinkel_grad_min =360 // ANTAL_M



# 4) Event-loop: luk pænt ved klik på kryds
koerer = True
while koerer:
    for haendelse in pygame.event.get():
        if haendelse.type == pygame.QUIT:
             koerer = False
    
# 1) Tegn cirklerne
    pygame.draw.circle(skaerm, (0, 0, 255), (centrum_x, centrum_y), radius + 20)
    pygame.draw.circle(skaerm, (0, 0, 0), (centrum_x, centrum_y), 5)
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
        pygame.draw.line(skaerm, (0, 0, 0), start_punkt, slut_punkt, streg_tykkelse_T)

    for i in range (ANTAL_M):
        vinkel = i * vinkel_grad_min
        vinkel_rad = math.radians(vinkel)  # omregn til radianer
        x_start = centrum_x + radius * math.sin(vinkel_rad)      # x-koordinat for startpunkt
        y_start = centrum_y + radius * math.cos(vinkel_rad)      # y-koordinat for startpunkt
        start_punkt = (x_start, y_start)
        x_slut = centrum_x + (radius-streg_laengde_T) * math.sin(vinkel_rad) # y-koordinat for startpunkt
        y_slut = centrum_y + (radius-streg_laengde_T) * math.cos(vinkel_rad) # y-koordinat for startpunkt
        slut_punkt = (x_slut, y_slut)
        pygame.draw.aaline(skaerm, (0, 0, 0), start_punkt, slut_punkt, streg_tykkelse_M)    
         
    nu = datetime.now()
    sekunder = nu.second
    vinkel_grad_sekunder = math.radians(sekunder*6-90)       # 60 sekunder gange 6 = 360 grader
    x_min_slut = centrum_x + radius*0.7 * math.cos(vinkel_grad_sekunder)      # x-koordinat for startpunkt
    y_min_slut = centrum_y + radius*0.7 * math.sin(vinkel_grad_sekunder)      # y-koordinat for startpunkt
    pygame.draw.aaline(skaerm, (255, 255, 255), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_sekundt)

    minute = nu.minute
    vinkel_grad_minute = math.radians(minute*6-90)       # 60 sekunder gange 6 = 360 grader
    x_min_slut = centrum_x + radius*0.75 * math.cos(vinkel_grad_minute)      # x-koordinat for startpunkt
    y_min_slut = centrum_y + radius*0.75 * math.sin(vinkel_grad_minute)      # y-koordinat for startpunkt
    pygame.draw.line(skaerm, (255, 255, 255), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_minute)

    tid_time = nu.hour
    vinkel_grad_time = math.radians(tid_time*30+minute*0.5-90)       # 60 sekunder gange 6 = 360 grader
    x_min_slut = centrum_x + radius*0.85 * math.cos(vinkel_grad_time)      # x-koordinat for startpunkt
    y_min_slut = centrum_y + radius*0.85 * math.sin(vinkel_grad_time)      # y-koordinat for startpunkt
    pygame.draw.line(skaerm, (255, 255, 255), (centrum_x, centrum_y), (x_min_slut, y_min_slut), streg_tykkelse_Viser_time)
    
    ur_tik.tick(120)
    pygame.display.flip()
    print(sekunder)
          
            