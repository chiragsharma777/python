import random

number = random.randint(1, 100)
attempts = 7
score = 100

print("===== NUMBER GUESSING GAME =====")
print("I have chosen a number between 1 and 100.")
print("You have 7 attempts to guess it.")

for i in range(1, attempts + 1):

    guess = int(input(f"\nAttempt {i}: Enter your guess: "))

    if guess == number:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Your score:", score)
        break

    elif guess < number:
        print("Too low! Try a bigger number.")

    else:
        print("Too high! Try a smaller number.")

    score -= 10

else:
    print("\n❌ Game Over!")
    print("The correct number was:", number)
    print("Your score: 0")