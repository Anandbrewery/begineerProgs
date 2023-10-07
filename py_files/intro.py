from my_module import find_index as fi ,test
import sys
courses=['History' , 'Math' , 'Physics' , 'CompSci']
index= fi(courses, 'Math')
print(index)
print(test)

''' import my_module as mm  mm.find_index() is valid 
import * imports all has diadvantages such as sometimes all 
would not get imported '''

print(\n sys.path)

# if module is not there in our home directory
#follow these steps
#import sys
#sys.path.append()
# the above one in manual path setting 
#add ur path in environment variables
