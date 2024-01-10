#
# ROCK, PAPER, SCISSORS - Iterācija 1
# 
# 1. Spēle prasa ievadīt ciparu no 1 līdz 3 (izmanto input, https://www.w3schools.com/python/python_user_input.asp)
# 2. Dators iedomājas ciparu no 1 līdz 3  (izmanto random, https://www.w3schools.com/python/ref_random_randint.asp)
# 3. Atkarībā no ievadītajiem cipariem un datora, izdrukā paziņojumu par zaudējumu, uzvaru, vai neizšķirtu (izmanto if, else https://www.w3schools.com/python/python_conditions.asp)
#

ROCK = "1"
SCISSOR = "2"
PAPER = "3"

print("｡☆✼★━━━━━━━━━━━━★✼☆｡")
print("Welcome to Rock, Paper, Scissors!")
print("Make your move by writing your choice with the coresponding number: Rock = 1, Scissors = 2, Paper = 3.")
print("｡☆✼★━━━━━━━━━━━━★✼☆｡")
choice = input("Enter your choice:")
print("You picked:" + choice)


import time

time.sleep(0.5)
print("Rock")
time.sleep(0.5)
print("Paper")
time.sleep(0.5)
print("Scissors")
time.sleep(0.5)
print("Shoot!")
time.sleep(0.5)

import random

result = str(random.randint(1, 3))
print("Computer chose option: " + result)  

time.sleep(0.7)

if choice == result:
    print("It's a draw! Try playing again.")

elif choice == "1" and result == "3": 
    print("Computer picked Paper, you lost!")
elif choice == "1" and result == "2":
    print("Computer picked Scissors, you won!")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░   ░░░░░░   ░░░░░     ░░░░░░   ░░░░░   ░░░░░░░   ░░░░░░░░   ░   ░    ░░░░░   ░   ░░░░░░")
    print("▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒  ▒   ▒▒▒   ▒   ▒▒▒▒▒▒")
    print("▒▒▒   ▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒  ▒▒▒   ▒   ▒   ▒   ▒▒   ▒   ▒▒▒▒▒▒")
    print("▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓   ▓   ▓   ▓▓   ▓   ▓  ▓▓▓▓▓▓▓")
    print("▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓  ▓   ▓   ▓   ▓   ▓▓▓  ▓   ▓  ▓▓▓▓▓▓▓")
    print("▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓  ▓  ▓▓▓▓     ▓   ▓   ▓▓▓▓  ▓  ▓▓▓▓▓▓▓▓▓▓")
    print("█████   ██████████     ████████      ██████████   ████████   █   █   ██████   █   ██████")
    print("████████████████████████████████████████████████████████████████████████████████████████")

elif choice == "2" and result == "1":
    print("Computer picked Rock, you lost!")
elif choice == "2" and result == "3":
    print("Computer picked Paper, you won!")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░   ░░░░░░   ░░░░░     ░░░░░░   ░░░░░   ░░░░░░░   ░░░░░░░░   ░   ░    ░░░░░   ░   ░░░░░░")
    print("▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒  ▒   ▒▒▒   ▒   ▒▒▒▒▒▒")
    print("▒▒▒   ▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒  ▒▒▒   ▒   ▒   ▒   ▒▒   ▒   ▒▒▒▒▒▒")
    print("▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓   ▓   ▓   ▓▓   ▓   ▓  ▓▓▓▓▓▓▓")
    print("▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓  ▓   ▓   ▓   ▓   ▓▓▓  ▓   ▓  ▓▓▓▓▓▓▓")
    print("▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓  ▓  ▓▓▓▓     ▓   ▓   ▓▓▓▓  ▓  ▓▓▓▓▓▓▓▓▓▓")
    print("█████   ██████████     ████████      ██████████   ████████   █   █   ██████   █   ██████")
    print("████████████████████████████████████████████████████████████████████████████████████████")
elif choice == "3" and result == "1":
    print("Computer picked Rock, you won!")
    print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    print("░   ░░░░░░   ░░░░░     ░░░░░░   ░░░░░   ░░░░░░░   ░░░░░░░░   ░   ░    ░░░░░   ░   ░░░░░░")
    print("▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒  ▒   ▒▒▒   ▒   ▒▒▒▒▒▒")
    print("▒▒▒   ▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒  ▒▒▒   ▒   ▒   ▒   ▒▒   ▒   ▒▒▒▒▒▒")
    print("▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓   ▓▓▓   ▓   ▓   ▓▓   ▓   ▓  ▓▓▓▓▓▓▓")
    print("▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓  ▓   ▓   ▓   ▓   ▓▓▓  ▓   ▓  ▓▓▓▓▓▓▓")
    print("▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓  ▓  ▓▓▓▓     ▓   ▓   ▓▓▓▓  ▓  ▓▓▓▓▓▓▓▓▓▓")
    print("█████   ██████████     ████████      ██████████   ████████   █   █   ██████   █   ██████")
    print("████████████████████████████████████████████████████████████████████████████████████████")
elif choice == "3" and result == "2":
    print("Computer picked Scissors, you lost!")

    
