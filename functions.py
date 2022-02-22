# Purpose of functions is to avoid DRY. its already prepped and you don't have to rewrite code. Just call the function.
# Minimize lines of code.

# EG; if you want to create a square, without a function, you'll have to write the below code repeating yourself.

# turtle is a pre-installed package for drawing.

# import turtle

# my_turtle = turtle.Turtle()


# my_turtle.forward(100)
# my_turtle.right(90)

# my_turtle.forward(100)
# my_turtle.right(90)

# my_turtle.forward(100)
# my_turtle.right(90)

# my_turtle.forward(100)
# my_turtle.right(90)

# turtle.done()


# Creating a function: We'll loop through the code 4 times using the range function:


# def square():
# 	for i in range(4):
# 		my_turtle.forward(100)
# 		my_turtle.right(90)

# # calling the function:
# square()

# Taking a step further we can add arguments in the function and then use whatever argument we want when we call the function.

# def square(length, angle): # named these length and angle coz we're making a square. we could call them anything. 
# # 							#This creates the template for using however big square we want.
# 	for i in range(4):
# 		my_turtle.forward(length)
# 		my_turtle.right(angle)

# # calling the function:
# square(100, 90)

# # Now using different args for a bigger square:
# square(200, 90)

# To do multiple squares, we can loop through the FUNCTION:

# for i in range(36):
# 	square(100, 90)
# 	# moving to the right a bit will show us diff squares, otherwise it will keep drawing on itself.
# 	my_turtle.right(10)


# Using return in a function:

# def demo_func():
# 	print ('hello')

# demo_func()

# for i in range(5):
# 	demo_func()

# # using return will execute the function stopping short of outputting it:
# def demo_func(greeting, name):
# 	return f'{greeting} - {name}'
# # You can format the way you want to display the output by using the f string method.
# # Now to print it, you'll have to use the print statement:

# print (demo_func('Hello', 'Suhail'))

#Args and Kwargs (arguments and keyword arguments) - args is represented by * and kwargs **.
#args is used when you want to pass a list of items and kwargs when you want to pass a dictionary of items

# def employee_info(*a, **b):
# 	print(a)
# 	print (b)

# employee_info('suhail', 'malika', 'pissu', age=36, pay=240, salary= 310000)

# creating a function to find the index of the list:
# First break down what you want logically and write the code. then you can wrap it in a function.
my_list = ['suhail', 'yusuf', 'ebrahim']

# for i, v in enumerate(my_list):
# 	if v == 'yusuf':
# 		print (i, v)

# creating the function to find index:

def finding_index(list, target):
	for i, v in enumerate(list):
		if v == target:
			return i, v

	return 'We did not find the value'

# print(finding_index(list, 'yusuf'))

# x = 'global x'

# def words(x):
# 	y = 'local y'
# 	print (x)

# 	def inner():
# 		x = 'inner x'
# 		print (x)
# 	inner()

# words('hi')

