# 1. After flipping a coin 10 times you got this result,
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count_head = 0
for i in range(len(result)):
    if result[i] == "heads":
        count_head = count_head + 1
print(count_head)

# 2. Print square of all numbers between 1 to 10 except even numbers
lst = [result**2 for result in range(1, 11)]
print(lst)
lst2 = [result**2 for result in range(1, 11) if result%2 != 0]
print(lst2)
# 3. Your monthly expense list (from Jan to May) looks like this,