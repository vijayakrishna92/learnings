#functions
# functions are reusable pieces of code that perform a specific task
# they can take inputs (arguments) and return outputs (return values)
def greet(): # function definition
    pass

greet() # function call

def add(a, b):
    return a, b, a + b

a, b, var_1 = add(1, 2)
print(a, b, var_1)

#sending function as an argument to another function
def greet(name):
    return f"Hello, {name}!"
def greet_user(greeting_function, name):
    return greeting_function(name)

var_2 = greet_user(greet, "Alice")
print(var_2)

# *args and **kwargs
# *args is used to pass a variable number of non-keyword arguments to a function
# **kwargs is used to pass a variable number of keyword arguments to a function

def add(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(add(1, 2, 3, 4, 5))
print_info(name="Alice", age=30, city="New York")

#function recursion
# recursion is a technique where a function calls itself to solve a problem
# it is used to solve problems that can be broken down into smaller subproblems
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial_result = factorial(5)
print(factorial_result)

# lambda functions
# lambda functions are anonymous functions that can take any number of arguments but can only have one expression
# they are often used for short, throwaway functions that are not reused elsewhere in the code
var_3 = lambda x: x * 2
print(var_3(5))

var_4 = lambda x, y: x + y
print(var_4(5, 10))

var_5 = lambda x: "even" if x % 2 == 0 else "odd"
print(var_5(5))
