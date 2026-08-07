#1.
"""fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]

print("Fruit List:")
print(fruits) """


#2.
"""
numbers = [10, 20, 30, 40, 50]

print("First Element:", numbers[0])
print("Third Element:", numbers[2])
print("Last Element:", numbers[-1]) """

#3.
"""
colors = ["Red", "Blue", "Green", "Yellow", "Black"]

print("Original List:", colors)

colors[2] = "White"

print("Updated List:", colors)"""


#4.
"""
numbers = [10, 20, 30]

print("Original List:", numbers)

numbers.append(40)       # End
numbers.insert(0, 5)     # Beginning
numbers.insert(2, 15)    # Position

print("Updated List:", numbers) """


#5
"""
students = ["Amit", "Rahul", "Sneha", "Priya", "Rohan"]

print("Original List:", students)

students.pop(0)
students.pop()

students.remove("Sneha")

print("Remaining Students:", students)"""

#6.
""""
numbers = [23, 45, 12, 78, 56]

largest = numbers[0]
smallest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print("Largest:", largest)
print("Smallest:", smallest)"""

#7
"""
numbers = []

for i in range(10):
    num = int(input("Enter Number: "))
    numbers.append(num)

total = sum(numbers)
average = total / len(numbers)

print("Numbers:", numbers)
print("Sum:", total)
print("Average:", average)"""


#8
"""
numbers = []

for i in range(15):
    num = int(input("Enter Number: "))
    numbers.append(num)

even = 0
odd = 0

for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Numbers:", even)
print("Odd Numbers:", odd) """

#9.
"""
cities = ["Mumbai", "Pune", "Delhi", "Nagpur", "Nashik"]

city = input("Enter City Name: ")

if city in cities:
    print("City Found")
else:
    print("City Not Found")"""

#10.
"""
numbers = [10, 20, 30, 40, 50]

reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print("Original List:", numbers)
print("Reversed List:", reversed_list) """


#11.
"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 5 Elements:", numbers[:5])
print("Last 5 Elements:", numbers[5:])
print("Middle 4 Elements:", numbers[3:7])
print("Alternate Elements:", numbers[::2])
print("Reverse List:", numbers[::-1])
"""


#12.
"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80]

print("Elements at Even Index Positions:")

for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])
"""


#13.
"""
numbers = []

for i in range(10):
    num = int(input("Enter Number: "))
    numbers.append(num)

print("Original List:", numbers)

numbers.sort()

print("Ascending Order:", numbers)

numbers.sort(reverse=True)

print("Descending Order:", numbers)
"""


#14.
"""
numbers = [10, 20, 30, 20, 40, 10, 50]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original List:", numbers)
print("Unique Elements:", unique)
"""


#15.
"""
numbers = [10, 50, 30, 80, 60]

largest = numbers[0]
second = numbers[0]

for i in numbers:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest:", second)
"""


#16.
"""
students = [
    ["Rahul", 101, 85],
    ["Amit", 102, 90],
    ["Sneha", 103, 78]
]

for student in students:
    print("Name:", student[0])
    print("Roll Number:", student[1])
    print("Marks:", student[2])
    print()
"""


#17.
"""
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

result = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("Matrix Addition:")
for i in result:
    print(i)
"""


#18.
"""
cart = []

cart.append("Laptop")
cart.append("Mobile")
cart.append("Mouse")

print("Shopping Cart:", cart)

cart.remove("Mobile")

search = input("Search Item: ")

if search in cart:
    print("Item Found")
else:
    print("Item Not Found")

print("Final Cart:", cart)
print("Total Items:", len(cart))
"""


#19.
"""
students = ["Rahul", "Amit", "Sneha"]

print("Total Students:", len(students))

name = input("Search Student: ")

if name in students:
    print("Student Present")
else:
    print("Student Absent")

students.append("Rohan")

students.remove("Amit")

print("Updated Attendance List:", students)
"""


#20.
"""
books = ["Python", "Java", "C++"]

books.append("HTML")

print("Books:", books)

search = input("Search Book: ")

if search in books:
    print("Book Available")
else:
    print("Book Not Available")

remove_book = input("Remove Book: ")

if remove_book in books:
    books.remove(remove_book)

print("All Books:", books)

print("Total Books:", len(books))
"""

#21.
"""
list1 = [10, 20, 30]
list2 = [40, 50, 60]

merged_list = list1 + list2

print("First List:", list1)
print("Second List:", list2)
print("Merged List:", merged_list)
"""


#22.
"""
list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common Elements:", common)
"""


#23.
"""
numbers = [10, 20, 10, 30, 20, 10, 40]

frequency = {}

for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("Frequency of Elements:", frequency)
"""


#24.
"""
numbers = [10, 20, 30, 40, 50]

# Left rotation
left = numbers[1:] + numbers[:1]

# Right rotation
right = numbers[-1:] + numbers[:-1]

print("Original List:", numbers)
print("Left Rotation:", left)
print("Right Rotation:", right)
"""


#25.
"""
numbers = [10, 20, 30, 20, 10, 40, 50]

unique = []

for i in numbers:
    if i not in unique:
        unique.append(i)

print("Original List:", numbers)
print("List After Removing Duplicates:", unique)
"""


#26.
"""
marks = []

for i in range(20):
    m = int(input("Enter Student Marks: "))
    marks.append(m)

average = sum(marks) / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    else:
        below += 1

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)
"""


#27.
"""
salary = [25000, 60000, 45000, 70000, 20000]

average = sum(salary) / len(salary)

print("Highest Salary:", max(salary))
print("Lowest Salary:", min(salary))
print("Average Salary:", average)

print("Employees earning above 50000:")

for i in salary:
    if i > 50000:
        print(i)

print("Employees earning below 30000:")

for i in salary:
    if i < 30000:
        print(i)
"""


#28.
"""
scores = [120, 50, 30, 100, 75, 40, 90, 110, 60, 20]

century = 0
half_century = 0

for i in scores:
    if i >= 100:
        century += 1
    elif i >= 50:
        half_century += 1

print("Highest Score:", max(scores))
print("Lowest Score:", min(scores))
print("Total Runs:", sum(scores))
print("Average Runs:", sum(scores)/len(scores))
print("Centuries:", century)
print("Half Centuries:", half_century)
"""


#29.
"""
temperature = [30,32,35,31,29,40,38,33]

average = sum(temperature)/len(temperature)

above = []
below = []

for i in temperature:
    if i > average:
        above.append(i)
    else:
        below.append(i)

print("Hottest Day Temperature:", max(temperature))
print("Coldest Day Temperature:", min(temperature))
print("Average Temperature:", average)
print("Days Above Average:", above)
print("Days Below Average:", below)
"""


#30.
"""
patients = ["Rahul", "Amit", "Sneha"]
ages = [25, 30, 22]

# Add patient
patients.append("Rohan")
ages.append(40)

print("Patient Details:")

for i in range(len(patients)):
    print("Name:", patients[i], "Age:", ages[i])


# Search patient
name = input("Search Patient: ")

if name in patients:
    print("Patient Found")
else:
    print("Patient Not Found")


# Delete patient
remove = input("Remove Patient: ")

if remove in patients:
    index = patients.index(remove)
    patients.pop(index)
    ages.pop(index)


print("Updated Patient List:", patients)
print("Total Patients:", len(patients))
"""




