#rock paper scissors game
import random
"""
Friends = ["camille", "lyana", "george", "ray" , "mireille" , "park"]
print(random.choice(Friends))
"""
#rock paper ciseau rock
#user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
choice = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choice)
if user_choice == 0:
    if computer_choice == "Rock":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
        print(f"Computer choose {computer_choice} Match nul")
    elif computer_choice == "Paper":
        # Paper
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

        print( f"Computer choose {computer_choice} you win")
    else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
        print(f"computer choose {computer_choice} you loose")

elif user_choice == 1 :
    if computer_choice == "Rock":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
        print(f"Computer choose {computer_choice} You win")
    elif computer_choice == "Paper":
        # Paper
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

        print( f"Computer choose {computer_choice} Match nul")
    else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
        print(f"computer choose {computer_choice} you loose")

elif user_choice == 2 :
    if computer_choice == "Rock":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
        print(f"Computer choose {computer_choice} You loose")
    elif computer_choice == "Paper":
        # Paper
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

        print( f"Computer choose {computer_choice} You Win")
    else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)
        print(f"computer choose {computer_choice} Match nul")
else :
    print("Wrong select, Type 0 for Rock, 1 for Paper or 2 for Scissors\n")