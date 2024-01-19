# import random
#*args
# def add(*args):
#     sum =0
#     args = list(args)
#     args[0] = 99
#     for i in args:
#         sum+=i
#     return sum
# print(add(1,2,3,4,5))

# #*kwargs
# def addkw(**kwargs):
#     kwargs['first'] = "Harsh"
#     print('Hello, ' + kwargs['first'] + " " + kwargs['last'])

# addkw(first="Bro" , last="BRO")

#random
# random_int = random.randint(1,6)
# print(random_int)

#file handling
with open("main.py","w") as file:
    content = file.write("Hello Bro")
    print(content)