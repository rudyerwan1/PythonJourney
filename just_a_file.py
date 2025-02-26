
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