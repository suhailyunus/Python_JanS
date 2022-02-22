print (range(10))

#range function performs a tast x number of times based on the range you define. You'll include it in a loop
#usually used to print multiple pages or repeat a task.
for i in range(0,5):
	print ('hello')

for i in range(5):
	print ('Bye')


#While loops: as long as condition is true, it will continue running unless you use the break statement.
#Using the += operator will allow the loop to continue running till you match the condition and then it will break.

x = 0

while x < 5: # x currently is less than 5 as it is 0. so it will continue running and printing 'hi. but will increment each time till
	#because of x += 1. Once it increments to 5, it will break.
	if x == 5:
		break
	print (x)
	x += 1

# Trying another example:

