#lists
#list is an ordered and changeable collection that can store variable values in square brackets
marks = [80, 90, 75, 95]
print(marks)

#accesding list elements
marks = [80, 90, 75, 95]
print(marks[0])  # first element
print(marks[1])  # second element
print(marks[2])  # third element


#change elements in a list
marks = [80, 90, 75]

marks[1] = 95  # change second element to 95
print(marks)


#change elements in a list
marks = [80, 90, 75]

marks[2] = 78# change second element to 95
print(marks)

#add the elements in a list
marks = [80, 90, 75]
marks.append(85)  # add 85 to the end of the list
print(marks) #output: [80, 90, 75, 85]

#remove elements from a list
marks = [80,90,75]
marks.remove(90)  # remove 90 from the list
print(marks)

#insert elements in a list
numbers = [10,20,30]
numbers.insert(1, 15)  # insert 15 at index 1
print(numbers)  # output: [10, 15, 20, 

numbers = [10,20,30]
numbers.insert(2, 15)  # insert 15 at index 2
print(numbers) 

#extend a list with another list
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # output: [1, 2, 3, 4, 5, 6]


#clear a list
numbers  =[10, 20, 30]
numbers.clear()
print(numbers)  # output: []
#index of an element in a list
numbers = [10, 20, 30,40]
print(numbers.index(30))  # output: 2

numbers = [10, 20, 30,40,50,60,70,80,90]
print(numbers.index(70))  # output: 6
print
(numbers.index(90))  # output: 8

#count of an element in a list
numbers = [10, 20, 30, 20, 40, 20]
print(numbers.count(20))  # output: 3

#sort the elements in a list
numbers = [40,10, 30, 20]
numbers.sort()
print(numbers)  # output: [10, 20, 30, 40]
numbers.sort(reverse=True)
print(numbers)  # output: [40, 30, 20, 10]
#reverse method
numbers = [10,20,30,40]
numbers.reverse()
print(numbers)
#copy numbrs
a = [1,2,3]
b = a.copy()
print(b)
#start,stop,step
numbers = [10,20,30,40,50]
#slicing
print(numbers[1:4])  # output: [20, 30, 40]
print(numbers[:3])  # output: [10, 20, 30]
print(numbers[2:])
print(numbers[::-1])
#tuples in python
#tuples are ordered and unchangeable collection of elements in parentheses
student = ("pranathi",18,"python")
print(student[0])
print(student[1])
print(student[2])
#immutable nature of tuples
#tuples are immutable,meaning they cannot be changed 
numbers = (10,20,20,30,20)
print(numbers.count(20))

numbers = (10,20,30,40)
print(numbers.index(30))

numbers = (10,20,30,40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
#sets
#set is a collection of unique values that is unorderded and mutable
numbers={10,20,30,20,10}
print(numbers)
