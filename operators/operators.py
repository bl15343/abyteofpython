#Divide and floor operator
print(13//3)

#Bitwise left shift, expecting 8
print(2<<2)

#Bitwsie right shift, expecting 2
print(8>>2)

#Bitwise AND, expecting 7
print(7&15)

#Bitwise OR, expecting 9
print(8|1)

#Bitwise XOR, expecting 9
print(8^1)

#Bitwise invert, expecting -6
#2's complement is -(x+1)
print(~5)

#>, <, >=, <=, ==, != are same as perl

#boolean NOT
x = True
print(not x) #False
print(not not x) #True

#boolean AND
y = True
print(y and x) #True
print(y and not x) #False

#boolean OR
z = False
print(z or y) #True
print(z or z) #False

#Math + assignment shortcuts are the same as perl
a = 2
a *= 2 #4
print(a)

a -= 2 #2
print(a)

a += 2 #4
print(a)

a **= 2 #16
print(a)

a //= 4 #4, 4.0 if not using the floor operator
print(a)

#Changing the order of evaluation
#Parens force evaluation of innards, as we expected from PEMDAS
b = (2+3) * 4 #20
print(b)

length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter', 2 * (length +breadth))
