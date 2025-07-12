import random
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 to 100.")

number = random.randint(1,100)

diff = input("Choose the difficulty. Type 'easy' or 'hard': ")
no_of_attempts = 10
if diff.lower() == "hard":
    no_of_attempts = 5

num = no_of_attempts
flag = 0
for i in range(no_of_attempts):
    print(f"You have {num} attempts remaining to guess the number.")
    num -= 1
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You guess the number👌👌")
        flag = 1
        break
    elif guess < number:
        print("Too low!")
        print("Guess again!")
    elif guess > number:
        print("Too high!")
        print("Guess again!")

if flag == 0:
    print("You loose 😢😢")
    print(f"The number is : {number}")