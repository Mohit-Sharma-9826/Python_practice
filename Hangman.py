import random

hangman_stages = [
    '''
        +---+
            |
            |
            |
            ===''',
    '''
        +---+
        O   |
            |
            |
            ===''',
    '''
        +---+
        O   |
        |   |
            |
            ===''',
    '''
        +---+
        O   |
        /|   |
            |
            ===''',
    '''
        +---+
        O   |
        /|\\  |
            |
            ===''',
    '''
        +---+
        O   |
        /|\\  |
        /    |
            ===''',
    '''
        +---+
        O   |
        /|\\  |
        / \\  |
            ==='''
]

word_list = ["Monkey", "Camel", "Cat", "Hello", "Rose"]
ran_word = random.choice(word_list)
hide_letter = []
for i in range(len(ran_word)):
    hide_letter.append("_")

print("Welcome to the Hangman game!")

win = False
hang = 0
while True:
    for k in hide_letter:
        print(k," ", end='')
    guess = input("\n\nGuess a letter: ")

    flag = 0
    for j in range(len(ran_word)):
        if guess == ran_word[j].lower() and hide_letter[j] == "_":
            hide_letter[j] = ran_word[j]
            flag = 1
    if flag == 1:
        print("You guess right!")
    else:
        print("You guessed worng!")
        print(hangman_stages[hang])
        hang += 1

    if hide_letter == list(ran_word):
        win = True
        break
    if hang == 7:
        break

if win:
    print("\n<---------- You Win ---------->")
else:
    print("\n<---------- You hanged ---------->")
    


