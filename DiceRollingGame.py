
import random

while True:
    input("Press Enter to roll the dice...")

    dice = random.randint(1, 6)

    print("🎲 You rolled:", dice)

    play_again = input("Roll again? (y/n): ").lower()

    if play_again != "y":
        print("Game over! 👋")
        break
