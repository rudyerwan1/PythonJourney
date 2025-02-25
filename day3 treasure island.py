
"""print ("Welcome to the treasure game")
direction = input("Select a direction Left or Right \n")
#Section to choose the direction
if direction == "Left" or direction == "left" :
    print("Right choice")
    action=input("Which action you choose Swin or Wait\n")
    if action == "Swin " or action == "swin":
        color = input("Which door you choose Red,Blue or Yellow \n")
        if color == "Blue" or color == "blue" :
            print("you did get eat by wolf")
        elif color == "Red" or color =="red":
            print(" Burned by fire Game Over")
        elif color == "Yellow" or color =="yellow":
            print(" You Win!")
        else:
            print("Fall into a hole Game Over.")

    else:
        print("Game Over.")

else:
    print("Game Over")
#Section
"""
#Jeux d'apprentis sorcier
"""
Tu es un sorcier alchimiste et ta mission est de préparer une potion magique en suivant 
les étapes correctes. Tu devras faire des choix critiques à chaque étape et utiliser des calculs pour obtenir les bonnes quantités d'ingrédients. Si tu fais les bons choix, ta potion sera réussie et tu seras couronné Maître Alchimiste.
Instructions :

    Choix de la base de la potion :

    Choisis une base : "Eau" ou "Huile"

    Coût de la base (3€/litre pour l'eau, 4€/litre pour l'huile)

Quantité de base :

    Entre la quantité de la base en litres (nombre décimal)

Choix de l'ingrédient principal :

    Choisis un ingrédient : "Feuille d'argent" ou "Poussière de fée"

Action avec l'ingrédient principal :

    Si "Feuille d'argent" : "Broyer" ou "Infuser"

    Si "Poussière de fée" : "Mélanger" ou "Agiter"

Calcul du coût total des ingrédients :

    Coût de la base

    Coût de l'ingrédient principal (10€ pour "Feuille d'argent", 15€ pour "Poussière de fée")

    Affiche le coût total arrondi à 2 décimales

Vérification de la réussite de la potion :

    Si "Feuille d'argent" et "Infuser" ou "Poussière de fée" et "Mélanger" : Potion réussie

    Sinon : Potion échouée
"""
print("Bienvenu au jeu d'apprenti sorcier\n")
print(r"""

                   .
         /^\     .
    /\   "V"
   /__\   I      O  o
  //..\\  I     .
  \].`[/  I
  /l\/j\  (]    .  O
 /. ~~ ,\/I          .
 \\L__j^\/I       o
  \/--v}  I     o   .
  |    |  I   _________
  |    |  I c(`       ')o
  |    l  I   \.     ,/
_/j  L l\_!  _//^---^\_    -Row
""")

print("""Instruction Tu es un sorcier alchimiste et ta mission est de préparer une potion magique en suivant 
les étapes correctes. Tu devras faire des choix critiques à chaque étape et utiliser des calculs pour obtenir 
les bonnes quantités d'ingrédients. Si tu fais les bons choix, ta potion sera réussie et tu seras couronné Maître Alchimiste.
Instructions""")

#Choix de la base de la potion :
base_de_la_potion = input('Choisi une base de ta potion "Eau" ou "Huile"\n').lower()
cout_de_la_base = 0
cout_de_lingredient = 0
if base_de_la_potion == "Eau" :
    cout_de_la_base += 3
    print(cout_de_la_base)
    quantite_de_la_base = float(input("Entre la quantité de la base en litres (nombre décimal) \n"))
elif base_de_la_potion == "Huile":
    cout_de_la_base += 4
    print(cout_de_la_base)
#Choix de l'ingrédient principal

else :
    print("Tu ne suis pas les regles")

quantite_de_la_base = float(input("Entre la quantité de la base en litres (nombre décimal) \n"))
#calcul du cout de la potion

#Choix de l'ingrédient principal
ingredient_principal = input('Choisis un ingrédient : "Feuille d\'argent" ou "Poussière de fée\n')
if ingredient_principal == 'Feuille d\'argent' :
    cout_de_lingredient += 10
    action = input('"Broyer" ou "Infuser"')
    if ingredient_principal == 'Feuille d\'argent' and action == "Infuser":
        print("Potion reussie")
elif ingredient_principal == 'Poussière de fée':
    cout_de_lingredient += 15
    action = input('"Mélanger" ou "Agiter"')
    if ingredient_principal == "Mélanger" and action == "Agiter":
        print("Potion reussie")

else :
    print("Tu n'est pas un si bon Alchimiste malheursement ")

