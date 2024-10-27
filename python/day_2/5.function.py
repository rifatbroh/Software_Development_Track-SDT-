"""
    def funtion_name(Parameters):
        statements
        return
"""

def greet():
    print("Welcome to python programming")
greet()

def add(a, b):
    print("add is ", a+b)

add(10, 2)

def name(n):
    print("My name is: ", n)

name("rifat")

def add(a, b):
    return a+b
print(add(2,3))


# take as a user input

def num(a, b):
    return a+b

num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))

print(num(num1, num2))