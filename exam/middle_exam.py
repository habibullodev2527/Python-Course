



### Python middle exam
##
#



##################### ---------- TASK 1 ---------- ################################


# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

# Example: kiyik, aziza

word = input("So'zni kiriting: ")

if word == word[::-1]:
    print(f"{word}- palindrome so'z!")
else:
    print(f"{word}- palindrome so'z emas!")

##################### ---------- TASK 2 ---------- ################################


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values 
# are the square of the keys.

# Expected_output = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

numbers = {}

for i in range(1, 16):
    numbers[i] = i ** 2
    
print(numbers)


##################### ---------- TASK 3 ---------- ##################################

# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# Example:
# Input:
# 3
# Output:
# Weird

n = int(input('n = '))

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
else:
    print(f"{n} kiritdingiz. Boshqa son kiriting!")


##################### ---------- TASK 4 ---------- ################################



# Print reverse number pattern

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

##################### ---------- TASK 5 ---------- ##################################


# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) 
# chop etuvchi funksiyani yozing.

# Misol:
# Kiritish:
# 10
# Natija:
# 2 4 8
# (Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)


def power_of_2(n):
    for i in range(1, n + 1):
        if 2 ** i <= n:
            print(2 ** i, end=" ")
            
n = int(input("n = "))
power_of_2(n)

