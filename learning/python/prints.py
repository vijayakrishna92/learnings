# Prints in Python
print('hello world') # single quotes are used for strings
print("hello world") # double quotes are used for strings
print("""hello world""")  # triple quotes are used for multi-line strings
print('''hello world''') # triple quotes are used for multi-line strings
print('hello world', end='') # end is an optional parameter, it specifies what to print at the end of the line, by default it is a newline character
print() # print a newline character
print(None) # None is a special value in Python, it represents the absence of a value or a null value
print("hello","world", sep="@") # sep is a separator, it separates the strings with the given separator
print("hello 'world'") # ' is a single quote, " is a double quote, they can be used interchangeably
print('hello "world"') # ' is a single quote, " is a double quote, they can be used interchangeably
print("hello \"world\"") # \ is an escape character, it allows you to use special characters in a string
print("hello \'world\'") # \' is an escape character, it allows you to use special characters in a string
print(r"hello \"world\"") # r is a raw string, it ignores escape characters
print("hello \n world") # \n is a newline character
print("hello \t world") # \t is a tab character
a1 = 1
print(f"hello {a1}") # f-string
print("hello {}".format(a1)) # format method