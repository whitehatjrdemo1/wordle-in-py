
from xml.etree.ElementTree import iselement
from numpy import equal
from cv2 import correctMatches
import random


def checkword(word, lst):
    for w in lst:
        if word == w.strip():
            return True
    print("That word does not exist")
    return False


def checklen(n):
    if n == no_of_letters:
        return True
    else:
        print("That word is not the correct length")

        return False


no_of_letters = int(input("type any number from 4 to 7 to choose level "))

if no_of_letters == 5:
    file_name = "sgb-words.txt"
# add else ifs of other numbers and repository file paths
f = open(file_name)
words = f.readlines()
# print(words)
len_words = len(words)
num = random.randint(0, len_words)
gameover = False
word_ans = words[num]
word_ans = str(word_ans).strip()

tries = 0
i, j = 0, 0
correct_position = []
correct_letter = []
print(word_ans)  # comment off this line later
while tries < 6 and not gameover:
    print(gameover, tries)
    current_guess = input(
        f"Enter your guess of the word of {no_of_letters} letters")

    correct_letter = []
    correct_position = []
    i = 0
    tries = tries+1
    print(current_guess, word_ans)
    current_guess = str(current_guess).strip()
    if checklen(len(current_guess)) and checkword(current_guess, words):

        if current_guess == word_ans:
            gameover = True
            print(f"Congratulations! you win in {tries}/6 tries")
        elif tries < 6:
            while i < len(word_ans):
                j = 0
                if word_ans[i] == current_guess[i]:
                    correct_position.append(i+1)
                    print(f"{current_guess[i]}", end=" ")
                else:
                    print(f"_", end=" ")

                    while j < len(current_guess):
                        if word_ans[i] == current_guess[j]:
                            if current_guess[j] in correct_letter:
                                break

                            correct_letter.append(current_guess[j])
                        j = j+1

                i = i+1
            if len(correct_position) == 0:
                print(f"Sorry none of the letter were in the correct positions")
            else:
                print(
                    f"\nPositions {correct_position} were the correct letters in the correct positions")

            if len(correct_letter) == 0 and len(correct_position) == 0:
                print(f"Sorry none of the letters match")
            else:
                print(
                    f"\n{correct_letter} were the correct letters but in incorrect positions")

            print(f"Sory! Take another guess")
        else:
            print(f"Sorry you lose, the word is {word_ans}")
    else:
        tries = tries - 1
        print(f"Please try again!")
