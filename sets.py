#set is a collection of unique values that is unorderded and mutable
numbers={10,20,30,20,10}
print(numbers)
#why use sets
#suppose students have selected subjects
subjects = {"python","java","python","SQL","java"}
print(subjects)
#add values from a set
subjects = {"python","java"}
subjects.add("SQL")
print(subjects)
#remove values to a set
subjects = {"python","java","SQL"}
subjects.remove("java")
print(subjects)
#sets do not allow duplicate values
numbers = {1,2,3,4,3,2}
print(numbers)
#display personal details using variables
#getting the input from user
name = input("enter your name")
age = int(input("enter your age"))
height = float(input("enter your height"))
print(name)
print(age)
print(height)
#personalised greeting
name = input("enter your name")
print(F"Hello,{name}!")
#add two numbers read as strings
#taken the input as a string
a = input ("enter a : 10 ")
b = input (" enter b : 20 ")
#converting the string into integer
#find the sum
total = a+b
#print the result
print(total)
#float to integer conversation
#float:numbers with decimal values
#reading a float value from the user
n = float(input("enter a number:5"))
print(n)
#convert the float into integer :decimal point will be removed
new = int(n)
print (new)
#sum using arthematic opereter
a = int(input(19))
b = int(input(29))
print(a+b)
#area of rectangle
length = float(input())
breadth = float(input())
area = length*breadth
print(area)
#quotient and remainder
a = int(input())
b = int(input())
q = a/b
r = a%b
print(q)
print(r)
# power calculation
base = int(input())
exponent = int(input())
print(base**exponent)
#average of three numbers
n1 = int(input())
n2 = int(input())
n3 = int(input())
total = n1+n2+n3
Average = total/3
print(average)
#Greater than comparison
a = int(input(9))
b = int(input(5))
print(a>b)
#equality check
#check whether both the numbers are same or not
#If the numbers are same - true
#If the numbers are different - false
n1 = int(input())
n2 = int(input())
print(n1==n2)
#Both numbers positive check
#If thr number is greater than 0
#logical and-->if all the combining conditions is true ,result is true
n1 = int(input())
n2 = int(input())
print(n1>0 and n2>0)
# At least one Even number
#Even number :If any one of the combining condition is true,then the result is true.
arthmetic operators
/-->Divison - result is in form of decimal Value
example :13/2 = 6.5
// --> floor division - result is in form of integer
example :13/2 = 6
%-->modulo - result is the reminder of the division operation
example :13/2 = 1
n1 = int(input())
n2 = int(input())
print(n1%2==0 or n2%2==0)
#logical NOT on a condition
#logical not -->reverse the result
true -->False
false -->True
reading the input from the User
num = int(input())
print(not(num>0))
#Augmented assignment operations
#Read a number from the user
a = int(input())
b = int(input())
#logic 1 - using temp variable
temp = a
a = b
b = temp
print(a)
print(b)
#logic 2:without using temp (3rd variable)
a = a+b
b = a-b
print(a)
print(b)
#logic 3:without using temp (3rd variable)
a = a^b
b = a^b
a = a^b
print(a)
print(b)
#logic 4:without using temp(3rd variable)
#problem: It cannot handle 0
a = a*b
b = a/b
a = a/b
print(a)
print(b)
#logic 5:using pythons special
#simplest way
a,b = b,a
print(a)
# calculate simple interest
#formula :(principle*rate*time)/100
#user inputs
principle = float(input()) #loan amount
rate = float(input())# rate of intrest


