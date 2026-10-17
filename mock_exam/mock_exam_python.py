##################### ---------- TASK 1 ----------

# Write a Python program that checks whether a given word starts and ends with the same letter.

# If the first and last letters are the same, print:

# Same

# Otherwise, print:

# Different
# Example 1

# Input:

# level

# Output:

# Same
# Input:

# python

# Output:

# Different


#solution

# word = input("So'zni kiriting: ")

# if word[0] == word[-1]:
#     print("Same")
# else:
#     print("Different")


##################### ---------- TASK 2 ----------

# Write a Python script to create a dictionary where the keys are numbers between 1 and 10 (both included) and the values are the cube of the keys.

# Expected Output:

# {
# 1:1,
# 2:8,
# 3:27,
# 4:64,
# 5:125,
# 6:216,
# 7:343,
# 8:512,
# 9:729,
# 10:1000
# }

#solution

# cube_numbers = {}

# for i in range(1, 11):
#     cube_numbers[i] = i ** 3

# print(cube_numbers)


##################### ---------- TASK 3 ----------

# Given an integer n, perform the following actions:

# If n is divisible by both 3 and 5, print FizzBuzz
# If n is divisible only by 3, print Fizz
# If n is divisible only by 5, print Buzz
# Otherwise, print the number itself.


#solution

# n = int(input("n = "))

# if n % 3 == 0 and n % 5 == 0:
#     print("FizzBuzz")
# elif n % 3 == 0:
#     print("Fizz")
# elif n % 5 == 0:
#     print("Buzz")
# else:
#     print(n)

##################### ---------- TASK 4 ----------

# Print the following number pattern:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

#solution

##################### ---------- TASK 5 ----------

# Write a function that prints all multiples of 3 that do not exceed a given number N.

# Example:

# Input:

# 20

# Output:

# 3 6 9 12 15 18


#solution

def multiples_of_3(n: int): 
    for i in range(3, n + 1):
        if i % 3 == 0:
            print(i)
            
multiples_of_3(20)