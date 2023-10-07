# Tuples sequential data type
# Sets unordered collection of data without duplicates
courses=['History' , 'Math' , 'Physics' , 'CompSci']
print(courses)
print(len(courses))
print(courses[0]) # 1st element
print(courses[-1]) # last element
print(courses[0:2]) # all the values between 0 and 2 2 not inclusive
print(courses[:2]) # similar as above
print(courses[2:]) # all the values from 2 till end 
courses.append('Art') # inserts at the end
courses.insert(0,'Art') # inserts at the 0th index
courses_2=['Art','Education']
#courses.insert(0,courses_2) # inserts courses_2 at  the 0th index
#courses.extend(courses_2) # extends courses by adding courses_2 at  the end
courses.remove('Math')# removes Math from course
courses.pop()# pop the last index as it is considered top
courses.reverse #reverse the list
#courses.sort() #ascending order
courses.sort(reverse=True) #descending order
sortlist=sorted(courses)# not an method it is an built-in function
nums=[1,3,2]
print(min(nums))
print(max(nums))
print(sum(nums))
print(courses.index('CompSci'))
print('Math' in courses)
for index,course in enumerate(courses):
	print(index,course)
for index,course in enumerate(courses, start=1):
	print(index,course)
course_str=', '.join(courses)
print(course_str) # History, Math, Physics, CompSci
newlist=course_str.split(', ') #['History' , 'Math' , 'Physics' , 'CompSci']
#Tuple are immutable type
list_1=['History' , 'Math' , 'Physics' , 'CompSci'] 
list_2=['History' , 'Math' , 'Physics' , 'CompSci'] 
print(list_1)
print(list_2)
list_1[0]='Art'
print(list_1)
print(list_2)

tuple_1=('History' , 'Math' , 'Physics' , 'CompSci')
tuple_2=tuple_1

print(tuple_1)
print(tuple_2)
 
#tuple_1[0]= 'Art'   --error : tuple object doesn't support item assignment

# Sets
courses_sets={'History' , 'Math' , 'Physics' , 'CompSci'}
print(courses_sets)#print is not in same order of declaration
courses_sets={'History' , 'Math' , 'Physics' , 'CompSci','Math'}
art_courses={'History' , 'Math' ,'Art' , 'Design'}
print(courses_sets.intersection(art_courses))
print(courses_sets.difference(art_courses))
print(courses_sets.union(art_courses))

#empty data types
empty_list = []
empty_list = list()

empty_tuple = ()
empty_tuple = tuple()

empty_set = {} # This isn't right it's a dict
print(type(empty_set))
empty_set = set()
print(type(empty_set))