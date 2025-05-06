# conditional statements
# if, elif, else

# if condition
if True:
    print("This is true")

# if condition with else
if False:
    print("This is true")
else:
    print("This is false")

# if condition with elif and else
if False:
    print("This is true")
elif True:
    print("This is true")
else:
    print("This is false")

#case statement
# match case statement
# match case statement is similar to switch case statement in other languages
# match case statement is used to match a value against a set of values
a = 1
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case 3:
        print("a is 3")
    case _:
        print("a is not 1, 2 or 3")