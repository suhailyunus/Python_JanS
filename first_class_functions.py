# First class function = a function that has been assigned to a variable.

def square(x):
	return x * x

def cube(x):
	return x * x * x
#assigning the function to a variable
# result = square

# # since the variable is now a function, must be brackets and contain your argument
# print (result(5))
# print (result(6))

# We can also pass functions as an argument to another function

my_list = [1, 2, 3, 4]
# I want to square these numbers using the square function. I want the result to be in list ideally and not just iterated results.

# for i in my_list:
# 	print (result(i))

# # Taking it a step further, if we want to append these results to a list, we can use the append function.

# First create a list to which we can put the values in:

# squared_list = []

# for i in my_list:
# 	squared_list.append(result(i))

# print (squared_list)

# Now taking it a step further, we can make this into a function.

def square_func(function, list):
	result = []
	for i in my_list:
		result.append(square(i))
	return result

print (square_func(square, my_list))


def square_func(function, list):
	result = []
	for i in my_list:
		result.append(cube(i))
	return result

print (square_func(cube, my_list))
