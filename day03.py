dicts = {'name': 'suhail', 'age': 36, 'language': 'python'}

print (dicts)
# You can update values by accessing the key and updating it:

dicts['name'] = 'Yusuf'
print (dicts)

# Using the update function will add to the dict and not change the existing values:
dicts.update({'first': 'ebrahim'})
print (dicts)

dicts.update({'last':'muhammad', 'email': 'moe@gmail.com'})
print (dicts)

# To delete, use the delete function:

del dicts['email']
print (dicts)

# alternately, you can use the pop method:

dicts.pop('last')
print (dicts)

# to check which kay and value were removed, you can asign to a variable and print it:

removed = dicts.pop('first')
print (removed)
print(dicts)


#printing keys & values:

print (dicts.keys())
print (dicts.values())

#to print both keys and values use items:

print (dicts.items())

# You can iterate through a dictionary similar to a list.

for i, v in dicts.items():
	print (i, v)

# you can format the items as well by using the format method - refer to formatting strings:

for i, v in dicts.items():
	print (f' {i} -- {v}')

# use get method to access values
# use update to update in dict
# use del to delete keys or .pop()

