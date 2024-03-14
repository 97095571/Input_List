# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...
x = True
steden = []
while x:
    stad = input("Vul een stad in\n")
    steden.append(stad)
    if stad == "x": 
        x = False
    else:
        steden.append(stad )


print (steden)