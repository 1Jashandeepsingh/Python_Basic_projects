import random

subjects = [
    "Shahrukh khan",
    "virat Kohloi",
    "Nirmla SithaRama",
    "A Mumbai cat",
    "A Group of Monkeys",
    "Prime Minister modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "Mumbai Local",
    "a Plate of samosa",
    "inside Parliament",
    "at Ghanga Ghaat",
    "during IPL Match",
    "at India Gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"Breaking News : {subject} {action} {places_or_thing}"
    print("\n", headline)

    user_input = input("\n Do you want another headline? (yes/no)".strip().lower())
    if user_input == "no":
        break

print("\n Thanks for using the fake news headliner. Have fun today!")