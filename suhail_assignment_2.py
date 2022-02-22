'''

1.What are the two values of the Boolean data type? How do you write them?

True | False

2. What are the three different types of Boolean operators?

and | or | not

3. Make a list of each Boolean operator's truth tables 
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).

prg_lang = 'Python'
additional_lang = 'R'

if prg_lang == 'Java':
	print ('You are good')
elif prg_lang == 'Java' or additional_lang == 'Rust':
	print ('You are satisfactory')
elif prg_lang == 'Python' and additional_lang == 'R':
	print ('You are a data analyst')


4. What are the values of the following expressions?
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)

(5 > 4) and (3 == 5)
False
not (5 > 4)
False 
(5 > 4) or (3 == 5)
True
not ((5 > 4) or (3 == 5))
True
(True and True) and (True == False)
(not False) or (not True)

5. What are the six comparison operators?

==
!=
>
<
>=
<=

6. How do you tell the difference between the equal to and assignment operators?
Describe a condition and when you would use one.

equal to is used twice. when used once, its an assignment operator. eg; age = 27 is assigning 27 to age. whereas age == 27 means the age is equal to 27.


7. Write and Identify the three blocks in this code:

spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

spam = 0 - This is assigning 0 to the variable spam.

if spam == 10:
print('eggs')

This is a boolean statement if spam is equal to 10, it will print eggs, otherwise nothing will be printed. Here nothing will be printed.

if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

Here the statement will also return false as spam = 0. The else statement will come into effect where ham spam spam will be printed.(ussiming that indentation was applied to be in the if statement)

8. Write code that prints Hello if 1 is stored in spam, prints Hey if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

spam = 1

if spam == 2 or 1:
	print ('Hello')
else:
	print ('Greetings!')

9.If your programme is stuck in an endless loop, what keys you’ll press?

escape.

10. How can you tell the difference between break and continue?

break will cause the loop to terminate wherease continue will cause the loop to move on to the next step. eg:

for val in 'suhail':
	if val == 'i':
		break
	print (val)

this will cause it to print up to but excluding i and the loop will end.


for val in 'suhail':
	if val == 'i':
		continue
	print (val)

this will cause it to execute the loop and print all the values excluding i since it skipped/continued on i.


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

No difference. All will execute the same. first two are self explanatory. range(0, 10, 1) takes it from 0-10 and then drops to 1. since 0-10 is already printed, result is same.

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.

for i in range(11): print(i)

While loop:
x = 0


while x < 11:
	if x == 11:
		break
	print (x)
	x += 1

13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?

First I'd create the function and save it as a .py file.

Then in a new or another file, i'd import it using the import function:
import spam.py

Then i'd call the function after the import.

def bacon(name):
  print("Hello, " + name)

The next step would be to save this as spam.py

In another file, 

import spam.py

then call the function:
spam.bacon('John')

This will print 'Hello John'
'''
