# 1 display personal details using variables
name = input()
age = int(input())
height = float(input())
print(name)
print(age)
print(height)
# 2 personalised greeting
name = input()
print(F"Hello,{name}!")
# 3 add two numbers read as strings
a = input()
b = input()
#converting the string into integer
a = int(a)
b = int(b)
#find the sum
total = a+b
#print the result
print(total)
#4 float to integer conversion
# float:numbers with decimal value
#int:whole numbers without any decimal or fractional value
#reading a float value from the user
n = float(input())
#print the float value
print(n)
#convert the float into integer:decimal point values will be removed
new = int(n)
#print the result
print(new)
#5 sum using arithmetic operator
#reading 2 integers from the user
a = int(input())
b = int(input())
#finding the sum and printing the result
print(a+b)
# 6 area of a rectangle
#reading input from the user
length = float(input())
breadth = float(input())
#calculating the area of a rectangle
area = length*breadth
#print the result
print(area)
#7 quotient and remainder
#user inputs
a = int(input())
b = int(input())
#find the quotient
q = a/b
#find the remainder
r = a%b
#print the result
print(q)
print(r)
#8 wer calculation
#reading user input
base = int(input())
exponent = int(input())
#calculate thr power of and print the result
print(base**exponent)
#9 average of three numbers
# taking 3 integer numbers from the user
n1 = int(input())
n2 = int(input())
n3 = int(input())
#find the total
total = n1+n2+n3
#find the average
avg = total/3#division operator/-->always gives the result as a float
#print the average
print(avg)
#10 greater than comparision
#read 2 integer numbers from user
a = int(input())
b = int(input())
#check wether the 1st number is greater than the 2nd number
print(a>b)
#11 equality check
#check whether both the numbers are same or not
#if the numbers are same-true
#If the numbers are different-false
#reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1==n2)
#12 both numbers positive check
#If the numbers is greater than 0
#Logical and-->If all the combining conditions are true,result is true
#Reading the input from the user
n1 = int(input())
n2 = int(input())
print(n1>0 and n2>0)
# 13 logical NOT on a condition
#logical not-->reverse the result
#true-->false
#false-->true
#reading the input from the user
num = int(input())
print(not(num>0))
#14 Augmented assignment operations
#read a number from the user
a = int(input())#20
a = a+5#a=20+5 -->25
a = a*2#a=25*2 -->50
a = a-3#a=50-3 -->47
print(a)
#15 exchange values of two variables
#reading the input from the user
a = int(input())
b = int(input())

#Logic1 -using temp variable
temp = a 
a = b
b = temp
print(a)
print(b)

#Logic 2: without using temp(3rd variable)
a = a+b
b = a-b
a = a-b
print(a)
print(b)
#logic 3:without using temp(3rd variable)
a = a^b
b = a^b
a = a^b
print(a)
print(b)
#Logic4:without using temp(3rd variable)
#problem:It cannot handle 0
a = a*b
b = a/b
a = a/b
print(a)
print(b)
#logic5:using python's special
#simplest way
a,b = b,a
print(a)
print(b)
#17 calculate simple intrest
#Formula:F = (principle*rate*time)/100
#User Inputs
principle = float(input())#loan amount
rate = float(input())#rate of intrest
time = float(input())#repayment time
#calculate intrest
si = (principle*rate*time)/100
#print the result
print(si)
#18 temperature conversion (celsius tofahrenheit)
#Formula :F = (c*9/5)+32
#Read the temperature in celsius
c = float(input())
#convert the celsius to fahrenheit
f = (c*9/5)+32
print(f)
#19 check divisibility by 3 and 5
n = int(input())
print(n%3==0 and 5==0)
#20 sum of digits of a two digit number
num = int(input()) #num = 48
tens = num//10 #tens = 48//10 =4
units = num%10 #units =48%10 =8
total = tens+units #total = 4+8 = 12
print(total)
#21 At Least one even number
#Even Number:If the number is divisible by 2 (without any reminder)
#Logical or -->If any one of the combining condition is true,then the result is true
#Arithmetic operators
#/-->Division-result is in form of decimal value
example:13/2=6.5
#/-->Floor Division-result in the form of integer
Example:13/2=6
#%-->Modulo-result is the remainder of the division 
Example:13/2=1

#reading the input from the user
n1 = int(input())
n2 = int(input())

print(n1%2==0 or n2%2==0)




