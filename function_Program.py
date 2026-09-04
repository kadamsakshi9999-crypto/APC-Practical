
# 1. Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter Number: "))
print("Factorial is", factorial(n))


# 2. Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter Number: "))
print("Number is", check_even_odd(n))


# 3. Greater of Two Numbers
def greater(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))
print("Greater number is", greater(n1, n2))


# 4. Simple Interest
def simple_interest(p, r, t):
    si = (p * r * t) / 100
    return si

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
print("Simple Interest is", simple_interest(p, r, t))


# 5. Prime Number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter Number: "))

if is_prime(n):
    print("Number is Prime")
else:
    print("Number is Not Prime")


# 6. Area of Circle
def area_circle(r):
    area = 3.14 * r * r
    return area

r = float(input("Enter Radius: "))
print("Area of Circle is", area_circle(r))


# 7. Sum of First n Natural Numbers
def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter Number: "))
print("Sum is", sum_n(n))


# 8. Power
def power(base, exponent):
    return base ** exponent

base = int(input("Enter Base: "))
exponent = int(input("Enter Exponent: "))
print("Answer is", power(base, exponent))


# 9. Largest Element without max()
def largest(numbers):
    large = numbers[0]

    for n in numbers:
        if n > large:
            large = n

    return large

numbers = list(map(int, input("Enter Numbers: ").split()))
print("Largest number is", largest(numbers))


# 10. Count Vowels
def count_vowels(s):
    count = 0

    for ch in s:
        if ch in "aeiouAEIOU":
            count = count + 1

    return count

s = input("Enter String: ")
print("Number of vowels is", count_vowels(s))


# 11. Reverse String
def reverse_string(s):
    return s[::-1]

s = input("Enter String: ")
print("Reverse is", reverse_string(s))


# 12. Palindrome
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

s = input("Enter String or Number: ")

if palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")


# 13. Average of List
def average(numbers):
    total = 0

    for n in numbers:
        total = total + n

    return total / len(numbers)

numbers = list(map(int, input("Enter Numbers: ").split()))
print("Average is", average(numbers))


# 14. Count Occurrence
def count_element(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count = count + 1

    return count

numbers = list(map(int, input("Enter Numbers: ").split()))
element = int(input("Enter Element: "))

print("Occurrence is", count_element(numbers, element))


# 15. Unique Elements
def unique(numbers):
    new_list = []

    for n in numbers:
        if n not in new_list:
            new_list.append(n)

    return new_list

numbers = list(map(int, input("Enter Numbers: ").split()))
print("Unique elements are", unique(numbers))


# 16. Second Largest
def second_largest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

numbers = list(map(int, input("Enter Numbers: ").split()))
print("Second Largest is", second_largest(numbers))


# 17. First n Fibonacci Numbers
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter Number: "))
fibonacci(n)
print()


# 18. Percentage and Grade
def percentage_grade(marks):
    total = sum(marks)
    per = total / 5

    if per >= 90:
        grade = "A"
    elif per >= 80:
        grade = "B"
    elif per >= 70:
        grade = "C"
    elif per >= 60:
        grade = "D"
    else:
        grade = "F"

    return per, grade

marks = []

for i in range(5):
    marks.append(float(input("Enter Marks: ")))

per, grade = percentage_grade(marks)

print("Percentage is", per)
print("Grade is", grade)


# 19. Electricity Bill
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    return bill

units = int(input("Enter Units: "))
print("Electricity Bill is", electricity_bill(units))


# 20. Gross Salary
def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    gross = basic + hra + da

    return gross

basic = float(input("Enter Basic Salary: "))
print("Gross Salary is", gross_salary(basic))


# 21. Total Bill after Discount
def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    discount = total * 0.10
    final_bill = total - discount

    return final_bill

prices = list(map(float, input("Enter Prices: ").split()))
quantities = list(map(int, input("Enter Quantities: ").split()))

print("Final Bill is", total_bill(prices, quantities))


# 22. Minimum, Maximum, Sum and Average
def calculate(numbers):
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average

numbers = list(map(int, input("Enter Numbers: ").split()))

minimum, maximum, total, average = calculate(numbers)

print("Minimum is", minimum)
print("Maximum is", maximum)
print("Sum is", total)
print("Average is", average)


# 23. Student Records
def student_result(marks):
    total = sum(marks)
    percentage = total / 5

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    return total, percentage, grade


students = []

n = int(input("Enter Number of Students: "))

for i in range(n):
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")

    marks = []

    for j in range(5):
        marks.append(float(input("Enter Marks: ")))

    total, percentage, grade = student_result(marks)

    students.append((name, roll, total, percentage, grade))

for s in students:
    print(s)

percentages = [s[3] for s in students]

print("Class Average:", sum(percentages) / len(percentages))
print("Highest Scorer:", max(students, key=lambda x: x[3]))
print("Lowest Scorer:", min(students, key=lambda x: x[3]))


# 24. Banking Functions
balance = 0
history = []

def deposit(amount):
    global balance
    balance = balance + amount
    history.append("Deposited " + str(amount))

def withdrawal(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        history.append("Withdrawn " + str(amount))
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")

def balance_enquiry():
    print("Balance is", balance)

def transaction_history():
    for h in history:
        print(h)

deposit(5000)
withdrawal(1000)
balance_enquiry()
transaction_history()


# 25. Library Management
books = {
    "Python": True,
    "Java": True,
    "C++": True
}

def add_book(name):
    books[name] = True

def issue_book(name):
    if name in books and books[name]:
        books[name] = False
        print("Book Issued")
    else:
        print("Book Not Available")

def return_book(name):
    books[name] = True
    print("Book Returned")

def search_book(name):
    if name in books:
        print("Book Found")
    else:
        print("Book Not Found")

def display_books():
    for name in books:
        if books[name]:
            print(name)

add_book("Python")
issue_book("Python")
search_book("Java")
display_books()


# 26. Electricity Bill with Fixed Charges, Tax and Discount
def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10

    fixed = 50
    bill = bill + fixed

    tax = bill * 0.05
    bill = bill + tax

    discount = 0

    if units < 100:
        discount = bill * 0.05

    bill = bill - discount

    return bill

units = int(input("Enter Units: "))
print("Final Electricity Bill is", calculate_bill(units))


# 27. Hospital Bill
def consultation(charge):
    return charge

def laboratory(charge):
    return charge

def medicine(charge):
    return charge

def room(charge):
    return charge

def final_bill(category, c, l, m, r):
    total = consultation(c) + laboratory(l) + medicine(m) + room(r)

    if category == "senior":
        total = total * 0.90

    return total

category = input("Enter Category: ")

c = float(input("Consultation Charges: "))
l = float(input("Laboratory Charges: "))
m = float(input("Medicine Charges: "))
r = float(input("Room Charges: "))

print("Final Bill is", final_bill(category, c, l, m, r))


# 28. Shopping Invoice
def subtotal(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total = total + prices[i] * quantities[i]

    return total

def final_invoice(prices, quantities):
    total = subtotal(prices, quantities)

    discount = total * 0.10
    total = total - discount

    gst = total * 0.18
    total = total + gst

    return total

prices = list(map(float, input("Enter Prices: ").split()))
quantities = list(map(int, input("Enter Quantities: ").split()))

print("Final Invoice is", final_invoice(prices, quantities))


# 29. Recursive Binary Search
def binary_search(numbers, low, high, key):
    if low > high:
        return False

    mid = (low + high) // 2

    if numbers[mid] == key:
        return True
    elif key < numbers[mid]:
        return binary_search(numbers, low, mid - 1, key)
    else:
        return binary_search(numbers, mid + 1, high, key)

numbers = list(map(int, input("Enter Sorted Numbers: ").split()))
key = int(input("Enter Element: "))

if binary_search(numbers, 0, len(numbers) - 1, key):
    print("Element Found")
else:
    print("Element Not Found")


# 30. Decimal to Binary using Recursion
def decimal_binary(n):
    if n == 0:
        return ""

    return decimal_binary(n // 2) + str(n % 2)

n = int(input("Enter Decimal Number: "))

if n == 0:
    print("Binary is 0")
else:
    print("Binary is", decimal_binary(n))


# 31. Palindrome using Recursion
def palindrome_recursive(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrome_recursive(s[1:-1])

s = input("Enter String: ")

if palindrome_recursive(s):
    print("Palindrome")
else:
    print("Not Palindrome")


# 32. Functions as Arguments
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def calculate_operation(operation, a, b):
    return operation(a, b)

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("Addition:", calculate_operation(addition, a, b))
print("Subtraction:", calculate_operation(subtraction, a, b))
print("Multiplication:", calculate_operation(multiplication, a, b))
print("Division:", calculate_operation(division, a, b))



# 33. Square using Lambda
square = lambda n: n * n

n = int(input("Enter Number: "))
print("Square is", square(n))


# 34. Cube using Lambda
cube = lambda n: n * n * n

n = int(input("Enter Number: "))
print("Cube is", cube(n))


# 35. Even using Lambda
even = lambda n: n % 2 == 0

n = int(input("Enter Number: "))
print(even(n))


# 36. Maximum of Two Numbers using Lambda
maximum = lambda a, b: a if a > b else b

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))

print("Maximum is", maximum(a, b))


# 37. Simple Interest using Lambda
simple_interest = lambda p, r, t: (p * r * t) / 100

p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))

print("Simple Interest is", simple_interest(p, r, t))


# 38. Squares using map() and Lambda
numbers = list(map(int, input("Enter Numbers: ").split()))

squares = list(map(lambda n: n * n, numbers))

print("Squares are", squares)


# 39. Cubes using map() and Lambda
numbers = list(map(int, input("Enter Numbers: ").split()))

cubes = list(map(lambda n: n * n * n, numbers))

print("Cubes are", cubes)


# 40. Sum of Corresponding Elements of Two Lists
list1 = list(map(int, input("Enter 1st List: ").split()))
list2 = list(map(int, input("Enter 2nd List: ").split()))

result = list(map(lambda a, b: a + b, list1, list2))

print("Sum List is", result)


# 41. Even Numbers using filter() and Lambda
numbers = list(map(int, input("Enter Numbers: ").split()))

even = list(filter(lambda n: n % 2 == 0, numbers))

print("Even Numbers are", even)


# 42. Prime Numbers using filter() and Lambda
def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

numbers = list(map(int, input("Enter Numbers: ").split()))

result = list(filter(lambda n: prime(n), numbers))

print("Prime Numbers are", result)


# 43. Positive Numbers using filter()
numbers = list(map(int, input("Enter Numbers: ").split()))

positive = list(filter(lambda n: n > 0, numbers))

print("Positive Numbers are", positive)


# 44. Numbers Greater Than 50
numbers = list(map(int, input("Enter Numbers: ").split()))

result = list(filter(lambda n: n > 50, numbers))

print("Numbers greater than 50 are", result)


# 45. Words Having More Than 5 Characters
words = input("Enter Words: ").split()

result = list(filter(lambda word: len(word) > 5, words))

print("Words are", result)


# 46. Sort Words According to Length
words = input("Enter Words: ").split()

words.sort(key=lambda word: len(word))

print("Sorted Words are", words)


# 47. Sort Students According to Marks
students = [
    ("Amit", 80),
    ("Rahul", 60),
    ("Sneha", 90)
]

students.sort(key=lambda x: x[1])

print("Students sorted by marks:")
print(students)


# 48. Sort Employees According to Salary
employees = [
    ("Amit", 30000),
    ("Rahul", 50000),
    ("Sneha", 40000)
]

employees.sort(key=lambda x: x[1])

print("Employees sorted by salary:")
print(employees)


# 49. Student Names and Marks
students = [
    ("Amit", 80),
    ("Rahul", 60),
    ("Sneha", 90),
    ("Priya", 70)
]

average = sum(map(lambda x: x[1], students)) / len(students)

above_75 = list(filter(lambda x: x[1] > 75, students))

students.sort(key=lambda x: x[1])

print("Average Marks:", average)
print("Students above 75:", above_75)
print("Sorted Students:", students)


# 50. Employee Records
employees = [
    ("Amit", "IT", 60000),
    ("Rahul", "HR", 40000),
    ("Sneha", "IT", 70000)
]

above_50000 = list(filter(lambda x: x[2] > 50000, employees))

employees = list(
    map(lambda x: (x[0], x[1], x[2] * 1.10), employees)
)

employees.sort(key=lambda x: x[2])

print("Employees earning above 50000:", above_50000)
print("Salary increased by 10%:", employees)
print("Sorted Employees:", employees)


# 51. Product Records
products = [
    ("Pen", 20, 10),
    ("Bag", 1200, 2),
    ("Book", 500, 3)
]

products = list(
    map(lambda x: (x[0], x[1], x[2], x[1] * x[2]), products)
)

above_1000 = list(filter(lambda x: x[3] > 1000, products))

products.sort(key=lambda x: x[3])

print("Total Value:", products)
print("Products above 1000:", above_1000)
print("Sorted Products:", products)


# 52. Words using map(), filter() and sorted()
words = input("Enter Words: ").split()

lengths = list(map(lambda word: len(word), words))

long_words = list(
    filter(lambda word: len(word) > 5, words)
)

sorted_words = sorted(words, key=lambda word: len(word))

print("Length of Words:", lengths)
print("Words having more than 5 characters:", long_words)
print("Sorted Words:", sorted_words)
