# file handling
# open, read, write, append, close
file = open('test.txt', 'w') # open file in write mode
file.write('Hello World\n') # write to file
file.write('This is a test file.\n') # write to file
file.close() # close file

with open('test.txt', 'r') as file: # open file in read mode
    content = file.read() # read file
    print(content) # print file content
    file.seek(0) # move cursor to beginning of file
    lines = file.readlines() # read all lines
    print(lines) # print lines
    file.close() # close file
'''r, w, a, r+, w+, a+
r+ = read and write, w+ = write and read, a+ = append and read'''