#mapping type
# A mapping type is a collection of objects that are stored as a key-value pair.
# The key is used to access the value. The key must be unique and immutable. The value can be of any type.
# The most common mapping type in Python is the dictionary.
# A dictionary is a collection of key-value pairs. The keys are unique and the values can be of any type.
# A dictionary is created using curly braces {} or the dict() constructor. 
# The keys and values are separated by a colon : and the key-value pairs are separated by commas ,.

d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(d) # {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(d)) # <class 'dict'>
print(d['name']) # John key to access value
a = d.copy() # copy the dictionary
print(a) # {'name': 'John', 'age': 30, 'city': 'New York'}
a['name'] = 'Jane' # change the value of the key 'name'
print(a) # {'name': 'Jane', 'age': 30, 'city': 'New York'}
print(d) # {'name': 'John', 'age': 30, 'city': 'New York'}
print(d.get('name')) # John get the value of the key 'name
print(d.items()) # return a view object that displays a list of a dictionary's key-value tuple pairs
print(d.keys()) # return a view object that displays a list of all the keys in the dictionary
print(d.values()) # return a view object that displays a list of all the values in the dictionary
print(d.popitem()) # remove the last inserted key-value pair and return it as a tuple
print(d.setdefault('name')) # return the value of the specified key. If the key does not exist, insert the key with the specified value
d.update({'name': 'Jane'}) # update the dictionary with the specified key-value pair
print(d) # {'name': 'Jane', 'age': 30, 'city': 'New York'}
print(d.clear()) # remove all the elements from the dictionary