import random
print("Welcome to the number guessing game!")
# Generate a random number between 1 and 100
number = random.randint(1, 100)
# Keep track of number of guesses
guesses = 0
while True:
    guess = int(input("Enter your guess: "))
    guesses += 1
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("You got it in {guesses} guesses! The number was {number}.")
        break





