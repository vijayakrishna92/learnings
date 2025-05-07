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
print(s[::-1]) # dlroW olleH reversing the string
print(s[::2]) # Hlo ol slicing the string from start to end with step 2
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

# list
# list is a mutable sequence of elements enclosed in square brackets
l = [1, 2, 3, 'a', True, 1.2] # list of mixed data types
l = [1, 2, 3, [4, 5]] # list of lists
l = [1, 2, 3, (4, 5)] # list of tuples
l = [1, 2, 3, {4, 5}] # list of sets
l = [1, 2, 3, {4: 5}] # list of dictionaries
l = [1, 2, 3, None] # list of None
l = [1, 2, 3, True] # list of booleans
l = [1, 2, 3, 1.2] # list of floats
l = [1, 2, 3, 'a'] # list of strings
l = [1, 2, 3, b'abc'] # list of bytes
l = [1, 2, 3, bytearray(b'abc')] # list of bytearray
l = [1, 2, 3, memoryview(b'abc')] # list of memoryview
l = [1, 2, 3, frozenset([4, 5])] # list of frozenset
l = [1, 2, 3, 4, 5] # list of integers
print(type(l)) # <class 'list'>
print(l[0]) # 1 accessing the first element
print(l[1:3]) # [2, 3] slicing the list from index 1 to 2
print(l[-1]) # [5] accessing the last element
print(l[::-1]) # [5, 4, 3, 2, 1] reversing the list
print(l[::2]) # [1, 3] slicing the list from start to end with step 2
l.append(6) # appending 6 to the list
print(l) # [1, 2, 3, 4, 5, 6] appending 6 to the list
print(l.count(1)) # 1 counting the number of occurrences of 1
l.extend([7, 8]) # extending the list with [7, 8]
print(l) # [1, 2, 3, 4, 5, 6, 7, 8] extending the list with [7, 8]
print(l.index(1)) # 0 finding the first occurrence of 1
l.insert(0, 0) # inserting 0 at index 0
print(l) # [0, 1, 2, 3, 4, 5, 6, 7, 8] inserting 0 at index 0
print(l.pop()) # 8 removing the last element and returning it
l.remove(1) # removing 1 from the list
print(l) # [0, 2, 3, 4, 5, 6, 7] removing 1 from the list
l.reverse() # reversing the list
print(l) # [7, 6, 5, 4, 3, 2, 0] reversing the list
l.sort() # sorting the list
print(l) # [0, 2, 3, 4, 5, 6, 7] sorting the list
print(l.clear()) # clearing the list
m = l.copy() # copying the list
print(m) # [2, 3, 4, 5, 6, 7] copying the list
m[0] = 1 # modifying the copied list
print(m) # [1, 3, 4, 5, 6, 7] modifying the copied list
print(l) # [2, 3, 4, 5, 6, 7] original list remains unchanged
print(sum([1, 2, 3])) # Sum of a list
print(min([1, 2, 3])) # Minimum of a list
print(max([1, 2, 3])) # Maximum of a list
print(sorted([3, 2, 1])) # Sorted list
print(sorted([3, 2, 1], reverse=True)) # Sorted list in descending order
l = ['a', 'b', 'c'] # list of strings
print(''.join(l)) # abc joining the list of strings

# tuple
# tuple is an immutable sequence of elements enclosed in parentheses
t = (1, 2, 3, 4, 5) # tuple of integers
t = (1, 2, 3, 'a', True, 1.2) # tuple of mixed data types
t = (1, 2, 3, [4, 5]) # tuple of lists
t = (1, 2, 3, (4, 5)) # tuple of tuples
t = (1, 2, 3, {4, 5}) # tuple of sets
t = (1, 2, 3, {4: 5}) # tuple of dictionaries
t = (1, 2, 3, None) # tuple of None
t = (1, 2, 3, True) # tuple of booleans
t = (1, 2, 3, 1.2) # tuple of floats
t = (1, 2, 3, 'a') # tuple of strings
t = (1, 2, 3, b'abc') # tuple of bytes
t = (1, 2, 3, bytearray(b'abc')) # tuple of bytearray
print(type(t)) # <class 'tuple'>
print(t[0]) # 1 accessing the first element
print(t[1:3]) # (2, 3) slicing the tuple from index 1 to 2
print(t[-1]) # (4, 5) accessing the last element
print(t[::-1]) # ((4, 5), 3, 2, 1) reversing the tuple
print(t[::2]) # (1, 3) slicing the tuple from start to end with step 2
print(t.count(1)) # 1 counting the number of occurrences of 1
print(t.index(1)) # 0 finding the first occurrence of 1
print(t.index(1, 1)) # 2 finding the first occurrence of 1 after index 1
e = zip(t,t) # zipping the tuple
print(list(e)) # [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)] zipping the tuple


