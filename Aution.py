print("Welcome to the Auction!")

bidders = {}

ans = "yes"
while ans.lower() == "yes":
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))
    ans = input("Do you have more bidders? (yes/no): ")
    bidders[name] = bid

highest = 0
for key in bidders:
    if bidders[key] > highest:
        highest = bidders[key]

for key in bidders:
    if bidders[key] == highest:
        print(f"The auction won by {key} with the bid of ${bidders[key]}")
        break
