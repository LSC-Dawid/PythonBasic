#######################################
# 2023.05.04.
# Dávid
# Python Basic - 12th Lesson
#######################################


# 1. feladat
print("\n---------1. feladat---------")

length_of_list = 1
numbers = []

while length_of_list > 0:
    new_number = int(input("Enter a number: \n"))
    numbers.append( new_number )
    length_of_list -= 1

print(numbers)

"""
Önálló feladat:
Külön változókba gyűjtsük ki a következő típusok darabszámát:
    -pozitív számok
    -negatív számok
    -nulla
    
    -páros
    -pátarlan
"""

pos_num = 0
neg_num = 0
zeros = 0

even = 0
odd = 0

i = 0
while i < len(numbers):
    if numbers[i] > 0:
        pos_num += 1
    elif numbers[i] < 0:
        neg_num += 1
    else:
        zeros += 1

    if numbers[i] % 2 == 1:
        odd += 1
    else:
        even += 1

    i += 1


print("Number of positive numbers: ", pos_num, "\nNumber of negative numbers: ", neg_num , "\nNumber of zeros: ", zeros, "\nNumber of odd numbers", odd, "\nNumber of even number", even )


# 2. feladat
print("\n---------2. feladat---------")

lista = [56, 34, 156, 67]

lista.pop()
lista.pop(0) # 34, 156
# pop (-1) elem kivétel az utolsó helyről
lista.pop(-1) # 34

# megadott helyre való érték beszúrás
lista.insert(0, 99)
lista.insert(0, 99)
lista.insert(0, 99)
lista.insert(0, 444)
lista.insert(0, 123) # 123, 444, 99,99, 99, 34

print(lista[:2])
print(lista[2:])
print(lista[1:4])

# érték törlés
lista.remove(99)

print(lista)





# 3. feladat
print("\n---------3. feladat---------")

import random

myNumbers = []
newNumbers = []

for i in range(15):
    myNumbers.append( random.randint(1, 5) )

print( myNumbers )
duplicated_numbers = 0

for i in myNumbers:

    if i not in newNumbers:
        newNumbers.append( i )
    else:
        duplicated_numbers += 1

print("Numbers:", newNumbers, "\nDuplicated number of numbers: ", duplicated_numbers)



# 4. feladat
print("\n---------4. feladat---------")

myList = [4, 5, 7.2, 9, 0, 5.6, True, False, "Star Wars"]

# Listát fűz hozzá
# myList.append(["Hello", "Logiscool"])

# Listába több elem hozzáfűzése
myList.extend([504, "Hello", "Logiscool"])

print(myList)