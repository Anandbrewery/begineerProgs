message="Hello world"
message1="bobby's world"
message2='bobby\'s world'
message3=""" bobby's world was
a good cartoon in 1990"""
message4=''' bobby's world was
a good cartoon in 1990'''
print(message1)
print(message2)
print(message3)
print(message4 )
print("length of message 1",len(message1))
print(message[0]) # acessing particular char string
print(message[0:5]) #slicing the string--Hello
print(message[ :5]) #slicing the string--Hello default start=0
print(message[6:]) #slicing the string--Hello default end=len-1
#methods are functions that belong to an object
#every data type has it's own method
print(message.lower())
print(message.upper())
print(message.count('l')) #try for hello too
print(message.find("uni"))# -1 or returns starting index
print(message.replace('world','universe'))#returns the replaced value don't forget to assign it!
greeting="hello"
name="miachel"
message=greeting + ", " + name + ".Welcome!"
print(message)
message= '{}, {}.Welcome!'.format(greeting,name)#.format method {}
print(message)
#f strings access above 3.6 release
message= f'{greeting}, {name}.Welcome!'
message= f'{greeting}, {name.upper()}.Welcome!'
# get a help for all attribute and method when you  are struck
print(dir(name))# get all methods and attributes related to a string
print(help(str))# get detailed help regarding how the data type attributes and method  works 
print(help(str.lower))# get how lower method work's



