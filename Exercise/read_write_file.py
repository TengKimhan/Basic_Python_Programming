
# 1. poem.txt contains famous poem "Road not taken" by poet Robert Frost.
#    You have to read this file in your python program and find out words with maximum occurance.
import re

word_value = {}

with open("poem.txt", "r") as f:
    for line in f:
        line_split = re.split("\s|[.,:—!:;]", line)
        for word in line_split:
            if word in word_value:
                word_value[word] +=1
            else:
                word_value[word] = 1

word_occurance = list(word_value.values())
max = max(word_occurance)
for key, value in word_value.items():
    if value == max:
        print(f"{key} {value}")


# word_stats={}
#
# with open("poem.txt","r") as f:
#     for line in f:
#       words=line.split(' ')
#       for word in words:
#         if word in word_stats:
#           word_stats[word]+=1
#         else:
#           word_stats[word] = 1
#
# print(word_stats)
#
# word_occurances = list(word_stats.values())
# max_count = max(word_occurances)
# print("Max occurances of any word is:",max_count)
#
# print("Words with max occurances are: ")
# for word, count in word_stats.items():
#     if count==max_count:
#         print(word)


# 2. stocks.csv contains stock price, earnings per share and book value.
#    You are writing a stock market application that will process this file
#    and create a new file with financial metrics such as pe ratio and price to book ratio.
#    These are calculated as,

# pe ratio = price / earnings per share
# price to book ratio = price / book value
