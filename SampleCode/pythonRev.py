# 1. Variable
# var = 10 -> can be int, float, string, double all data type just insert like this
# print(var), print("We can print multi variable", var1, var2, var3)

# 2. Number
# substract = 10 - 4
# add = 10 + 4
# multiple = 10 * 4
# power = 10**2
# divide = 10/2
# modulo = 10%4
# floor = 10//4
# use_round = round(divide)
# print("Operation is python: ", substract, add, multiple, power, divide
#                             ,modulo, floor, use_round)

# 3. String
# stri = "Hello world"
# print(stri[:5])
# print(stri[6:])
# multi_line = '''hello world
# my name is Kimhan
# What's your name?
# '''
# print(multi_line)
# cast = str(10)
# concate = stri + cast
# print(concate)

# 4. List
# lst = ["first", "Second", "Third"]
# lst2 = ["Second List", "Blah Blah"]
# print(lst)
# print(lst[:2])
# print(lst[-1]) # -1 mean first index but from the end
# # add more item
# lst.append("Fourth")
# # length
# print(len(lst))
# # insert()
# lst.insert(1, "hello")
# # join list
# combine = lst + lst2
# print(combine)
#
# # using iterator
# for l in lst:
#     print(l)

# 5. if statement
animal = ["dog", "cat", "tiger", "lion", "mouse"]
fruit = ["apple", "grape", "banana", "straberry"]

# input
# choice = input("Enter a string: ")
# if choice in animal:
#     print("It is an animal: ", choice)
# elif choice in fruit:
#     print("It is a fruit: ", choice)
# else:
#     print("Don't know")

# 6. for loop
# price = [10, 20, 30, 40, 50, 60]
# for item in price:
#     print(item)
#
# for idx in range(len(price)):
#     print(price[idx])
#
# i = 0
# while i <= len(price):
#     print(price[i])
#     i = i + 1

# 7. function
# def mul(lst):
#     for idx in range(len(lst)):
#         lst[idx] = lst[idx] * 2
#     return lst
#
# num1 = [1, 2, 3, 4, 5, 6]
# num2 = [10, 20, 4]
#
# print("List one: ")
# print (mul(num1))
# # print("List two: ", mul(num2))

# 8. Dictionary
# dic = {"key1": "Value1", "key2": "Value2", "key3": "Value3"}
# point = (1,2) # tuple
#
# # add dictionary
# dic["Key4"] = "Value4"
# # delete dictionary
# del dic["Key4"]
#
# for k, v in dic.items():
#     print("Keys: ", k, "Values: ", v)
#
# for item in point:
#     print(item)

# 9. Working with Json
import json
# create books dictionary
book = {}
book["tom"] = {
    "name": "tom",
    "age": 15,
    "position": "student"
}

book["john"] = {
    "name": "john",
    "age": 20,
    "position": "banker"
}
# convert to json file
s = json.dumps(book)
# write a file
with open("test.txt", "w") as f:
    f.write(s)









