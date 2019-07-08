shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

#Indexing or 'Subscription' operation #
print('Item 0 is', shoplist[0])
print('Item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

# Slicing on a list #
print('Item 1 to 3 is', shoplist[1:3])
print('Item 2 to end is', shoplist[2:])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

# Slicing on a string
print('Characters 1 to 3 is', name[1:3])
print('Characters 2 to end is', name[2:])
print('Characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

#Third argument to slice indicates the step

print('All items by 1', shoplist[::1])
print('All items by 2', shoplist[::2])
print('All items by 3', shoplist[::3])
#In reverse!
print('All items reversed', shoplist[::-1])


