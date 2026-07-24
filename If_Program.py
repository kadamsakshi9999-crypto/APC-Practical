
#1
"""
n=int(input("Enter Number:"))
if n==0:
    print("Number is Zer0:")
else:
    print("The number is non zero:")"""


#2
"""
n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))
if n1>n2:
    print("n1 is greater")
else:
    print("n2 is graeter")"""


#3
"""
n=int(input("Enter the number:"))
if n>0:                                                                 
    print("Number is positive")
elif n<0:
    print("Number is negative:")
else:
    print("Number is Zero")"""


#4
"""
ch=input("Enter an Alphabet:")
if ch in('a','e','i','o','u','A','E','I','O','U'):
    print("Entered character is vowel")
else:
    print("Enetered character is Consonant:")"""


#5
"""
per = float(input("Enter the percentage: "))

if per >= 90:
    print("Excellent Performance")
elif per >= 80:
    print("Very Good Performance")
elif per >= 70:
    print("Good Performance")
elif per >= 60:
    print("Average Performance")
else:
    print("Poor Performance")"""


#6
"""
n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))
n3=int(input("Enter 3rd Number:"))
if n1>n2 and n1>n3:
    print("Largest number is",n1)
elif n2>n1 and n2>n3:
    print("Largest number is",n2)
else:
    print("Largest number is",n3)"""


#7
"""
n1=int(input("Enter 1st Number:"))
n2=int(input("Enter 2nd Number:"))
n3=int(input("Enter 3rd Number:"))
if n1<n2 and n1<n3:
    print("Smallest number is",n1)
elif n2>n1 and n2<n3:
    print("Smallest number is",n2)
else:
    print("Smallest number is",n3)"""

#8
"""
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")"""


#9
"""
year = int(input("Enter year: "))

if year % 4 == 0:
    print("Year is a leap year")
else:
    print("Year is not a leap year")"""


#10



marital = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if marital == "married":
    print("Driver is Insured")
elif marital == "unmarried" and gender == "male" and age > 30:
    print("Driver is Insured")
elif marital == "unmarried" and gender == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")























