import random

wordlist = ("processor", "graphics", "mouse", "monitor", "cable", "keyboard",
            "server", "networking", "firewall", "code", "programming",
            "storage", "fiber", "client", "compile", "computer", "laptop")

word = random.choice(wordlist)
underscores = ["_"] * len(word)
print(" ".join(underscores))
points = 0
wrong = 0

while True:
    letter = input("Enter a letter: ")
    if letter in word:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == letter:
                underscores[i] = letter
                if "_" not in underscores:
                    print("You completed the word! You win!")
                    break
        print(" ".join(underscores))
        print("Thats correct!")
    else:
        print("Incorrect.")
        wrong += 1
        if wrong == 6:
            print("You've missed 6 times, you lose.")
            break
