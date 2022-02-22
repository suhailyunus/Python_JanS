prog_language = 'Java'

if prog_language == 'python':
	print ('you suck')

elif prog_language == 'Python':
	print ('youre good')

else:
	print ('no good')
# operators are: ==(is or is equal to) | > (greater than) | < (less than) | != (not equal) | >= | <= | is | not


# Using and | or | not in conditions:

skill = 'tableau'

if prog_language == 'Java' and skill == 'AWS':
	print ('you are a data scientist')

if prog_language == 'python' or skill == 'AWS':
	print ('you are a half data scientist')

else:
	print ('you are a fake')

if prog_language is not 'java':
	print ('you are wasting time')

