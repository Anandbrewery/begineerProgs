#Hash maps or associate arrays or key:value
student={'name':'John', 'age':25, 'courses':['Math', 'Compsci']}
students={100:'John', 'age':25, 'courses':['Math', 'Compsci']}
print(student)
print(student['courses'])
print(students[100])
print(student['phone']) # will give u key error
print(student.get('phone')) # None
print(student.get('phone','Not_Found')) # assigning the unknown keys with Not_Found
student['phone']= '555-5555' # Adding the new key value
print(student)
student['name']= 'Jane' # Update the existing key
print(student)
student.update({'name': 'Green', 'age':26 , 'phone': '555=5555'})#multiple updates
print(student)
del student['age']
print(student)
student['age']=25
age=student.pop('age')#pop will return value of the key and del the key:value pair
print(student)
print(age)
print(len(student))# length of dict
print(student.keys())
print(student.values())
print(student.items())







