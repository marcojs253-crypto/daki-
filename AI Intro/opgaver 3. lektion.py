print (4.1)
pizzas = ["margarita", "kebab og salt", "peperoni"]
for pizza in pizzas:
    print(f"{pizza} er godt")

print( "\njeg elsker pizza")

print("\n4.2")
dyrs = ["orangotang", "grorilla", "chimpanse"]
for dyr in dyrs:
    print(f"{dyr} ligner et menneske")

print("alle disse dyr ligner mennesker")

print("\n4.3")
#for tal in range (1,21):
#    print(tal)

print("\n4.4")
#liste_million = []
#or million in range (1,1000001):
#    liste_million.append(million)

#print(liste_million)


print("\n4.5")
#print (min(liste_million))
#print (max(liste_million))
#print (sum(liste_million))

print("\n4.7")
for tal in range (1,21,2):
    print (tal)

print("\n4.8")
for tal in range (3,31):
    print (tal*3)

print("\n4.9")
for tal in range (1,11):
    print (tal**3)

comprihent_list=[tal**3 for tal in range (1,11)]

print(comprihent_list)


print("\n4.10")

print(f"de første 3 ting er{comprihent_list[:3]}")
print(f"de 3 midderste ting er{comprihent_list[len(comprihent_list)//2-1:len(comprihent_list)//2+2]}")
print(f"de sidste 3 ting er{comprihent_list[-3:]}")

min_vens_pizza = pizzas [:]
min_vens_pizza.append("annanas")
pizzas.append("katoffel")
print(min_vens_pizza)
print(pizzas)