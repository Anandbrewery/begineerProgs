nums = [1, 2, 3, 4, 5]

for num in nums:
	print(num)
#break: to break loop after certain condition

for num in nums:
	if num == 3:
		print('Found!')
		break
	print(num)
# output: 1\n2 \nFound!

#continue: to continue loop after certain condition is met too
for num in nums:
	if num == 3:
		print('Found!')
		continue
	print(num)
# output: 1\n2 \nFound!\n4\n5


for num in nums:
	for letter in 'abc':
		print(num, letter)


#using the range function

for i in range(10):
	print(i)
#output:0 to 9 inclusive of both

for i in range(1,11):
	print(i)
#output:1 to 11 inclusive of both


# using the While loop

x=0
while x < 10:
	print(x)
	x+=1

x=0
while x < 10:
	if x == 5:
		break
	print(x)
	x+=1
#ctrl c to stop the infinite loop if u dont use break statement or false condition
x=0
while True :
	if x == 5:
		break
	print(x)
	x+=1


