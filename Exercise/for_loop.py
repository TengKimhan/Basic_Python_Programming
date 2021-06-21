# 1. After flipping a coin 10 times you got this result,
# Using for loop figure out how many times you got heads

# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# count_head = 0
# for i in range(len(result)):
#     if result[i] == "heads":
#         count_head = count_head + 1
# print(count_head)

# 2. Print square of all numbers between 1 to 10 except even numbers
# lst = [result**2 for result in range(1, 11)]
# print(lst)
# lst2 = [result**2 for result in range(1, 11) if result%2 != 0]
# print(lst2)

# 3. Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
# If expense is not found then it should print that as well.
# user_expense = int(input("Enter expense amount:"))
# if user_expense in expense_list:
#     index = expense_list.index(user_expense)
#     if index == 0:
#         print("January")
#     elif index == 1:
#         print("Febraury")
#     elif index == 2:
#         print("March")
#     elif index == 3:
#         print("May")
# else:
#     print("Not found")

# 4. Lets say you are running a 5 km race. Write a program that,
#
# i. Upon completing each 1 km asks you "are you tired?"
# ii. If you reply "yes" then it should break and print "you didn't finish the race"
# iii. If you reply "no" then it should continue and ask "are you tired" on every km
# iv. If you finish all 5 km then it should print congratulations message

for i in range(5):
    users = input("Are you tired?")
    if users == "yes":
        print("you didn't finish the race")
        break
    else:
        continue

if i == 4:
    print("Congratulation")
