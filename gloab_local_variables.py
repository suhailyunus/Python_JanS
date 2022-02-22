# # Global & Local variables
# LEGB rule - Local, Enclosing, Global, Builtin
# First it looks for what is within the function(locally) then will look in the enclosing, then the global then builtin

x = 'Global X'

def demo():
	y = 'local y'
	print (y)


demo()

# the function is printing y since y is local. if we substitute print with x, it will look locally first then look out. so will print global x.

def demo():
	y = 'local y'
	print (x)


demo()

# creating an enclosing:

def word():
	x = 'outer x'
	print (x)



	def inner_word():
		nonlocal x
		x = 'enclosed x'
		print (x)
	inner_word()
word()