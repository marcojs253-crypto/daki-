import pygame, sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
radius = 10
list_punkter=[]
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         pos=pygame.mouse.get_pos()
         btn=pygame.mouse
         print ("x = {}, y = {}".format(pos[0], pos[1]))
         list_punkter.append(pos)
         print(list_punkter)
         if len(list_punkter) > 1:
            pygame.draw.aaline(screen,(255, 255, 255), list_punkter[-2], pos, 1) 
            pygame.display.flip()








         
        #  pygame.draw.circle(screen, (0, 0, 255), pos, radius)
        #  pygame.display.flip()


         