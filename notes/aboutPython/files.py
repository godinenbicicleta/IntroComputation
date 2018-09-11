# create a file with the name 'kids' and open it for writing
nameHandle = open('kids', 'w')

#open file and write two lines:
for i in range(2):
    name = input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()

#open file and read lines
nameHandle = open('kids', 'r')
for line in nameHandle:
    print(line)
nameHandle.close()

# 'w' overwrites, to append we use 'a':
nameHandle = open('kids', 'a')

# read all contents of the file as one string:
nameHandle.read()

#other operatrions:
nameHandle.readline()
nameHandle.readlines()
nameHandle.write(s) # s is a string
nameHandle.writeLines(S) # S is sequence of strings
nameHandle.close() # closes file
