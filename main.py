import random
from colorama import Fore, Style

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print(Fore.CYAN + "The number is between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
            print(Fore.RED + "Too high!")
        elif guess < number:
            print(Fore.YELLOW + "Too low!")
        else:
            print(Fore.GREEN + f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

print("Welcome to the Guess the Number Game!")
print("Do you want to play? (Y/N)")
answer = input("Enter your answer: ").strip().upper()

if answer == "Y":
    print("Game start!")
    guess_number()
else:
    print("Sorry I didn't understand your answer correctly.")
