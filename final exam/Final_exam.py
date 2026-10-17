# 1. You have a list which contains country names. you need to sort this list according to the length of elements ascending order
# 	ls = ['Uzbekistan','USA','UK','Germany','Chine']
# expected output: ['UK','USA,'Chine','Germany','Uzbekistan']

ls = ['Uzbekistan','USA','UK','Germany','Chine']

ls.sort(key=len)

print(ls)

# 2.Write a Python program to find the indexes of numbers in a following list below a given threshold.
# 	ls = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
# 	threshold = 100
# 	expected output: [0, 1, 2, 3, 7, 8, 9, 10]

ls = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
threshold = 100
result = []

for i in range(len(ls)):
        if ls[i] < threshold:
                result.append(i)
                
print(result)

# 3.Write a recursive function to find the sum of the digits of a number.

def sum_of_digits(n):
        if n == 0:
                return 0
        return n % 10 + sum_of_digits(n // 10)

n = int(input('n = '))
print(sum_of_digits(n))

# task 4
# -----------------------------------------------------------------------------------------------------
#       Using student.json file, create CSV file called student.csv with following columns like ID,Name,Age

import json
import csv

with open('student.json', 'r') as file:
        student = json.load(file)
        
result = []

for i in range(len(student['Students'])):
        data = {
                'ID': student['Students'][i]['ID'], 
                'Name': student['Students'][i]['Name'], 
                'Age': student['Students'][i]['Age']
        }
        
        result.append(data)

print(result)

with open('student.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Age'])
        
        writer.writeheader()
        writer.writerows(result)

# task 5
# -----------------------------------------------------------------------------------------------------
#       using employee_data.csv file.
        # task 1. Create 4 separate csv file for 4 different countries
        # task 2. Find the Most Experienced Employee in Each Country
        # task 3. Find Employees Earning Above Their Country’s Average Salary

import pandas as pd

employee_data = pd.read_csv('employee_data.csv')

# 1. CSV file yaratish

for country, data in employee_data.groupby('Birth_Country'):
        data.to_csv(f"{country}.csv", index=False)
        
# 2. Har bir Countrydagi eng tajribali employee

employee_data['HireDate'] = pd.to_datetime(employee_data['HireDate'])

most_experienced = employee_data.loc[
        employee_data.groupby('Birth_Country')['HireDate'].idxmin()
]

print(most_experienced[['EmpName', 'HireDate']])

# 3. O‘z mamlakatidagi o‘rtacha ish haqidan yuqori maosh oluvchi xodimlar

above_average = employee_data[
        employee_data['Salary'] > employee_data.groupby('Birth_Country')['Salary'].transform('mean')
        ]

print(above_average)