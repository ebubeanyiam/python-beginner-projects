import random

attempts = 0

number = random.randint(1, 30)
print("I am thinking of a number between 1 and 30")

while attempts < 6:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess < number:
        print("Higher")
    if guess > number:
        print("Lower")
    if guess == number:
        break

if guess == number:
    print(f"Yes, you guessed the correct number in {attempts} guesses")

if guess != number:
    print(f"Oops, seems like you failed. The right guess was {number}")
