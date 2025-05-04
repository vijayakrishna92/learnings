#string
# string is a sequence of characters enclosed in single, double, or triple quotes
s = 'Hello World' # string
s = "Hello World" # string
s = '''Hello World''' # string
s = """Hello World""" # string
print(type(s)) # <class 'str'>
print(s[0]) # H accessing the first character
print(s[1:5]) # ello slicing the string from index 1 to 4
print(s[-1]) # d accessing the last character
print(s.upper()) # HELLO WORLD converting to uppercase
print(s.lower()) # hello world converting to lowercase
print(s.title()) # Hello World converting to title case
print(s.capitalize()) # Hello world converting to capitalize case
print(s.strip()) # Hello World removing leading and trailing whitespace
print(s.lstrip()) # Hello World removing leading whitespace
print(s.rstrip()) # Hello World removing trailing whitespace
print(s.replace('H', 'h')) # hello World replacing H with h
print(s.split()) # ['Hello', 'World'] splitting the string into a list of words
print(s.split('o')) # ['Hell', ' W', 'rld'] splitting the string into a list of words using o as separator
print(s.find('o')) # 4 finding the first occurrence of o
print(s.rfind('o')) # 7 finding the last occurrence of o
print(s.index('o')) # 4 finding the first occurrence of o
print(s.rindex('o')) # 7 finding the last occurrence of o
print(s.count('o')) # 2 counting the number of occurrences of o
print(s.startswith('H')) # True checking if the string starts with H
print(s.endswith('d')) # True checking if the string ends with d
print(s.isalpha()) # False checking if the string contains only alphabets
print(s.isalnum()) # False checking if the string contains only alphanumeric characters
print(s.isdigit()) # False checking if the string contains only digits
print(s.islower()) # False checking if the string is in lowercase
print(s.isupper()) # False checking if the string is in uppercase
print(s.isspace()) # False checking if the string contains only whitespace
print(s.isnumeric()) # False checking if the string contains only numeric characters
print(s.isdecimal()) # False checking if the string contains only decimal characters
print(s.isidentifier()) # False checking if the string is a valid identifier
print(s.isprintable()) # True checking if the string is printable
print(s.isascii()) # True checking if the string contains only ASCII characters
print(s.isunicode()) # False checking if the string contains only Unicode characters