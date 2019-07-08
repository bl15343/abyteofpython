import sys

# get name of attributes in sys module

print(dir(sys))

#only few entries shown here

# get names of attributes for current module
print(dir())

#Create new variable a
a = 5
print(dir())

del a

print(dir())