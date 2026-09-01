#%%
import random

popular_people = [
    {
        "name": "Cristiano Ronaldo",
        "occupation": "Professional Footballer",
        "followers": 668 ,
        "place_of_origin": "Funchal, Madeira, Portugal"
    },
    {
        "name": "Lionel Messi",
        "occupation": "Professional Footballer",
        "followers": 510 ,
        "place_of_origin": "Rosario, Argentina"
    },
    {
        "name": "Selena Gomez",
        "occupation": "Singer and Actress",
        "followers": 417 ,
        "place_of_origin": "Grand Prairie, Texas, USA"
    },
    {
        "name": "Kylie Jenner",
        "occupation": "Media Personality and Entrepreneur",
        "followers": 393 ,
        "place_of_origin": "Los Angeles, California, USA"
    },
    {
        "name": "Dwayne 'The Rock' Johnson",
        "occupation": "Actor and Professional Wrestler",
        "followers": 392 ,
        "place_of_origin": "Hayward, California, USA"
    },
    {
        "name": "Ariana Grande",
        "occupation": "Singer-Songwriter and Actress",
        "followers": 374 ,
        "place_of_origin": "Boca Raton, Florida, USA"
    },
    {
        "name": "Kim Kardashian",
        "occupation": "Media Personality and Businesswoman",
        "followers": 355 ,
        "place_of_origin": "Los Angeles, California, USA"
    },
    {
        "name": "Beyoncé",
        "occupation": "Singer-Songwriter and Actress",
        "followers": 310 ,
        "place_of_origin": "Houston, Texas, USA"
    },
    {
        "name": "Justin Bieber",
        "occupation": "Singer-Songwriter",
        "followers": 294 ,
        "place_of_origin": "London, Ontario, Canada"
    },
    {
        "name": "Taylor Swift",
        "occupation": "Singer-Songwriter",
        "followers": 280 ,
        "place_of_origin": "West Reading, Pennsylvania, USA"
    },
    {
        "name": "Virat Kohli",
        "occupation": "Professional Cricketer",
        "followers": 273 ,
        "place_of_origin": "New Delhi, India"
    },
    {
        "name": "Neymar Jr.",
        "occupation": "Professional Footballer",
        "followers": 231 ,
        "place_of_origin": "Mogi das Cruzes, São Paulo, Brazil"
    },
    {
        "name": "Jimmy Donaldson (MrBeast)",
        "occupation": "YouTuber and Content Creator",
        "followers": 350,
        "place_of_origin": "Wichita, Kansas, USA"
    },
    {
        "name": "Khaby Lame",
        "occupation": "TikTok Content Creator",
        "followers": 162 ,
        "place_of_origin": "Ziguinchor, Senegal"
    },
    {
        "name": "Charli D'Amelio",
        "occupation": "Social Media Personality and Dancer",
        "followers": 156 ,
        "place_of_origin": "Norwalk, Connecticut, USA"
    }
]

# Next Random Person Generator
def PullRan():
    Ran_Person = random.choice(popular_people)
    return(Ran_Person)

# Print Details
def PrintDetails(num,Dct):
    First_Second = "A"
    name = Dct["name"]
    occupation = Dct["occupation"]
    place = Dct["place_of_origin"]      # 0 is First and 1 is Second

    if num == 1:
        First_Second = "B"
    print(f"Person {First_Second} is {name}. They are a {occupation}. \nThey live in {place}")

    return Dct["followers"]

# Getting First Record of Person
first = PullRan()
second = PullRan()
count = 0

# Main game
while True:
    print("Guess the person with higher follower count. \n")
    first_tot = PrintDetails(0,first)
    second_tot = PrintDetails(1,second)
    user_in= input("Select A(a) or B(a) or quit(q). ")

    if user_in.lower() == "q":
        break

    # Comparing persons
    if user_in.lower() == 'a' and first_tot>second_tot:
        count += 1
        print(f"You're right. They have {first_tot}M and {second_tot}M followers respectively.")
        print(f"Current Score: {count}")
    elif user_in.lower() == 'b' and first_tot<second_tot:
        count += 1
        print(f"You're right. They have {first_tot} and {second_tot} respectively.")
        print(f"Current Score: {count}")
    else:
        print(f"You lose. They have {first_tot} and {second_tot} respectively.")
        print(f"Total Score: {count}")
        break

    # Retaking new persons for next round
    if first_tot>second_tot:
        second = PullRan()
    else:
        first = second
        second = PullRan()
# %%
