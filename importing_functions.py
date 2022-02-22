# The below will import a previously created function from another file. You don't have to rewrite the function.
# note how it is necessary to add fu before calling the function (line 9) to ensure that you are picking it from that file.
# Alternateily, you could say: 'from functions import finding_index as fi' and this will specify the function.

# import functions as fu

from functions import finding_index as fi, my_list

greetings = ['bye', 'hi', 'hey', 'hello', 'whatzup']

# Use this if # import functions as fu
# print (fu.finding_index(greetings, 'hello'))

# use this if from functions import finding_index as fi
# Note you don't even have to repeat the function. just use fi to call it.

print (fi(greetings, 'hello'))


# You can also import the list from a previous file. eg in functions, we have "my_list/" add that to from functions import...with a comma
print (fi(my_list, 'yusuf'))


# importing means there is a py file saved somewhere. many built in functions contained in files which you can finding
# you can use a location function to find the path.

# calendar is a builtin function. you can open it and see what its all about
import calendar

print (calendar.isleap(2022))