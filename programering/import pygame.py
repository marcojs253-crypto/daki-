import pygame
import random
import math

# ---------- Indstillinger ----------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

SHIP_SIZE = 30  # firkant (rumskib) side længde
SHIP_SPEED = 4  # pixels per frame (fart bevaret i retning)

NUM_GOLD = 10
GOLD_MIN_POINTS = 1
GOLD_MAX_POINTS = 100
# -----------------------------------

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rumskib - Guldklumper")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 40)

# Hjælpefunktioner
def clamp_angle_to_vector(dx, dy):
    # normaliserer vektoren, men håndterer (0,0)
    mag = math.hypot(dx, dy)
    if mag == 0:
        return 0, 0
    return dx / mag, dy / mag

def distance(a, b):
    return math.hypot(a[0]-b[0], a[1]-b[1])

# Rumskib (firkant) initialisering
ship_x = SCREEN_WIDTH // 2
ship_y = SCREEN_HEIGHT // 2

# Startbevægelse: stillestående (0,0)
vel_x = 0.0
vel_y = 0.0

# Generer guldklumper (liste af dicts)
gold_list = []
for _ in range(NUM_GOLD):
    pts = random.randint(GOLD_MIN_POINTS, GOLD_MAX_POINTS)
    # radius proportional med points: base + scale*points
    radius = 4 + int(pts / 4)  # justeret så størrelserne bliver rimelige
    # vælg tilfældig position, så cirklen ikke sidder helt ude ved kanten
    gx = random.randint(radius + 5, SCREEN_WIDTH - radius - 5)
    gy = random.randint(radius + 5, SCREEN_HEIGHT - radius - 5)
    gold_list.append({"x": gx, "y": gy, "points": pts, "r": radius})

total_score = 0

# Popup ved indsamling (vis "+N" i kort tid)
popup_texts = []  # liste af dicts: {"text":..., "x":..., "y":..., "timer":...}

def add_popup(text, x, y, duration_frames=60):
    popup_texts.append({"text": text, "x": x, "y": y, "timer": duration_frames})

running = True
while running:
    dt = clock.tick(FPS)

    # --- Events ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Retningsændring ved tastetryk (pile + WASD)
            if event.key in (pygame.K_LEFT, pygame.K_a):
                vel_x, vel_y = clamp_angle_to_vector(-1, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
                vel_x, vel_y = clamp_angle_to_vector(1, 0)
            elif event.key in (pygame.K_UP, pygame.K_w):
                vel_x, vel_y = clamp_angle_to_vector(0, -1)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                vel_x, vel_y = clamp_angle_to_vector(0, 1)
            # Diagonaler hvis to taster trykkes samtidigt håndteres ikke her -- man kan ændre til at lytte på pygame.key.get_pressed() hvis ønskes.

    # Rumskib bevægelse: konstant bevægelse i retningen * SHIP_SPEED
    ship_x += vel_x * SHIP_SPEED
    ship_y += vel_y * SHIP_SPEED

    # Wrap-around (teleport til modsatte side)
    if ship_x < -SHIP_SIZE:
        ship_x = SCREEN_WIDTH + SHIP_SIZE
    elif ship_x > SCREEN_WIDTH + SHIP_SIZE:
        ship_x = -SHIP_SIZE
    if ship_y < -SHIP_SIZE:
        ship_y = SCREEN_HEIGHT + SHIP_SIZE
    elif ship_y > SCREEN_HEIGHT + SHIP_SIZE:
        ship_y = -SHIP_SIZE

    # --- Kollisionsdetektion mellem rumskib (firkant) og cirkler ---
    # Brug center af firkanten som reference
    ship_center = (ship_x + SHIP_SIZE/2, ship_y + SHIP_SIZE/2)
    collected_indices = []
    for i, gold in enumerate(gold_list):
        gold_center = (gold["x"], gold["y"])
        # afstand
        d = distance(ship_center, gold_center)
        # if d < (radius + half_ship_diag) - men enklere: brug half diagonal for mere præcis :)
        # half diagonal af firkant:
        half_diag = math.hypot(SHIP_SIZE/2, SHIP_SIZE/2)
        if d <= gold["r"] + half_diag:
            collected_indices.append(i)

    # Fjern indsamlede og opdater score + popup
    # fjern fra højeste indeks først for at undgå index-forskydning
    for idx in sorted(collected_indices, reverse=True):
        gold = gold_list.pop(idx)
        pts = gold["points"]
        total_score += pts
        # lav popup ved rumskibens center
        add_popup(f"+{pts}", ship_center[0], ship_center[1])

    # Opdatér og fjern popups når deres timer løber ud
    for p in popup_texts[:]:
        p["timer"] -= 1
        p["y"] -= 0.5  # flytter popupen lidt op hver frame
        if p["timer"] <= 0:
            popup_texts.remove(p)

    # --- Tegn alt ---
    screen.fill((12, 12, 30))  # baggrundsfarve (mørk)

    # Tegn guldklumper
    for gold in gold_list:
        # gul farve
        pygame.draw.circle(screen, (212, 175, 55), (gold["x"], gold["y"]), gold["r"])
        # skriv point ovenpå cirklen (centreret)
        txt = font.render(str(gold["points"]), True, (0, 0, 0))
        txt_rect = txt.get_rect(center=(gold["x"], gold["y"]))
        screen.blit(txt, txt_rect)

    # Tegn rumskib (firkant)
    ship_rect = pygame.Rect(int(ship_x), int(ship_y), SHIP_SIZE, SHIP_SIZE)
    pygame.draw.rect(screen, (180, 180, 255), ship_rect)
    # evt. lille "cockpit" for at gøre det tydeligere
    cockpit = pygame.Rect(int(ship_x + SHIP_SIZE*0.25), int(ship_y + SHIP_SIZE*0.15), int(SHIP_SIZE*0.5), int(SHIP_SIZE*0.5))
    pygame.draw.rect(screen, (100, 150, 255), cockpit)

    # Tegn total score (øverst til venstre) - opdateres når du samler
    score_surf = big_font.render(f"Score: {total_score}", True, (255, 255, 255))
    screen.blit(score_surf, (10, 10))

    # Tegn popup-tekster
    for p in popup_texts:
        surf = big_font.render(p["text"], True, (255, 220, 0))
        rect = surf.get_rect(center=(int(p["x"]), int(p["y"])))
        screen.blit(surf, rect)

    # Hvis alle klumper er indsamlet, vis en besked
    if not gold_list:
        msg = big_font.render("Alle guldklumper er indsamlet! Godt klaret!", True, (200, 255, 200))
        rect = msg.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(msg, rect)

    pygame.display.flip()

pygame.quit()
