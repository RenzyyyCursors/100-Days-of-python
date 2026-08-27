#%%
import random

print("Welcome to Number Guessing Game!")
print("You are guessing a number between 1-100.")

# using local vairables in funtion to return a value 
def get_difficulty():
    while True:
        print("Diffiulty Hard(h),Normal(n),Easy(e)")
        difficulty = input("Enter Difficulty level. ")

        if difficulty.lower() == 'h':
            tries = 5
            return tries
        elif difficulty.lower() == 'n':
            tries = 10
            return tries
        elif difficulty.lower() == 'e':
            tries = 15
            return tries
        else:
            print("Enter correct difficulty")
            continue

# Another example of local variable function
def randomizer():
    number = random.randint(1,100)
    return number 

# Main function
tries = get_difficulty()
number = randomizer()

while True:
    guess = int(input("Guess a number. "))
    if tries == 0:
        print("You Lost!")
        break
    if guess == number:
        print(f"You correctly guessed the number was {number}.")
        break
    elif guess > number:
        print(f"Number is smaller. Tries left {tries}")
        tries -= 1
    elif guess < number:
        print(f"Number is greater. Tries left {tries}")
        tries -= 1

# %%
