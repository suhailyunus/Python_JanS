'''
1. In the below elements which of them are values or an expression? 
eg:- values can be
integer or string and expressions will be mathematical operators.

* expression
'hello' - value (string)
-87.8 - value(float)
- expression
/ expression
+ expression
6 value (integer)

2. What is the difference between string and variable?

a string is a data type that is made up of contextual data. A variable is a container that can store different data types (strings/integers, lists, dictionaries etc)

3. Describe three different data types.

string - textual data eg; 'hello'
integer - numerical data consisting of a whole number, eg, 4 100 
float - numerical data with decimals. eg, 5.9

4. What is an expression made up of? What do all expressions do?

An expression is a combination of values and functions. Eg: 4 * 4. Expressions produce a certain result that we want when forming the expression.

5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

The expression is the entire phrase (spam = 10). In this case, there is no difference between it being an assignment statement and expression.

6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

Still bacon contains 22. If we wanted to increment it, we should have used +=

7. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3

'spam' + 'spamspam' = spamspamspam
'spam' * 3 = spamspamspam

8. Why is eggs a valid variable name while 100 is invalid?

variables must start with string data. It can contain numbers but it must start with text.


9. What three functions can be used to get the integer, floating-point number, or string version of a value?

str will get the string version of a value. int will get the whole number of a value. eg, we can cast7.0 to 7 using the int() function.
float() will return the value in float form. eg; 7 can be cast to 7.0 using the float() function.

10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 + 'burritos.'

Because string and integer cannot be concatenated. We can fix this by surrounding 99 with quotes so it turns into a string.
Like this: print ('I have eaten' + ' 99 ' + 'burritos.')

create 2 variables message and greeting and assign a values Morning and Hey. Using string representation methods. i.e .format and f'strings' display the output 'Hello, Good Morning'

message = 'Hello'
greeting = 'Good Morning'

print (f'{message}, {greeting}')
'''


