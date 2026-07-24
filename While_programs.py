#1
"""
n = int(input("Enter n: "))
i = 1

while i <= n:
    print(i)
    i += 1"""

#2
"""
n = int(input("Enter n: "))
i = 1

print("Even numbers:")
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

i = 1
print("Odd numbers:")
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1 """


#3
"""
n = int(input("Enter n: "))
i = 1
sum = 0

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)"""


#4
"""
n = int(input("Enter n: "))
i = 1
sum = 0

while i <= n:
    if i % 2 != 0:
        sum += i
    i += 1

print("Sum of odd numbers =", sum)"""

#5
"""
n = int(input("Enter n: "))
i = 1
sum = 0

while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1"""


#6
"""
n = int(input("Enter n: "))

while n >= 1:
    print(n)
    n -= 1

print("Sum of even numbers =", sum)"""

#7
"""
n = int(input("Enter number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c   """

#8
"""
n = int(input("Enter a number: "))
i = 2
count = 0

while i < n:
    if n % i == 0:
        count += 1
    i += 1

if n > 1 and count == 0:
    print("Prime Number")
else:
    print("Not a Prime Number")
    i += 1  """

#9
'''
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10  '''

#10
"""
n = int(input("Enter a number: "))
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

print("Sum of digits =", sum)  """

#11
"""
n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1  """

#12
"""
n = int(input("Enter how many numbers: "))

i = 1
num = int(input("Enter number: "))
largest = num
smallest = num

while i < n:
    num = int(input("Enter number: "))
    
    if num > largest:
        largest = num
    
    if num < smallest:
        smallest = num

    i += 1

print("Largest =", largest)
print("Smallest =", smallest)   """
