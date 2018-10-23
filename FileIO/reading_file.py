# Files

# open(file, mode, encoding, errors)
f = open("story.txt")

# read(n)  => n number of lines
print("first: ", f.read())
print("second: ", f.read())

# seek(n)  => n is the position of the character
f.seek(0)

print("After cursor seek(0)", f.read())

# readline()
# It returns the next current line, 1 by one
f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())

# readlines()
# It returns a list with all the lines
f.seek(0)
print(f.readlines())

# closed
# Boolean if its closed or not
print(f.closed)

# close()
# Close a file. Cant be readed again
try:
    f.close()
    print("File Closed")
except:
    print("Problem closing file")

# with
# Automatically close the file
with open("story.txt") as file:
    data = file.read()
    file.seek(0)
    
    for line in file:
        print("for", line)

print(file.closed)
print(data)
