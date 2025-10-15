import random

easy_words = ["apple" , "train" , "tiger" , "money" , "India"]
medium_words = ["python" , "bottle" , "monkey" , "plant" , "laptop"]
hard_words = ["elephant" , "diamond" , "umbrella" , "computer" , "mountain"]

print("Welcome to the password guessing game")


level = input("Enter the difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invaild choice. Defaultin to easy Level!")
    secret = random.choice(easy_words)

attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess : ").lower()
    attempts+=1

    if guess == secret:
        print(f"congratulations! You guess it in {attempts} attempts.")
        break

    hint = ""
    for i in range(len(secret)):
        if i<len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint+="_"
    
    print("Hint : " , hint)
print("game over!")

