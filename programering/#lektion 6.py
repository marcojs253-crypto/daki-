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
import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels

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

speed=0.07
x_kommende_retning=0
y_kommende_retning=0
apple_list = []
for i in range(10):
        x_værdier=random.randrange(0,640)
        y_værdier=random.randrange(0,480)
        apple_list.append((x_værdier, y_værdier))
        print (x_værdier, y_værdier)

box_position = [30, 30]
while True:

 

   
    screen.fill((255, 255, 255)) # Fill the screen with white
    for apple in apple_list:
        pygame.draw.circle(screen, (255, 0, 0), apple, 10)
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
    if box_position[1] > 470:
        box_position[1] = 10
    elif box_position[1] < 10:
        box_position[1] = 470
    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(box_position[0], box_position[1], 60, 60))   
    pygame.display.flip()
    if box_position+10 == apple_list:
         apple_list.remove(box_position)
         
    
    if event.type == pygame.QUIT:
                pygame.quit()
                exit()


    



       
