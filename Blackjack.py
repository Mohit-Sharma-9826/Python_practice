import random

print("""\n╔══════════════════════════════════════╗
║                                      ║
║      🂡🂱 Welcome to BLACKJACK 🂡🃑      ║
║                                      ║
║  🃟 Try your luck, beat the dealer!   ║
║        21 is the magic number!       ║
║                                      ║
╚══════════════════════════════════════╝\n""")

def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(pl_score, com_score):
    if  pl_score<=21 and pl_score>com_score or com_score>21:
        print("You won👌👌")
    elif pl_score==com_score and pl_score<=21 and com_score<=21:
        print("Its a draw 😐😐")
    elif pl_score>21 and com_score>21:
        print("Wasted Match 😞😞")
    else:
        print("You loose😢😢")
    print("\n")

player_card = [deal_card(), deal_card()]
computer_card = [deal_card(), deal_card()]
pl_score = sum(player_card)
com_score = sum(computer_card)

print(f"Your cards: {player_card}, current score: {pl_score}")
print(f"Computer's first card: {computer_card[0]}")

ans = input("Type 'y' to get another card, type 'n' to pass: ")
if ans == "y":
    player_card.append(deal_card())
    pl_score = sum(player_card)
    print(f"Your cards: {player_card}, current score: {pl_score}")
    print(f"Computer's first card: {computer_card[0]}")

if com_score <= 15:
    chance = [True, False]
    if random.choice(chance):
        computer_card.append(deal_card())
        com_score = sum(computer_card)

print(f"Your final hand: {player_card}, final score: {pl_score}")
print(f"Computer's final hand: {computer_card}, final score: {com_score}")

calculate_score(pl_score, com_score)