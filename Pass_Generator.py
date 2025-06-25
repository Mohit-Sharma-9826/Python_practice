import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_','=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"',',', '<', '.', '>', '/', '?', '`', '~']

print("Welcome to the Password Generator!")
n_letter = int(input("How many letters would you like in your password: "))  #5
n_number = int(input("How many numbers would you like in your password: "))  #3
n_sym = int(input("How many symbols would you like in your password: "))  #2

total = n_letter + n_number + n_sym
password = []
ch = [letters, numbers, symbols]


while len(password) != total:
    ran = random.choice(ch)
    if ran == ch[0]:
        if n_letter > 0:
            password.append(random.choice(ran))
        n_letter -= 1
    elif ran == ch[1]:
        if n_number > 0:
            password.append(random.choice(ran))
        n_number -= 1
    else:
        if n_sym > 0:
            password.append(random.choice(ran))
        n_sym -= 1

print("Password is: ", end='')
for i in password:
    print(i, end='')