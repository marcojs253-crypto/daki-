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

pygame.init()
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels



box_position = (30, 30)
while True:
    screen.fill((255, 255, 255)) # Fill the screen with white
    for event in pygame.event.get():


       
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

       
