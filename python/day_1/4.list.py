# """
#     list:
#         list contains many types of data like int, string etc
#         list has special things that is, can iterate reverse
# """
# colors = ['red', 'green', 'blue', 'white']

# print(colors[0])
# print(colors[1])
# print(colors[2])
# print(colors[3])

# print(colors)

# # iterate reverse
# print(colors[-1])

# box = ['python', 3.1416, 976]
# print(box[0])
# print(type(box[0]))
# print(type(box[1]))
# print(type(box[2]))

# # new item adding called append
# colors.append('orange')
# colors.append('mango')
# print(colors)

# # extend()

colors = ['red', 'blue', 'green']
colors.append('white')
colors.extend(['yellow', 'indigo', 'violet'])
print(colors)
print(len(colors))

# remove item from list
colors.remove('red')
colors.remove('green')
print(colors)
print(len(colors))