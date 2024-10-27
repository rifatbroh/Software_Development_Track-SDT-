a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

if a > b:
    print("a is greater than b")
elif a == b:
    print("both are equal")
else:
    print("a is less than b")



x = 7
y = 5
z = 9
if x > y and z > y:
    print("Both condition are true")
else:
    print("bla bla bla")


yy = 5
if yy > 0:
    if yy%2 == 1:
        print("The  num is positive and odd number")




x = int(input("Enter a number:"))
if x > 0:
    if x % 2 == 1:
        print("The number is positive and an odd number.")
    else:
        print("The number is positive and an even number")
else:
    print("You entered a negative number")