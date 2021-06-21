# 1. Using following list of cities per country,
# i.  Write a program that asks user to enter a city name and it should tell which country the city belongs to
# ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
#     For example if I enter mumbai and chennai, it will print "Both cities are in India"
#     but if I enter mumbai and dhaka it should print "They don't belong to same country"
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# i.
user_city = input("Enter a city name:")
if user_city in india:
    print(f"{user_city} is in India")
elif user_city in pakistan:
    print(f"{user_city} is in Pakistan")
elif user_city in bangladesh:
    print(f"{user_city} is in Bangladesh")
else:
    print("None")

# ii.
# first_city = input("Enter first city name:")
# second_city = input("Enter second city name:")
#
# if first_city and second_city in india:
#     print("Both cities are in India")
# elif first_city and second_city in pakistan:
#     print("Both cities are in Pakistan")
# elif first_city and second_city in bangladesh:
#     print("Both cities are in Banglasdesh")
# else:
#     print("None")

# Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

# user_sugar = int(input("Enter your sugar to check it is normal or not:"))
# if user_sugar in range(80, 101):
#     print("Normal fasting level sugar")
# elif user_sugar < 80:
#     print("Sugar is low")
# else:
#     print("It is high")