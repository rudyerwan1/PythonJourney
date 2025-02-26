
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
#my solution:
print("Welcome to the Harry Poter game\n")
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
potion_base = input("Please choose between Water or Oil \n").lower()
#Choix de la quantite  :
quantity = float(input("Please insert the quantities\n"))
#Choix de l'ingredient principale  :
main_ingredient = int(input("Please choose the main ingredient 1 for sliver leaf or 2 for fairy dust\n"))
#cout de la base
cost_of_base = 0
ingredient_cost = 0
total_cost_base = 0
if potion_base == "water" :
    cost_of_base = quantity * 3
elif potion_base == "oil":
    cost_of_base = quantity * 4
else :
    print("Choose between water or oil please")
    exit("you didn't select the right choice")
#action baser sur l'ingredient principale
if main_ingredient == 1 :
    action_with_ingredient = input("What would you like to do with the sliver leaf Grind or Infuse ?\n").lower()
    ingredient_cost += 10
    total_cost_base = ingredient_cost + cost_of_base
    if action_with_ingredient == "infuse":
        print(f"Your potion is successful young wizard here what you use (Sliver) and you decide to ${action_with_ingredient} it,"
              f"here your total cost of base {total_cost_base:.2f}€")
        print("Great Job now you are Master Alchemist!")
    else:
        print(f"Your potion failed unfortunately here your total cost of base {total_cost_base:.2f}€")
elif main_ingredient == 2 :
    action_with_ingredient = input("What would you like to do with  fairy dust Mix or Shake ?\n").lower()
    ingredient_cost += 15
    total_cost_base = ingredient_cost + cost_of_base
    if action_with_ingredient == "mix":
        print(f"Your potion is successful young wizard here your total cost of base {total_cost_base:.2f}€")
        print ("Great Job now you are Master Alchemist!")
    else:
        print(f"Your Potion failed unfortunately here your total cost of base {total_cost_base:.2f}€")
else:
    print("you didn't choose the right choice please try again")
    exit("you didn't select the right choice")

