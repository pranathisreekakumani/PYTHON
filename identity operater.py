a = 5 #bitwise operator
b = 3
print(a & b)#and operater
print(a | b)#or operater
print(a ^ b)#xor operater
print(a<<b)#left shift
print(a>>b)#right shift

#electric bill calculator
units = float(input("enter number of units consumed:"))
rate = 6
bill = units * rate
print("total bill amount:", bill)

#travel expense calculator
travel = float(input("enter travel expense: "))
food = float(input("enter food expense: "))
hotel = float(input("enter hotel expense: "))

total = travel + food + hotel

print("total expense:", total)

#lists
#list is an ordered and changeable collection that can store variable values in square brackets
marks = [80, 90, 75, 95]
print(marks)

#accescsing list elements
marks = [80, 90, 75, 95]
print(marks[0])  # first element
print(marks[1])  # second element
print(marks[2])  # third element
