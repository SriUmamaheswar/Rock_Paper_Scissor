import random
user_action = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! Yahoo! you win")
    else:
        print("Paper covers rock! You lose better luck next time.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! Yahoo! you win")
    else:
        print("Scissors cuts paper! You lose better luck next time.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! Yahoo! You win")
    else:
        print("Rock smashes scissors! You lose better luck next time.")