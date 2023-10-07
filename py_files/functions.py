# keep your code DRY(don't repeat yourself)
def hello_func():
	# pass : in case dont want to do anything now but after i will the suite
	#print('Hello Function!')
	return 'Hello Function.'
def hello_funcs(greeting,name=You):
	return '{} , {}.'.format(greeting,name)

hello_func()
print(hello_func)# shows the object type and memory location
print(hello_func)# None if empty or return value
#knowing the ip and op of  the function is enoughlike len() function
print(hello_funcs('Hi'))
print(hello_funcs('Hi' , name='Rakuten'))

def student_info(*args, **kwargs):
	print(arg)#tuple 
	print(kwargs)#dictionary
student_info('Math','Art',name='John', age=22)


def student_infos(*args, **kwargs):
	print(arg)#tuple 
	print(kwargs)#dictionary

courses=['Math','Art']
info={name='John', age=22}

student_infos(*courses,**info)



