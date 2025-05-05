# type conversion
# type conversion is the process of converting a value from one data type to another.

a = '5'
print(type(a)) # <class 'str'>
b = int(a) # convert string to int
print(type(b)) # <class 'int'>
c = float(a) # convert string to float
print(type(c)) # <class 'float'>
d = bool(a) # convert string to bool
print(type(d)) # <class 'bool'>
e = list(a) # convert string to list
print(type(e)) # <class 'list'>
f = tuple(a) # convert string to tuple
print(type(f)) # <class 'tuple'>
g = set(a) # convert string to set
print(type(g)) # <class 'set'>
h = frozenset(a) # convert string to frozenset
print(type(h)) # <class 'frozenset'>
i = bytes(a, 'utf-8') # convert string to bytes
print(type(i)) # <class 'bytes'>
j = bytearray(a, 'utf-8') # convert string to bytearray
print(type(j)) # <class 'bytearray'>
k = memoryview(i) # convert bytes to memoryview
print(type(k)) # <class 'memoryview
l = str(b) # convert int to string
print(type(l)) # <class 'str'>