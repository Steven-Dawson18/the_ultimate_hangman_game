import random

with open("dragon_words.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    picked = random.choice(words).upper()
    print(picked)