message = ['hello', 'bye', 'hi']
list_elements = [message[0], message[-1]]
print (list_elements)

# append adds to the list
message.append('Hey')
print (message)

# insert lets you add at whatever index point you wish
message.insert(2, 'Cool')
print (message)

# using append or insert to merge another list to a list will add in list form which we don't want
words = ['super', 'cute']

# message.append(words)
# print (message)

# use extend instead to add list to list

message.extend(words)
print (message)


# updating list or modifying a list:

message[0] = 'idiot'
# removing items from a list

message.remove('hi')
print (message)

# using .pop() will also remove but must use index of item and not the explicit item
message.pop(1)
print (message)

# for_loop -iterating through list:

for i in message:
	print (i)

# using the enumerate function in the loop will also give us the index of the list item
for i in enumerate(message):
	print (i)
# using another word after the for will give us neater output

for index, i in enumerate(message):
	print (index, i)

# formatting stings in a list - you can use any form of punctuation:

formatted_no_commas = ' '.join(message)
print (formatted_no_commas)

formatted_dashes = '-'.join(message)
print(formatted_dashes)


# sets create a list which will return distinct values. sets are created by using explicit "set" or {}. better
# better to use explicit set coz {} is also used for dictionaries


sets = {'idiot', 'crazy', 'idiot', 'good', 'crazy'}
print (sets)