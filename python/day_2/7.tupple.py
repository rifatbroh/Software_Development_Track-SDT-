# num = (1,2,3,4,5,6)
# print(num)

# #dictonary

# friends = {'rifat': 12, 'prome': 14, 'monnem': 16 }
# print(friends)
# print(type(friends))

# # general procss uisng dict

# player = dict(sakib =75, rahim = 45, somoya = 90)
# for item in player:
#     print("the plyer name is", item, player[item])


# #item add
# player ['rifat'] = 64
# print(player)

# # item update

# player['sakib'] = 45
# print(player)

# # item cancel

# del player['rifat']
# print(player)

# print(len(player))

"""
    format cheking:
        helo{}.format(variable_name);
        reverse system:
            define = {1}
            define = {0}
"""
a = 10
b = 50
print("value of a = {1}, value of b = {0}".format(a, b))
print("value of a is {}".format(a))
print("vlaue of b is {}".format(b))

name = input("Enter something: ")
print("The name of something is {}".format(name))



my_list = [1,2,3,4,5]
print("my list{}".format(my_list))


# python split and join

s = "hey party people"
print(s.split())

x = "amar sonar bangla ami tomay valovasi"
j = x.split()
for i in j:
    print(i)


# again join
print(" ".join(j))


# form list to join

num = ['hello', 'rifat', 'how', 'are', 'you']
print(" ".join(num))

"""
    string method:
        .upper() -- > captial kore dibe
        .lower() -- > smaller kore dibe
        .swapcase() -- > boro choto replace kore dibe
        s.replace("this", "that") -- > replace methode
        .count() -- > count number of char
        .find("helo") -- > find a word / char
        .join(num)
        .split() -- > divide string as a single word
"""