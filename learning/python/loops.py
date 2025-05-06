#loops

#for loop
#for loop is used when the number of iterations is known
for i in range(5): #range(start, stop, step)
    print(i)
#nested for loop
for i in range(5):
    for j in range(5):
        print(i, j)
#for loop with else 
for i in range(5):
    print(i)
else:
    print("Loop finished")

#while loop
#while loop is used when the number of iterations is not known
i = 0
while i < 5:
    print(i)
    i += 1
# nested while loop
i = 0
while i < 5:
    j = 0
    while j < 5:
        print(i, j)
        j += 1
    i += 1
#while loop with else   
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")
    
#break, continue and pass
#break is used to exit the loop
#continue is used to skip the current iteration and continue with the next iteration
#pass is used to do nothing and continue with the next iteration
for i in range(5):
    if i == 2:
        break
    print(i)
for i in range(5): 
    if i == 2:
        continue
    print(i)
for i in range(5):
    if i == 2:
        pass
    print(i)