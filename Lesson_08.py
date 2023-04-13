#######################################
# 2023.03.30.
# Dávid
# Python Basic - 8th Lesson
#######################################


# 1. feladat
print("\n---------1. feladat---------")

import time
# Hangman game

puzzle = "logiscool"

my_solution = "*********"

correct_letters = []
incorrect_letters = []
life = 10

while life > 0 and puzzle != my_solution:
    print(my_solution)
    tip = input("Tip a new letter:\n")
    if len(tip) == len(puzzle):
        print("You try to guess the solution... and your guess is...")
        time.sleep(1)

        if tip == puzzle:
            print("Correct!")
            my_solution = tip
        else:
            print("Sorry, but this isn't your day.")
            life -= 1
            print("Number of lives left: " + str(life))
    else:

        found_something = False
        for i in range(len(puzzle)):
            if puzzle[i] == tip:
                my_solution_list = list(my_solution)
                my_solution_list[i] = tip
                my_solution = "".join(my_solution_list)
                found_something = True

        if not found_something:
            incorrect_letters.append(tip)
            life -= 1
            print("Number of lives left: " + str(life))
        else:
            correct_letters.append(tip)

    print("List of the correct letters: " + str(correct_letters))
    print("List of the incorrect letters: " + str(incorrect_letters))

if life > 0:
    print("Congratulations!")
else:
    print("Maybe next time...")


# 2. feladat
print("\n---------2. feladat---------")

# A legnagyobb közös osztó - Greatest common divisor

num_1 = int(input("Enter the first number:\n"))
num_2 = int(input("Enter the second number:\n"))
gcd = 1

for i in range(1, num_1+1):
    if num_1 % i == 0 and num_2 % i == 0:
        gcd = i

print("The greatest common divisor of " + str(num_1) + " and " + str(num_2) + " is: " + str(gcd))
