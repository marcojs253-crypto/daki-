import pygame
import math

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

start_point = (100, 100)
angle = 25
length = 300
end_x = start_point[0] + length * math.cos(math.radians(angle))
end_y = start_point[1] + length * math.sin(math.radians(angle))
end_point = (end_x, end_y)

pygame.draw.line(screen, (0,0,0), start_point, end_point, 5)

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()