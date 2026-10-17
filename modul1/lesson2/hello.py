# Task1

name = input("Ismingizni kiriting: ")
year_of_birth = int(input("Tug'ilgan yilingizni kiriting: "))
age = 2026 - year_of_birth
print(f"""
        Ism - {name}, {age} yoshda
      """)


# Task2

txt = "LMaasleitbtui"

txt1 = txt[0::2]
txt2 = txt[1::2]
print(txt1, txt2)


# task3

txt = "MsaatmiazD"

txt1 = txt[0::2]
txt2 = txt[-1::-2]
print(txt1, txt2)


# task4

txt = "I'am John. I am from London"

print(txt[21:])


# task5

txt = input("Satrni kiriting: ")

txt = txt[::-1]
print(txt)


# task6

import re

txt = input("Satrni kiriting: ")

counter = len(re.findall(r"[aeiou]", txt.lower()))
print(counter)


# task7

numbers = [23, 34, 12, 45, 65, 32, 4, 2]

max_num = max(numbers)
print(max_num)


# task8

txt = input("Satrni kiriting: ")

if txt == txt[::-1]:
    print(txt)
else:
    print("Kiritilgan so'z palindrom emas")


# task9

email = input("Email kiriting: ")

index = email.index("@")
domen = email[index + 1 :]

print(domen)


# task10

import random
import string

password = "".join(random.choices(string.ascii_letters + string.digits, k=10))

print(password)
