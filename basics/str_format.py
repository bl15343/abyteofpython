age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name,age))
print('Why is {0} playing with that python?'.format(name))

print('{} was {} years old when he wrote this book'.format(name,age))
print('Why is {} playing with that python?'.format(name))

print('{name} was {age} years old when he wrote this book'.format(name=name,age=age))
print('Why is {name} playing with that python?'.format(name=name))

print(f'{name} was {age} years old when he wrote this book')
print(f'Why is {name} playing with that python?')

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))

#keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

#Prevent newline character from being printed
print('a', end='')
print('b', end='')

#Print end with space
print('a', end=' ')
print('b', end=' ')
print('c')

#Inline newline
print('This is the first line\nThis is the second line')

#Break single contiguous print over lines with \
print('"This is the first sentence. \
This is the second sentence"')

#Raw string (no processing)
print(r"Newlines are indicated by \n")

