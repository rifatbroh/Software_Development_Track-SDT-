total_input = int(input("How many number: "))
count = 1
sum = 0.0

while count <= total_input:
    number = float(input("Enter number " + str(count) + ":"))
    sum += number
    count +=1
average = sum / total_input
print("average is", average)