#######################################
# 2023.04.27.
# Dávid
# Python Basic - 11th Lesson
#######################################


# 1. feladat
print("\n---------1. feladat---------")

for i in range(1, 11):
    for j in range(i):
        print(i, end=" ")
    print("")

# 2. feladat
print("\n---------2. feladat---------")

"""
Keressük meg azokat a számokat 1500 és 2500 között, amelyek oszthatóak 7-el és 4-el is.
A megkeresett elemeket írassuk ki.
"""
div_w_4 = []
div_w_7 = []

for i in range(1501, 2500, 4):
    if i % 7 == 0:
        div_w_7.append(i)

for i in range(1501, 2500):
    if i % 7 == 0 and i % 4 == 0:
        div_w_4.append(i)

if div_w_4 == div_w_7:
    print("Both lists have the same elements.")
else:
    print("There are different elements.")


# 3. feladat
print("\n---------3. feladat---------")

vezeteknev = ["Kovács", "Kerekes", "Tóth", "Nagy"]
keresztnev = ["Petúnia", "István", "Rajmond", "Evelin"]

for i in vezeteknev:
    for j in keresztnev:
        print(i, j)

# 4. feladat
print("\n---------4. feladat---------")

names = ["Harry", "Hermione", "Ronald", "Dumbledore", "Neville"]

for i in range(len(names)):
    for j in range(len(names)):
        if i < j:
            print(names[i] , " and ", names[j])


# 5. feladat
print("\n---------5. feladat---------")


my_number = int(input("Give me a number: "))
prime_divisors = []

for i in range(1, my_number+1):
    if my_number % i == 0:
        prime_divisors.append(i)

if len(prime_divisors) > 2:
    print(str(my_number) + " is not a prime number because it has " + str(len(prime_divisors))
          + " divisors. These divisors are: " + str(prime_divisors))
elif len(prime_divisors) == 1:
    print("The number is 1.")

else:
    print(str(my_number) + " is prime because it has " + str(len(prime_divisors))
          + " divisors, one and itself.")




# 6. feladat
print("\n---------6. feladat---------")
names = ["Aladár", "Baladár", "Jobbadár", "Szaladár"]
goals = [6, 2, 5, 7]
# hibázások
faults = [3, 1, 7, 2]

# Legtöbb gólt szerzett játékos
top_score = max(goals)
ts_index = goals.index(top_score)

print("Top-scorer: ", names[ts_index])

print("Version 2, Top-Scorer: ", names[goals.index(max(goals))])

"""
Az előbbi módszer alapján írassuk ki annak a nevét, aki a legkevesebbet hibázott.
"""

least_faults = min(faults)
lf_index = faults.index(least_faults)

print("Least-Faults: ", names[lf_index])

print("Version 2, Least-faults: ", names[faults.index(min(faults))])




average = []
for i in range(len(goals)):
    average.append( goals[i] - faults[i] )

print("All averages", average)

print("The best in average ", names[average.index(max(average))] ,
      " with an average of ", average[average.index(max(average))])

"""
1) Bővítsük ki a listákat több adattal.
2) Nézzük meg, hogy ugyanolyan hosszúak-e a listák.
3) Keressük meg azokat a játékosokat, akik 5-től több gólt lőttek, de 2-nél kevesebbszer hibáztak.
"""