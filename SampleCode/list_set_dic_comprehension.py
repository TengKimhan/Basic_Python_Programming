import math as m

# list, set, dictionary comprehension in python
# comprehension in python is transform one list, set or dictionary to another one

# # list comprehension
# # eg: we have list of numbers we want to squre number
# numbers = [1, 2, 3, 4, 5, 6]
# sqr_numbers = [result*result for result in numbers] # square the number
# print(sqr_numbers)
#
# # eg: find even numbers
# numbers2 = [2, 3, 5, 6, 8, 10, 12]
# even_numbers = [result for result in numbers2 if result%2 == 0] # find even numbers
# print(even_numbers)
#
# # eg: cube numbers
# numbers3 = [1, 2, 3]
# cube_numbers = [pow(result, 3) for result in numbers3] # cube the number
# print(cube_numbers)
#
# # eg: squre root of numbers
# numbers4 = [4, 9, 16, 49]
# sqrt_numbers = [m.sqrt(result) for result in numbers4] # find square root
# print(sqrt_numbers)


# set comprehension
# eg: we have list of numbers we want to square number
# set_number = {1, 2, 3, 4, 4 ,4}
# # print(set_number) # result will be 1, 2, 3, 4
# set_square = {result*result for result in set_number}
# print(set_square)
#
# # eg: find even numbers
# set_number2 = {1, 2, 3, 5, 3, 9, 10}
# set_even = {result for result in set_number2 if result%2==0}
# print(set_even)
#
# # eg: cube numbers
# set_number3 = {1, 2, 3, 4}
# set_cube = {pow(result, 3) for result in set_number3}
# print(set_cube)
#
# # eg: squre root of numbers
# set_number4 = {1, 4, 16, 9}
# set_sqrt = {m.sqrt(result) for result in set_number4}
# print(set_sqrt)

# dictionary comprehension
# cities = ["Phnom Penh", "Bangkok", "Ho Chi Minh", "New York"]
# countries = ["Cambodia", "Thailand", "Vietnam", "USA"]
# z = zip(cities, countries)
#
# dict = {key:value for key, value in z}
# print(dict)
#
# # print(z)
# # for key, value in z:
# #     print(key, value)
