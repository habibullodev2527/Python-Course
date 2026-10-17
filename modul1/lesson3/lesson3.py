# 1-topshiriq 

# Berilgan listga "Orange" elementini qo'shing.

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
print(fruits)

# 2-topshiriq

# Berilgan listdan "Blue" elementini o'chiring.

colors = ["Red", "Blue", "Green", "Yellow"]
colors.remove("Blue")
print(colors)


# 3-topshiriq 

# Berilgan list elementlarini teskari tartibda joylashtiring.

numbers = [10, 20, 30, 40, 50]
numbers = numbers[::-1]
print(numbers)


# 4-topshiriq

# Tuple ichida nechta "Python" elementi mavjudligini aniqlang.

languages = ("Python", "Java", "Python", "C++", "Python")
counter = languages.count("Python")
print(counter)


# 5-topshiriq 

# Tuple ichida "SQL" elementining indeksini toping.

courses = ("Excel", "Python", "SQL", "Power BI", "Tableau")
index = courses.index("SQL")
print(index)