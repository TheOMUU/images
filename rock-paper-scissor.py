import random

def play():
    user = input("Enter your choice from rock, paper, scissor : ").lower()
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    print(f"\nYou chose : {user}")
    print(f"Computer chose : {computer}")

    if user == computer:
        return "It's a tie"
    elif (user == "rock" and computer == "scissors") or \
          (user == "paper" and computer == "rock") or \
          (user == "scissors" and computer == "paper") :
        return "You win!"
    elif user not in choices:
        return "Invalid choice!"
    else:
        return "Computer wins!"

print(play())