# boolean data type
# A boolean is a data type that can have one of two values: True or False.
b = True
b = False
print(b)  # Output: False
print(type(b))  # Output: <class 'bool'>

# set data type
#set
# A set is an unordered collection of unique elements.
# Sets are mutable, meaning you can add or remove elements from them.
s = {1, 2, 3, 1, 4, 5}
print(s)  # Output: {1, 2, 3, 4, 5}
print(type(s))  # Output: <class 'set'>
s.add(6)  # Adding an element to the set
print(s)  # Output: {1, 2, 3, 4, 5, 6}
s.remove(1)  # Removing an element from the set
print(s)  # Output: {2, 3, 4, 5, 6}
s1 = s.copy()  # Copying the set
print(s1)  # Output: {2, 3, 4, 5, 6}
s1.add(7)  # Adding an element to the copied set
print(s1)  # Output: {2, 3, 4, 5, 6, 7}
print(s)  # Output: {2, 3, 4, 5, 6}
s1.discard(2)  # Discarding an element from the copied set
print(s1)  # Output: {3, 4, 5, 6, 7}
s1.pop()  # Removing and returning an arbitrary element from the copied set
print(s1)  # Output: {4, 5, 6, 7} (or any other element depending on the set's internal order)
s1.update([8, 9])  # Updating the copied set with new elements
print(s1)  # Output: {4, 5, 6, 7, 8, 9}
s1.intersection_update([5, 6, 7])  # Keeping only elements present in both sets
print(s1)  # Output: {5, 6, 7}
s1.difference_update([5, 6])  # Removing elements present in the second set from the first set
print(s1)  # Output: {7}
s1.symmetric_difference_update([7, 8])  # Keeping elements present in either set but not both
print(s1)  # Output: {8}
s.clear()  # Clearing the set
print(s)  # Output: set()

# frozenset
# A frozenset is an immutable version of a set. Once created, you cannot add or remove elements from it.
# It is hashable and can be used as a key in dictionaries or as an element in other sets.
fs = frozenset([1, 2, 3, 4, 5]) # Creating a frozenset
print(fs)  # Output: frozenset({1, 2, 3, 4, 5})
print(type(fs))  # Output: <class 'frozenset'>

#binary data types
# bytes
# A bytes object is an immutable sequence of bytes. It is used to represent binary data.
# Bytes are often used for file I/O, network communication, and other low-level operations.
b = bytes([1, 2, 3, 4, 5])  # Creating a bytes object
print(b)  # Output: b'\x01\x02\x03\x04\x05' 
print(type(b))  # Output: <class 'bytes'>

#bytearray
# A bytearray is a mutable sequence of bytes. It can be modified after creation.
# Bytearrays are often used for binary data manipulation.
ba = bytearray([1, 2, 3, 4, 5])  # Creating a bytearray object
print(ba)  # Output: bytearray(b'\x01\x02\x03\x04\x05')
print(type(ba))  # Output: <class 'bytearray'>

#memoryview
# A memoryview is a view of the memory of a bytes or bytearray object. It allows you to access the underlying data without copying it. 
mv = memoryview(ba)  # Creating a memoryview object from a bytearray
print(mv)  # Output: <memory at 0x7f8c1c0b2d00> (address may vary)
print(type(mv))  # Output: <class 'memoryview'>