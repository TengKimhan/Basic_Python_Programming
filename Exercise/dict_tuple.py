# 1. We have following information on countries and their population (population is in crores),
# Country	Population
# China	    143
# India	    136
# USA	    32
# Pakistan	21

# Using above create a dictionary of countries and its population
# Write a program that asks user for three type of inputs,
# print: if user enter print then it should print all countries with their population in this format
# i. add: if user input add then it should further ask for a country name to add.
#         If country already exist in our dataset then it should print that it exist and do nothing.
#         If it doesn't then it asks for population and add that new country/population in our dictionary and print it
# ii. remove: when user inputs remove it should ask for a country to remove.
#     If country exist in our dictionary then remove it and print new dictionary using format shown above in (a).
#     Else print that country doesn't exist!
# iii. query: on this again ask user for which country he or she wants to query.
#      When user inputs that country it will print population of that country.
# china==>143
# india==>136
# usa==>32
# pakistan==>21

# def print_all():
#     for key, value in dict.items():
#         print(f"{key}==>{value}")
#
# def add():
#     country = input("Please input country:")
#     if country in dict.keys():
#         print("Country already exist.")
#     else:
#         population = input("Please input population:")
#         dict[country] = population
#         for key, value in dict.items():
#             print(f"{key}==>{value}")
#
# def remove():
#     country = input("Please input country to remove:")
#     if country in dict.keys():
#         dict.pop(country)
#         for key, value in dict.items():
#             print(f"{key}==>{value}")
#     else:
#         print("Country doesn't exist!")
#
# def query():
#     country = input("Please input country to query:")
#     if country in dict.keys():
#         print(dict.get(country))
#     else:
#         print("Country doesn't exist!")
#
# def main():
#     user_input = input("Please input types print, add, remove, query:")
#     if user_input == "print":
#         print_all()
#     elif user_input == "add":
#         add()
#     elif user_input == "remove":
#         remove()
#     elif user_input == "query":
#         query()
#
# if __name__ == "__main__":
#     dict = {"China": 143,
#             "India": 136,
#             "USA": 32,
#             "Pakistan": 21}
#     main()

# 2. You are given following list of stocks and their prices in last 3 days,
# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]

# Write a program that asks user for operation. Value of operations could be,
# i. print: When user enters print it should print following,
# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33
# ii. add: When user enters 'add', it asks for stock ticker and price.
#     If stock already exist in your list (like info, ril etc) then it will append the price to the list.
#     Otherwise it will create new entry in your dictionary.
#     For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.

# def print_all():
#     for key, value in stock_price.items():
#         sum = 0
#         for i in value:
#             sum+=i
#         avg = sum/len(value)
#         print(f"{key} ==> {value} ==> avg: ", round(avg,2)) # round() to round float
#
# def add():
#     ticker = input("Please input stock ticker:")
#     price = int(input("Please input stock price:"))
#
#     if ticker in stock_price.keys():
#         stock_price[ticker].append(price)
#     else:
#         stock_price[ticker] = [price]
#     print_all()
#
# def main():
#     user_input = input("Please input operation:")
#     if user_input == "print":
#         print_all()
#     elif user_input == "add":
#         add()
#
# if __name__ == "__main__":
#     stock_price = {
#         "info": [600, 630, 620],
#         "ril": [1430, 1490, 1567],
#         "mtl": [234, 180, 160]
#     }
#     main()

# 3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter.
#    You should get these values in your main program by calling circle_calc function and then print them
import math


def circle_calc(radius):
    area = math.pi * (radius**2)
    circumference = 2*math.pi*radius
    diameter = 2*radius

    circle = {
        "area" : area,
        "circumference" : circumference,
        "diameter" : diameter
    }

    return circle

if __name__ == "__main__":

    user_radius = int(input("Please input radius:"))
    circle = circle_calc(user_radius)

    print("Area =", round(circle.get("area"), 2))
    print("Circumference =", round(circle.get("circumference"), 2))
    print("Diameter =", round(circle.get("diameter"), 2))