print("2.1")
samtale = "hej med dig"
print (samtale)

print (2.2)
hejsa = "hej hvordan har du det"
print (hejsa)
hejsa = "gå ud af min bruser"
print (hejsa)
print (2.3)
navn = "al"
besked = f"hejsa, {navn} "
print (besked)
print (2.4)
print (navn.lower())
print (navn.upper())
print (navn.title())

print (2.5)
print ('morgen freeman sagde engang "get busy living or get busy dying" ')

print (2.6)
kendt_person = "morgen freeman"
besked = 'sagde engang "get busy living or get busy dying"'
print (kendt_person,besked)
print (2.7)
print (f"\n {kendt_person}\t{besked}")
besked.rstrip()
print ("\t",besked)
besked.lstrip()
print ("\t","\t","\t",besked)
besked.strip()
print ("\t","\t","\t",besked)
print (2.8)
print(8*1)
print(8**1)
print(8/1)
print(9-1)

print (2.9)
y_nummer = 19
print (y_nummer)
print (2.10)
# hejsa det var de første 10 opgaver klaret.
print (3.1)
venner = ["mad", "al", "rasmus"]
print(venner[0])
print(venner[1])
print(venner[2])

print (3.2)
print (f"hej {venner[0]}, jeg håber i har det godt")
print (f"hej {venner[1]}, jeg håber i har det godt")
print (f"hej {venner[2]}, jeg håber i har det godt")
print (3.3)
ønske_liste = ["diamanter", "penge", "fly", "drone"]
print(f"jeg ønsker mig en fed {ønske_liste[3]}")
print (3.4)
print (f"hej {venner[0]}, jeg håber I vil med ud og spise")
print (f"hej {venner[1]}, jeg håber I vil med ud og spise")
print (f"hej {venner[2]}, jeg håber I vil med ud og spise")
print (3.5)

print (f"hej {venner[2]}, beklaker du ikke vil med ud og spise")
venner.pop()
venner.append("ivan")
print (f"hej {venner[0]}, rasmus kommer ikke, men ivan kommer")
print (f"hej {venner[1]}, rasmus kommer ikke, men ivan kommer")
print (f"hej {venner[2]}, rasmus kommer ikke, men ivan kommer")
print (3.6)
venner.insert(0,"steffen")
venner. insert(2,"marco")
print (venner)
print (3.7)
x=venner.pop()
print (f"farvel {x}")
del venner [0]
del venner [0]
del venner [0]
del venner [0]



print(venner)
print (3.8)
steder_jeg_gerne_vil_hen = ["din mor", "din søster", "verdens ende", "månen uden maske"]
venner.sort
print(steder_jeg_gerne_vil_hen.sort())
print (3.9)
print (3.10)

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