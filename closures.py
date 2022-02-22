# If you have mutiple functions, inner and outer, when you assign the function to a variable,
# It will be the inner function.

def outer_function():
	message = 'hello'


	def inner_function():
		print (message)

	return inner_function()


result = outer_function()
print (result.__ne__)
