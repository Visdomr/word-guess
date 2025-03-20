import random
import string

wordlist = ("processor", "graphics", "mouse", "monitor", "cable", "keyboard",
            "server", "networking", "firewall", "code", "programming",
            "storage", "fiber", "client", "compile", "computer", "laptop")

while True:
    word = random.choice(wordlist)
    underscores = ["_"] * len(word)
    wrong = 0
    print(" ".join(underscores))

    while True:
        letter = input("Enter a letter: ")
        if letter in word:
            print("Correct!")
            for i in range(len(word)):
                if word[i] == letter:
                    underscores[i] = letter
            print(" ".join(underscores))
            if "_" not in underscores:
                print("You completed the word! You win!")
                break
        else:
            print("Incorrect.")
            wrong += 1
            print("Wrong guesses:", wrong, "/6")
            if wrong == 6:
                print("You've missed 6 times, you lose. The word was:", word)
                break

    while True:
        play_again = input(
            "Would you like to continue playing? yes/no, y/n: ").lower()
        if play_again == "y" or play_again == "yes":
            break
        elif play_again == "n" or play_again == "no":
            print("Thanks for playing! Goodbye.")
            exit()
        else:
            print("Please enter yes or no, y or n only.")
