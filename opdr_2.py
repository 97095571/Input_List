# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]

import array

print(gasten)

print("Nou belt Marie dat ze niet meer meegaat.\nZorg ervoor dat Marie uit de lijst wordt gehaald.")
gasten.remove('Marie')
print(gasten)

print("Even later belt George, hij wil ook mee. George wil naast Kees zitten!\nZorg ervoor dat George naast Kees wordt toegevoegd.")
gasten.insert(3,"George")

print(gasten)