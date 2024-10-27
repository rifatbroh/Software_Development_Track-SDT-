"""
    python operator:
        1.  Arithmetic operators
        2.  Assignment operators
        3.  Relatational or comparison operator
        4.  Logical operator
        5.  Bitwise operator
        6.  Membership operator
        7.  Identity operators
"""

# Arithmetic operator (+, -, *, /, %)

a = 1
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a // b) # floar divison

# Assignment operators 

a += b
a -= b
a *= b
a /= b
a //= b # mod assign kora
a %= b  # modulus "
a ** b # exponent 
a &= b
a |= b
a ^= b 
a >>= b # right shift
a <<= b # left shift 

# Logical operator

a = True
b = True
print(a and b)

x = 4
y = 6
z = 3

print((x < y) or (y < z))
# one kind of reverse
print(not a)
print(not b)

# Relation / comparison operator
"""
    == Equal to
    != Not equal to
    <  Less than
    <= Less than or equal to
    >  Greater then
    >= Greater than or equal to
"""

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a <= b)
print(a < b)

# binary 

"""
    or
    xor
    and
    not
"""

rifat = 99
print(bin(rifat))

a = 9
c = a << 2

print(bin(c))
print(c)


# Membership operator (in, not in)

items = [1, 2, 3, 4, 5]
if 2 in items:
    print("item is exist")
else:
    print("item isn't exist")

if 6 not in items:
    print("item is not exits in the list")
else:
    print("item exits in the list")