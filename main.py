import random

wordlist = ("processor", "graphics", "mouse", "monitor", "cable", "keyboard",
            "server", "networking", "firewall", "code", "programming",
            "storage", "fiber", "client", "compile", "computer", "laptop")

word = random.choice(wordlist)
underscores = ["_"] * len(word)
print(" ".join(underscores))
points = 0

while True:
    letter = input("Enter a letter: ")
    if letter in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == letter:
                underscores[i] = letter
        print(" ".join(underscores))
    else:
        print("Incorrect.")
