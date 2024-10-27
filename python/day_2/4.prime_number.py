# num = int(input("Enter a num: "))

# for num in range(1, 100):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i):
#                 break
#             else:
#                 print(num)


for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end="")
    print("\r")


#while loop

a = 1
while a < 10:
    print(a)
    a = a+1
print("all done")