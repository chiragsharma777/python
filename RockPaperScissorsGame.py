
import random

choices = ["r", "p", "s"]

computer = random.choice(choices)

player = input("Choose (r = rock, p = paper, s = scissors): ").lower()

print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")

elif player == "r" and computer == "s":
    print("You win!")

elif player == "p" and computer == "r":
    print("You win!")

elif player == "s" and computer == "p":
    print("You win!")

elif player in choices:
    print("Computer wins!")

else:
    print("Invalid choice!")

