import random
data = [
    {
        "name": "Cristiano Ronaldo",
        "followers_count": 620000000,
        "description": "Professional footballer and international sports icon",
        "country": "Portugal"
    },
    {
        "name": "Taylor Swift",
        "followers_count": 290000000,
        "description": "Singer-songwriter known for storytelling in pop and country music",
        "country": "USA"
    },
    {
        "name": "Virat Kohli",
        "followers_count": 265000000,
        "description": "Indian cricketer and one of the top batsmen in the world",
        "country": "India"
    },
    {
        "name": "Lionel Messi",
        "followers_count": 480000000,
        "description": "Argentine footballer and global sports legend",
        "country": "Argentina"
    },
    {
        "name": "Kim Kardashian",
        "followers_count": 360000000,
        "description": "Reality TV star, entrepreneur, and beauty influencer",
        "country": "USA"
    },
    {
        "name": "Zendaya",
        "followers_count": 210000000,
        "description": "Actress, singer, and fashion icon",
        "country": "USA"
    },
    {
        "name": "Selena Gomez",
        "followers_count": 430000000,
        "description": "Actress and singer, known for her global music hits and advocacy",
        "country": "USA"
    },
    {
        "name": "Narendra Modi",
        "followers_count": 190000000,
        "description": "Prime Minister of India and political leader",
        "country": "India"
    },
    {
        "name": "Dwayne Johnson",
        "followers_count": 380000000,
        "description": "Actor and former professional wrestler, known as 'The Rock'",
        "country": "USA"
    },
    {
        "name": "Blackpink",
        "followers_count": 110000000,
        "description": "South Korean girl group known for global music success",
        "country": "South Korea"
    }
]

print(r"""
  _    _ _       _               
 | |  | (_)     | |              
 | |__| |_  __ _| |__   ___ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__|
 | |  | | | (_| | | | |  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|   
            __/ |                
           |___/     """, end = '')
print(r"""
                      _       ___  __        __ _____  _____  
                     | |     / _ \ \ \      / /| ____||  __ \ 
                     | |    | | | | \ \ /\ / / |  _|  | |__) |
                     | |___ | |_| |  \ V  V /  | |___ |  _  / 
                     |_____| \___/    \_/\_/   |_____||_| \_\
""")


vs = r"""
__      __   _____ 
\ \    / /  / ____|
 \ \  / /  | (___  
  \ \/ /    \___ \ 
   \  /     ____) |
    \/     |_____/ 
"""

score = 0
flag = 0

for i in range(5):
    opt1 = random.choice(data)
    opt2 = random.choice(data)
    while opt1 == opt2:
        opt2 = random.choice(data)

    if i>0:
        print(f"Your score is {score}")
    print(f"Compare A: {opt1["name"]}, {opt1["description"]}, {opt1["country"]}")
    print(vs)
    print(f"Against B: {opt2["name"]}, {opt2["description"]}, {opt2["country"]}")

    ask = input("Who has more followers? Type 'A' or 'B': ")
    if ask.lower() == "a" and opt1["followers_count"] > opt2["followers_count"]:
        score += 1
    elif ask.lower() == "b" and opt1["followers_count"] < opt2["followers_count"]:
        score += 1
    else:
        flag = 1
        break

if flag == 1:
    print("You are wrong! Your score is", score)
else:
    print("Your score is", score)
    print("You won this match😊😊")

