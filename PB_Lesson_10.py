#######################################
# 2023.04.20.
# Dávid
# Python Basic - 10th Lesson
#######################################


# 1. feladat
print("\n---------1. feladat---------")

myList = []
for i in range(5):
    myList.append(i)

for j in myList:
    print(j)

# 2. feladat
print("\n---------2. feladat---------")

a = input("a: ")
b = input("b: ")
c = input("c: ")

print(a, b, c)
print(a, b, c, sep="-")

# 3. feladat
print("\n---------3. feladat---------")

# Átváltás / Konvertálás
"""
type = input("Konvertálási típus (kg) (c) (km):")

if type == "kg":
    x = float(input("Érték megadása: "))
    unit = input("Egység (kg) (g):")
    if unit == "kg":
        print(str(x) + " kg in g " + str(x * 1000))
    elif unit == "g":
        print(str(x) + " g in kg " + str(x / 1000))
    else:
        print("Not a real unit!")

elif type == "c":
    x = float(input("Érték megadása: "))
    unit = input("Egység (C) (F):")
    if unit == "C":
        print(str(x) + " celsius in Fahrenheit " + str(x*1.8+32))
    elif unit == "F":
        print(str(x) + " Fahrenheit in celsius " + str((x-32) / 1.8 ))
    else:
        print("Not a real unit!")

elif type == "km":
    x = float(input("Érték megadása: "))
    unit = input("Egység (km) (miles):")
    if unit == "km":
        print(str(x) + " km in miles " + str(x*0.621))
    elif unit == "miles":
        print(str(x) + " miles in km " + str(x/0.621))
    else:
        print("Not a real unit!")

else:
    print("Nincs ilyen konvertálási típus!")

"""

# 4. feladat
print("\n---------4. feladat---------")

# Időszámítás
"""
time = input("Start time: ")
duration = int(input("Duration (min):"))
hour, minutes = time.split(":")

time_minutes = int(hour) * 60 + int(minutes)

# Vég (percben) = Jelenlegi idő (percben) + időtartam
end_minutes = time_minutes + duration
end_hours = (end_minutes // 60) % 24
end_min = end_minutes - (end_minutes // 60) * 60

print("End time: " + str(end_hours) + ":" + str(end_min))
"""

# 5. feladat
print("\n---------5. feladat---------")

# Jelszó ellenőrző

password = input("Jelszó:\n")
spec_char = ["&", "@",  "!", "+", "-", "$"]
if 6 <= len(password) <= 16:
    print("The length is good. :)")

lower = False
upper = False
digit = False
spec_c = False

for char in password:
    if char.islower():
        # print("There is a lower-case letter.")
        lower = True
    if char.isupper():
        # print("There is a upper-case letter.")
        upper = True
    if char.isdigit():
        # print("There is a digit in the password.")
        digit = True
    if char in spec_char:
        # print("There is a spec character.")
        spec_c = True

if lower and upper and digit and spec_c:
    print("This is a very strong password! :O")
else:
    print("This password is poor...")