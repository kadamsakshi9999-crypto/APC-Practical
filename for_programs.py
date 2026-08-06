#1Print natural numbers up to n
"""
n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(i)  """


#2.Print even and odd numbers up to n
"""
n = int(input("Enter n: "))

print("Even numbers:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)

print("Odd numbers:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i) """

#3.Print sum of all natural numbers up to n
"""
n = int(input("Enter n: "))

total = 0
for i in range(1, n + 1):
    total += i

print("Sum =", total)"""



#4Print sum of odd numbers up to n
"""
n = int(input("Enter n: "))

sum_odd = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum_odd += i

print("Sum of odd numbers =", sum_odd) """

#5.Print sum of even numbers up to n
"""
n = int(input("Enter n: "))

sum_even = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i

print("Sum of even numbers =", sum_even) """

#6.Print natural numbers up to n in reverse order
"""
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print(i) """


#7.Print Fibonacci series up to n terms

"""
n = int(input("Enter number of terms: "))
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c  """

#8.Check whether the entered number is prime or not
"""
n = int(input("Enter a number: "))

if n < 2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime") """

#9.Find the sum of digits of the entered number
"""
n = int(input("Enter a number: "))

total = 0
for digit in str(n):
    total += int(digit)

print("Sum of digits =", total)"""


#10.Check whether the entered number is a palindrome or not
"""
n = input("Enter a number: ")

rev = ""
for i in range(len(n) - 1, -1, -1):
    rev += n[i]

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")"""

#11.Print the multiplication table
"""
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i) """

#12.Print the largest and smallest number from n numbers
"""
n = int(input("Enter how many numbers: "))

num = int(input("Enter number 1: "))
largest = smallest = num

for i in range(2, n + 1):
    num = int(input(f"Enter number {i}: "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest =", largest)
print("Smallest =", smallest) """
