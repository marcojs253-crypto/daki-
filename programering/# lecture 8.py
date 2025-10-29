import random
import pygame
import math
import random

screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))

class data_point:
    def __init__(self, x_værdie, y_værdie, class_label, color):
        self.x_værdie = x_værdie
        self.y_værdie = y_værdie
        self.class_label = class_label
        self.color = color
    
    def metod_draw(self):  # ÆNDRET: Tilføjet 'self' som første parameter
        pygame.draw.circle(screen, self.color, (self.x_værdie, self.y_værdie), 10)  # ÆNDRET: Bruger selvets koordinater i stedet for 'liste_med_punkter'

liste_med_punkter=[]
for n in range(10):
     x = random.gauss(200, 20)
     y = random.gauss(200, 20)
     liste_med_punkter.append(data_point(x,y,"salmon", (255,10,10) ))

# ÆNDRET: Loopet kalder nu metoden på hvert OBJEKT i listen, ikke på klassen
for punkt in liste_med_punkter:  # ÆNDRET: Bruger 'punkt' i stedet for range(len()) for klarhed
    punkt.metod_draw()  # ÆNDRET: Kalder på OBJEKTET 'punkt', ikke klassen 'data_point'

def main():
    pygame.init()
    run_flag = True
    while run_flag is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_flag = False
        pygame.display.flip()

main ()





































# Exercise 9-1: Restaurant
# Make a class called Restaurant. The __init__() method for Restaurant should store
# two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of information,
# and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance of your restaurant from your class. Print the two attributes individually,
# and then call both methods.

# Here I will write the code and corresponding comments to complete the training tasks


class Resturant:
    def __init__(self):
        self.restaurant_name= "la rosa piza"
        self.cuisine_type = "pizza"
    def describe_restaurant (self):
        print(f"navnet på restuarnten er {self.restaurant_name}, og man kan spise {self.cuisine_type}")
resturant = Resturant()
resturant.describe_restaurant ()

print(resturant.cuisine_type)




        