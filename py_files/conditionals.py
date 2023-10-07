# if block
if True:
	print('conditionals was true')
if False:
	print('conditionals was true')
#if else bock
lang='Python'

if lang == 'Python':
	print('lang is py')
else:
	print('No match')
#elif block
lang='Java'

if lang == 'Python':
	print('lang is py')
elif lang='Java':
	print('lang is Java')
else:
	print('No match')

''' object identity: is #same obj in memory
boolean operators: 
	or
	and
	not '''
 user='Admin'
logged_in=False

if user='Admin' and logged_in:
	print('admin') 
else:
	print('Bad Creds')

logged_in=True

if user='Admin' or logged_in:
	print('admin') 
else:
	print('Bad Creds')

logged_in=False

if not logged_in:
	print('please log in') 
else:
	print('Welcome')
a=[1,2,3]
b=[1,2,3]
print(a==b)#True
print(id(a))
print(id(b))
print(a is b)#False
print(id(a)==id(b))# is 

# False Values:
	#0
                   #False
	#None
	#Zero of any numeric type
	#Any empty sequence. For example, ' ', ( ), [].
	#Any empty mapping. For example, { } .





 
