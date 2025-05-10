import random

# We are using r before string to ignores the escape character like "/"
rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def player(pl_choice):
    if(pl_choice.lower() == "r"):
        return rock
    elif(pl_choice.lower() == "p"):
        return paper
    elif(pl_choice.lower() == "s"):
        return scissors
    else:
        return None
        
def computer(cp):
    cp_choice = random.choice(cp)
    return cp_choice

def winner(pl, cp, p_score, c_score):
    if pl == cp:
        print(">>>>>>>>>>>>>> It is a tie! <<<<<<<<<<<<<<<")
        p_score += 1
        c_score += 1
    elif(pl == rock and cp == scissors):
        print(">>>>>>>>>>>>>> Player Wins <<<<<<<<<<<<<<<")
        p_score += 1
    elif(pl == rock and cp == paper):
        print(">>>>>>>>>>>>>> Computer Wins <<<<<<<<<<<<<<<")
        c_score += 1
    elif(pl == scissors and cp == paper):
        print(">>>>>>>>>>>>>> Player Wins <<<<<<<<<<<<<<<")
        p_score += 1
    elif(pl == scissors and cp == rock):
        print(">>>>>>>>>>>>>> Computer Wins <<<<<<<<<<<<<<<")
        c_score += 1
    elif(pl == paper and cp == rock):
        print(">>>>>>>>>>>>>> Player Wins <<<<<<<<<<<<<<<")
        p_score += 1
    elif(pl == paper and cp == scissors):
        print(">>>>>>>>>>>>>> Computer Wins <<<<<<<<<<<<<<<")
        c_score += 1
    else:
        print("Something went wrong")
    return [p_score, c_score]

num = int(input("Enter the number of matches: "))
pl_score, cp_score = 0, 0

for i in range(num):
    print("<---------- Rock Paper Scissors ---------->\n")

    pl_choice = input("Enter your move (R/P/S): ")
    comp = [rock, paper, scissors]

    pl = player(pl_choice)
    cp = computer(comp)

    if pl == None:
        print("Valid input for the game!")
        exit()

    print("","player's Move: ",pl,"Computer's Move:", cp, sep='\n')

    w = winner(pl, cp, pl_score, cp_score)
    pl_score = w[0]
    cp_score = w[1]
    print("Player's score: ", pl_score, "\t", "Computer's score: ", cp_score)

print("\n")
print(":"*15,"Match is over", ":"*15)

if pl_score > cp_score:
    print("*"*15,"You win the match", "*"*15)
elif pl_score < cp_score:
    print("*"*15,"You Loose", "*"*15)
else:
    print("*"*15,"The match is tie!", "*"*15)

print("\n")