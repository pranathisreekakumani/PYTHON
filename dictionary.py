# dictionary is a key value pair and it is unord"ered and mutable 
student = {"Name" : "pranathi", "marks" : "98" , "subject" : "python"}
print(student)
print(student. keys())
print(student.values())
print(student.items())
#access the elements in the dictionary
student = {"name":"pranathi","age":"18","subject":"python"}
print(student["name"])
print(student["age"])
print(student["subject"])
#change values in a dictionary
student["age"] = 11
print(student["age"])
#add new data to the dictionary
student["city"] = "kandukur"
print(student)
#remove data
student.pop("city")
print(student)
student ={"name":"pranathi","marks":"98","course":"python"}
print(student.get('name'))
print(student.get('marks'))
print(student.get('course'))
#update the values of specified key
student.update({"marks":18})
print(student)
#pop removes the specified key and its value
student.pop("marks")
print(student)

#popitem()
student={"name":"pranathi","marks":"98","subject":"python"}
student.popitem()
print(student)

#set defualt
student = {"name":"pranathi"}
student.setdefault("age",18)
print(student)

#clear method
student.clear()
print(student)
student = {"name":"pranathi","age":18}
new_student = student.copy()
print(new_student)
#order of evaluation(bodmas)
result = 2+13*2
print(result)