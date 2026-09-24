#if condition
age=18
if age>=20:
    print("eligible")
else:
    print("not eligible")
marks =75
if marks >=40:
    print("pass")
else:
    print("fail")

marks = int(input("enter marks:"))
if marks>=90:
    print("grade A")
elif marks >=75:
    print("grade B")
elif marks >=60:
    print("grade c")
elif marks >= 40:
    print("grade D")
else:
    print("fail")
# divisible 
number = int(input("enter a number:"))
if number%5==0:
    print("divisible by 5")
# even
number = int(input("enter a number:"))
if number %4 ==0:
    print("even")
else:
    print("odd")
#odd
number = int(input("enter a number"))
if number%7==0:
    print("odd ")
else:
    print("even")
#temparature check
temperature =float(input("enter temperature"))
if temperature > 40:
    print("high temparature")
#pass and fail
marks = int(input("enter your marks"))
marks=89
if marks>=90:
    print("fail")
else:
    print("pass")
#positive and negative
number = int(input("enter a number:"))
if number >=0:
    print("positive")
else:
    print("negative")
# greater and lesser
number = int(input("enter a number:"))
if number > 100:
    print("number is greater than 100")
else:
    print("number is not greater than 100")
#largest of two numbers
a = int(input("enter first number:"))
b = int(input("enter second number:"))
if a>b:
    print("largest:",a)
elif b>a:
    print("largest:",b)
else:
    print("both are equal")
# largest of three numbers
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if a>=b and a >= c:
    print("largest:",a)
elif b>=c and b >=c:
    print("largest:",b)
else : print("largest:",c)
#days
day = int(input("enter day number:"))
if day ==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("invalid day")
#zero
number = int(input("enter a number:"))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else :
    print("zero")

a =float(input("enter first number"))
b = float(input("enter second number"))
operater = input("enter operater(+,-,*,/):")

if operater =="+":
    print("result:",a+b)
elif operater =="-":
    print("result:",a-b)
elif operater =="*":
    print("result:",a*b)
elif operater =="/":
    if b !=0:
      print("result:",a/b)
    else:
      print("cannot divide by zero")
else:
     print("invalid operater")

username = input("enter username:")
password = input("enter password:")

if username == "admin":
   if password =="1234":
       print("login successful")
   else:
       print("wrong password")   
else:
    print("wrong username")   

balance = float(input("enter balance:")) 
amount = float(input("enter withdrawl amount:"))

if amount > 0:
    if amount <= balance:
        balance = balance - amount
        print("withdrawl successful")
        print("remaining balance:",balance)
    else:
        print("insufficient balance")
else:
    print("invalid amount")       


age = int(input("enter age"))
test = input("did you pass the driving test?(yes/no):")

if age >=18:
    if test =="yes":
        print("license can be issued")
    else:
        print("pass the driving test first")
else:
    print("not eligible due to age")
