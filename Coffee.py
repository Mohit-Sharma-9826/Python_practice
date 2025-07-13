resources = {"water": 3000, "coffee": 500, "milk": 1000, "money": 0}

coffees = {"expresso": {"water": 50, "coffee": 18, "milk": 0, "price": 1.0}, 
           "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 1.5},
           "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 2.5}
           }

def check(ask):
    global coffees
    global resources

    coffee = coffees[ask.lower()]
    items = ["water", "coffee", "milk"]
    for item in items:
        if resources[item] < coffee[item]:
            return False
    return True

Ques = "y"
while Ques in "Yy":
    ask = input("What would your like? (Expresso/ Latte/ Cappuccino): ")
    if ask.lower() in ["expresso", "latte", "cappuccino"]:
        print("Please insert coins.")
        quar = int(input("How many Quarters?: "))
        dime = int(input("How many Dimes?: "))
        nic = int(input("How many Nickles?: "))
        penny = int(input("How many Pennies?: "))
        total = quar*0.25 + dime*0.1 + nic*0.05 + penny*0.01

        price = coffees[ask.lower()]["price"]

        if total > price:
            if not check(ask):
                print("Sorry Insufficent items!😞😞")
                print(f"Here is your ${total: .3f} change.")
            else:
                print(f"Here is ${(total-price): .3f} change.")
                total = price

        if total == price and check(ask):
            resources["water"] -= coffees[ask.lower()]["water"]
            resources["coffee"] -= coffees[ask.lower()]["coffee"]
            resources["milk"] -= coffees[ask.lower()]["milk"]
            resources["money"] += price
            print(f"Here is your {ask} coffee.🍵")
            
        if total < price:
            print("Insufficient coins!")
            print(f"Here is your ${total: .3f} change.")

    if ask.lower() == "report":
        print("Water: ", resources["water"], "ml")
        print("Coffee: ", resources["coffee"], "g")
        print("Milk: ", resources["milk"], "ml")
        print("Money: $", resources["money"])
    
    Ques = input("Something else? (Y/N): ")


