#1
"""
tuple=(10,20,30,40,50)
print(tuple)
"""


#2
"""
cities=("Mumbai","Pune","Kolhapur","Delhi","Nashik")

print("First city:",cities[0])
print("Last city:",cities[-1])
print("Third city:",cities[2])
"""


#3
"""
student=("Sakshi","Samiksha","Anisha","Kajol","Gullu")

print("Students name:",student)
print("Total students:",len(student))
"""


#4
"""
colors=("Red","Blue","Green","Yellow","Black")

color=input("Enter a color:")

if color in colors:
    print("Color exists in the tuple")
else:
    print("Color does not exist in the tuple")
"""


#5
"""
fruits=("Mango","Orange","Cherry","Banana","Apple")

for fruit in fruits:
    print(fruit)
"""


#6
"""
numbers=(10,20,10,30,10,40,10)

n=int(input("Enter number:"))

print("Number appears",numbers.count(n),"times")
"""


#7
"""
employee=(101,102,103,104,105)

id=int(input("Enter Employee ID:"))

if id in employee:
    print("Index:",employee.index(id))
else:
    print("Employee ID not found")
"""


#8
"""
tuple1=(10,20,30)
tuple2=(40,50,60)

tuple3=tuple1+tuple2

print("First tuple:",tuple1)
print("Second tuple:",tuple2)
print("Combined tuple:",tuple3)
"""


#9
"""
numbers=(1,2,3)

result=numbers*4

print("Repeated tuple:",result)
"""


#10
"""
numbers=(1,2,3,4,5,6,7,8,9,10)

print("First five elements:",numbers[:5])
print("Last five elements:",numbers[5:])
print("Middle four elements:",numbers[3:7])
print("Alternate elements:",numbers[::2])
print("Reverse tuple:",numbers[::-1])
"""


#11
"""
numbers=(10,20,30)

numbers=list(numbers)
numbers.append(40)
numbers=tuple(numbers)

print("New tuple:",numbers)
"""


#12
"""
numbers=[]

for i in range(5):
    n=int(input("Enter number:"))
    numbers.append(n)

numbers=tuple(numbers)

print("Tuple:",numbers)
"""


#13
"""
numbers=(10,20,30)

numbers=list(numbers)

numbers[1]=50

numbers=tuple(numbers)

print("Modified tuple:",numbers)
"""


#14
"""
numbers=(10,20,30,40)

print("Tuple:",numbers)

del numbers

print("Tuple deleted successfully")
"""


#15
"""
students=(
    (1,"Sakshi",85),
    (2,"Samiksha",90),
    (3,"Anisha",88)
)

for student in students:
    print("Roll Number:",student[0])
    print("Name:",student[1])
    print("Marks:",student[2])
    print()
"""


#16
"""
numbers=(10,20,30,40,50,60,70,80,90,100)

total=sum(numbers)

print("Sum:",total)
"""


#17
"""
numbers=(25,10,45,5,30)

largest=numbers[0]
smallest=numbers[0]

for n in numbers:
    if n>largest:
        largest=n

    if n<smallest:
        smallest=n

print("Largest number:",largest)
print("Smallest number:",smallest)
"""


#18
"""
numbers=(10,20,30,40,50)

total=sum(numbers)
average=total/len(numbers)

print("Average:",average)
"""


#19
"""
numbers=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

even=0
odd=0

for n in numbers:
    if n%2==0:
        even=even+1
    else:
        odd=odd+1

print("Even numbers:",even)
print("Odd numbers:",odd)
"""


#20
"""
numbers=(10,20,30,40,50)

n=int(input("Enter number:"))

if n in numbers:
    print("Number exists in the tuple")
else:
    print("Number does not exist in the tuple")
"""


#21
"""
student=(101,"Sakshi","Computer",85)

print("Roll Number:",student[0])
print("Name:",student[1])
print("Department:",student[2])
print("Marks:",student[3])
"""


#22
"""
employees=(
    (101,"Amit",30000),
    (102,"Rahul",35000),
    (103,"Priya",40000)
)

for employee in employees:
    print("Employee ID:",employee[0])
    print("Name:",employee[1])
    print("Salary:",employee[2])
    print()
"""


#23
"""
prices=(100,250,150,500,300)

total=sum(prices)
average=total/len(prices)

highest=prices[0]
lowest=prices[0]

for price in prices:
    if price>highest:
        highest=price

    if price<lowest:
        lowest=price

print("Total bill:",total)
print("Average price:",average)
print("Highest price:",highest)
print("Lowest price:",lowest)
"""


#24
"""
temperature=(30,32,29,35,31,33,28)

highest=temperature[0]
lowest=temperature[0]

for temp in temperature:
    if temp>highest:
        highest=temp

    if temp<lowest:
        lowest=temp

average=sum(temperature)/len(temperature)

print("Maximum temperature:",highest)
print("Minimum temperature:",lowest)
print("Average temperature:",average)
"""


#25
"""
runs=(45,60,30,75,90,55,40,80,65,50)

total=sum(runs)
highest=runs[0]
lowest=runs[0]

for run in runs:
    if run>highest:
        highest=run

    if run<lowest:
        lowest=run

average=total/len(runs)

print("Total runs:",total)
print("Highest score:",highest)
print("Lowest score:",lowest)
print("Average score:",average)
"""


#26
"""
tuple1=(10,20,30,40)
tuple2=(30,40,50,60)

common=()

for n in tuple1:
    if n in tuple2:
        common=common+(n,)

print("Common elements:",common)
"""


#27
"""
tuple1=(10,20,30,40)
tuple2=(30,40,50,60)

merged=tuple1+tuple2
result=()

for n in merged:
    if n not in result:
        result=result+(n,)

print("Merged tuple:",result)
"""


#28
"""
numbers=(10,20,10,30,20,10,40)

checked=()

for n in numbers:
    if n not in checked:
        print(n,"appears",numbers.count(n),"times")
        checked=checked+(n,)
"""


#29
"""
numbers=(50,20,40,10,30)

ascending=tuple(sorted(numbers))
descending=tuple(sorted(numbers,reverse=True))

print("Ascending order:",ascending)
print("Descending order:",descending)
"""


#30
"""
patients=(
    (101,"Amit",25,"A+"),
    (102,"Priya",30,"B+"),
    (103,"Rahul",28,"A+"),
    (104,"Neha",35,"O+")
)

print("All Patient Records:")

for patient in patients:
    print(patient)

id=int(input("Enter Patient ID:"))

found=False

for patient in patients:
    if patient[0]==id:
        print("Patient found:",patient)
        found=True

if found==False:
    print("Patient not found")

print("Total number of patients:",len(patients))

blood=input("Enter Blood Group:")

print("Patients with",blood,"blood group:")

for patient in patients:
    if patient[3]==blood:
        print(patient)
"""
