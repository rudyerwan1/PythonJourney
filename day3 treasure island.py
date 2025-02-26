
#Jeux d'apprentis sorcier
"""
Objective of the Game:

You are a sorcerer alchemist, and your mission is to prepare a magical potion by following the correct steps.
You will need to make critical choices at each stage and use calculations to obtain the right quantities of ingredients.
If you make the right choices, your potion will be successful, and you will be crowned Master Alchemist.

Instructions:

    Choose the Base of the Potion:

        Select a base: "Water" or "Oil"

        Cost of the base (€3/liter for water, €4/liter for oil)

    Quantity of Base:

        Enter the quantity of the base in liters (decimal number)

    Choose the Main Ingredient:

        Select an ingredient: "Silver Leaf" or "Fairy Dust"

    Action with the Main Ingredient:

        If "Silver Leaf": "Grind" or "Infuse"

        If "Fairy Dust": "Mix" or "Shake"

    Calculate the Total Cost of Ingredients:

        Cost of the base

        Cost of the main ingredient (€10 for "Silver Leaf", €15 for "Fairy Dust")

        Display the total cost rounded to 2 decimal places

    Verify Potion Success:

        If "Silver Leaf" and "Infuse" or "Fairy Dust" and "Mix": Potion successful

        Otherwise: Potion failed
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

print("""Instructions:
You are a sorcerer alchemist, and your mission is to prepare a magical potion by following the correct steps. 
You will need to make critical choices at each stage and use calculations to obtain the right quantities of ingredients. 
If you make the right choices, your potion will be successful, and you will be crowned Master Alchemist.""")

#Choix de la base de la potion :

