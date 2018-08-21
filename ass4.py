#Que1-->Take an input year from user and decide whether it is leap year or not.
"""A year which occurs once every four years and
has 366 days is known as Leap Year"""
yr=int(input("enter a year"))
if yr % 4 == 0:
    print("Yes it is a leap year")
else:
    print("No,it is not a leap year")
print()

#Que2-->Take length and breadth input from user and check whether the dimensions are of square or rectangle
l=int(input("enter the length"))
b=int(input("enter the breadth"))
if l == b:
    print("it is a square");
else:
    print("it is a rectangle");
print()

#Que3-->Take the input age of 3 people and determine oldest and youngest among them.
a=int(input("enter age of first prsn"))
b=int(input("enter age of second prsn"))
c=int(input("enter age of third prsn"))
if a>b and a>c:
    print("a is oldest")
elif b>a and b>c:
    print("b is oldest")
else:
    print("c is oldest")

if a<b and a<c:
    print("a is youngest")
elif b<a and b<c:
    print("b is youngest")
else:
    print("c is youngest")
print()

#Que4--> Ask user to enter age,sex,marital status and then print their place of service.
age=int(input("enter your age"))
sex=input("enter your sex as 'M' or 'F'")
mrt=input("enter your marital status as 'Y' or 'N'")
if age<20 or age>60:
    print("error")
else:
    if sex == 'F' or sex == 'f':
        print("Works in urban areas")
    elif (sex == 'M' or sex == 'm') and (age>=20 and age<=40):
        print("Works anywhere")
    elif (sex == 'M' or sex == 'm') and (age>=40 and age<=60):
        print("Works in urban areas")
print()

#Que5-->A shop will give discount of 10% if the cost of purchased quantity is more than 1000,Ask user for quantity suppose,one unit wil cost 100.Judge and print total cost for user.
quant=int(input("enter quantity"))
cost=quant*100;
if cost>1000:
    total_cost=cost-(0.1*cost)
    print(total_cost)
else:
    print(cost)
print()

#Que6-->Take 10 integers from user and print it on screen.
print("enter 10 integers")
for i in range(10):
    a=int(input())
    print(a)
print()

#Que7-->Write an infinite loop.
while True:
    print("hyy")
print()

#Que8-->Make a list which will store square of elements of other list
l1=[]
l2=[]
n=int(input("enter number of elements"))
print("enter the elements:")
for i in range(n):
    a=int(input())
    l1.append(a)
print("first list is:" , end=' ')
print(l1)

for i in range(n):
    b=l1[i]*l1[i]
    l2.append(b)
print("list after finding squares is:",end=' ')
print(l2)
print()

#Que9-->From a list containing ints,strings and floats,make three lists to store them separately
lst=[1,2,'hyy',3,3.0,'gud']
print(lst)
l1=[]
l2=[]
l3=[]
for i in lst:
    if isinstance(i,int):
        l1.append(i)
    elif isinstance(i,str):
        l2.append(i)
    elif isinstance(i,float):
        l3.append(i)
print("integer list:",l1)
print("string list:",l2)
print("float list:",l3)
print()

#Que10-->Make a list containing prime numbers.
print("prime numbers are:")
for num in range(1,101):
    if num>1:
        isDivisible = False
        for index in range(2,num):
            if num % index == 0:
                isDivisible = True
        if not isDivisible:
            print(num)
print()

#Que11-->Print the pattern
for i in range(4):
    for j in range(i+1):
        print('*',end=' ')
    print('\n')
print()

#Que12-->Search and Delete an Element froma User defined list
n=int(input("enter number of elements"))
l1=[]
for i in range(n):
    a=int(input())
    l1.append(a)
print(l1)
b=int(input("enter element you want to delete:"))
if b in l1:
    l1.remove(b)
else:
    print("this element you entered does not exist in list")
print(l1)
