#lektion 6
'''
opgave 6,1-6,6
my_favourite_person= {'first_name': 'ernst', 'last_name': 'kjær', 'age': 23, 'city': 'Ålborg'}
print (my_favourite_person['first_name'])
print (my_favourite_person['last_name'])
print (my_favourite_person['age'])
print (my_favourite_person['city'])

for key, value in my_favourite_person.items():
    print (f"min vens {key}: er {value}")

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

list_of_people = ['jen', 'sarah', 'edward', 'phil', 'ernst', 'kristian', 'mikkel', 'mathias',  'marco']
for person in list_of_people:
    if person in favorite_languages.keys():
        print (f"tak {person} fordi deltog i undersøgelsen")
    else:
        print (f"{person} du burde tage undersøgelsen")


'''''
#opave 7.1-7.10
'''
bil_ønske= input(f"hvilken bil kunne du tænke dig ")

print (f"{bil_ønske} er virkelig en fed bil")
'''
'''
antal_af_mennsker = int(input("hvor mange mennsekser er I i aften?  "))
if antal_af_mennsker < 2: 
    print ("hvorfor er du en taber der spiser alene")
else:
    print ("velkommen til bordet")
'''
'''
liste_med_kundes_ønsked_pizza_topping = []

while True:
    topping_pizza = input("\n hvilken topping vil du have på din pizza? ")
    liste_med_kundes_ønsked_pizza_topping.append(topping_pizza)
    print (f"vi tilføjer {topping_pizza} til din pizza")
    svar = input(f"vil du have flere toppings? (ja/nej) ")
    if svar == 'nej':
        print (f"din pizza med følgende toppings er nu færdig: ")
        for topping in liste_med_kundes_ønsked_pizza_topping:
            print (f"- {topping}")
        break

 '''

#spil
# import pygame
# import math
# import random
# import pygame
# import math 

# pygame.init()
# screen = pygame.display.set_mode((640, 680)) # Create a window of 640x480 pixels

# game if there is ko kostant speed
'''''
box_position = (30, 30)
while True:
    screen.fill((255, 255, 255)) # Fill the screen with white
    for event in pygame.event.get():
        speed= []
        speed=+1


       
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_d:
                box_position = (box_position[0]+10, box_position[1])
           elif event.key == pygame.K_a:
                box_position = (box_position[0] - 10, box_position[1])
           elif event.key == pygame.K_s:
                box_position = (box_position[0], box_position[1]+10)
           elif event.key == pygame.K_w:
                box_position = (box_position[0], box_position[1]-10)
        
           if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(box_position[0], box_position[1], 60, 60))   
        
        pygame.display.flip()
'''''
#konstant hastighed 
# jeg har brug for at kassen bevæger sig med en konstant hastighed efter at jeg har trygget på en af tasterne
'''''
speed=0.01
x_kommende_retning=0
y_kommende_retning=0
box_position = (30, 30)
while True:
    
   
    screen.fill((255, 255, 255)) # Fill the screen with white
    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x_kommende_retning = speed
            elif event.key == pygame.K_a:
                x_kommende_retning = -speed
                
            elif event.key == pygame.K_s:
                y_kommende_retning = speed
            elif event.key == pygame.K_w:
                y_kommende_retning = -speed

    box_position = (box_position[0]+x_kommende_retning, box_position[1]+y_kommende_retning)
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(box_position[0], box_position[1], 60, 60))   
    pygame.display.flip()
    
    if event.type == pygame.QUIT:
                pygame.quit()
                exit()
'''
# jeg har brug for at kassen bevæger sig med en konstant hastighed efter at jeg har trygget på en af tasterne
import pygame
import math
import random
import pygame
import math 

pygame.init()
screen = pygame.display.set_mode((640, 680)) # Create a window of 640x480 pixels
speed=0.07
x_kommende_retning=0
y_kommende_retning=0
apple_library = []  # Liste af dicts
total_score = 0  # Husk at have dette for points
mængden_af_æbler = 0
box_position = [100, 100]
skrift_type_start = [30, 30]
skrift_type = pygame.font.Font(None, 32)
æble_skrift_type = pygame.font.Font(None, 20)
def generer_æbler():
    
    for i in range(10):
        x_værdier = random.randrange(20, 620)
        y_værdier = random.randrange(150, 660)
        points = random.randint(1, 100)
        radius = points // 4 + 10  # Proportional størrelse
        apple_library.append({
            'position':[ x_værdier,  y_værdier],
            'points': points,
            'radius': radius
        })
generer_æbler()

while True:
    screen.fill((255, 255, 255)) # Fill the screen with white
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 100))
    tal_tekst = str(f"mængden af æbler spist er  {mængden_af_æbler} og di score er:  {total_score}") 
    tal_billede = skrift_type.render(tal_tekst, True, (255,255,255))
    tal_bredde = tal_billede.get_width()
    tal_højde = tal_billede.get_height()
    screen.blit(tal_billede, ( skrift_type_start[0] , skrift_type_start[1]))


    for apple in apple_library:
        pygame.draw.circle(screen, (255, 0, 0), apple['position'], apple['radius'])
        tal_tekst = str(f"{apple['points']}") # her tages der et tal fra listen og den laves om til en string, så den fungere som et bogstav, 
        tal_billede = skrift_type.render(tal_tekst, True, (0,0,0))
        tal_bredde = tal_billede.get_width()
        tal_højde = tal_billede.get_height()
        screen.blit(tal_billede, (apple['position'][0]-tal_bredde//2 , apple['position'][1]-tal_højde//2))


    for event in pygame.event.get():
       if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                y_kommende_retning = 0
                x_kommende_retning = speed
            elif event.key == pygame.K_a:
                x_kommende_retning = -speed
                y_kommende_retning = 0
            elif event.key == pygame.K_s:
                x_kommende_retning = 0
                y_kommende_retning = speed
            elif event.key == pygame.K_w:
                x_kommende_retning = 0
                y_kommende_retning = -speed
 
    box_position[0]+=x_kommende_retning 
    box_position[1]+=y_kommende_retning
# viskal ændre det sådan at kassen ikke kan gå ud af skærmen kommer den tilbage på den anden side
    if box_position[0] > 630:
        box_position[0] = 10
    elif box_position[0] < 10:
        box_position[0] = 630
    if box_position[1] > 670:
        box_position[1] = 5
    elif box_position[1] < 5:
        box_position[1] = 670
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(box_position[0], box_position[1], 60, 60))   
    pygame.display.flip()



    # jeg har brug for at fjerne et æble når kassen rører ved det


#har brug for hjælp til at forstå denne del
    for apple in apple_library[:]:
        if (box_position[0] < apple['position'][0] + apple['radius'] and box_position[0] + 60 > apple['position'][0] - apple['radius'] and
            box_position[1] < apple['position'][1] + apple['radius'] and box_position[1] + 60 > apple['position'][1] - apple['radius']):
            total_score += apple['points']
            mængden_af_æbler += 1
            apple_library.remove(apple)
            print("æblet er spist")
            
            print(f"mængden af æbler spist er  {mængden_af_æbler} og di score er:  {total_score}")

    if not apple_library:
        generer_æbler()        
         

         
    
    if event.type == pygame.QUIT:
                pygame.quit()
                exit()

