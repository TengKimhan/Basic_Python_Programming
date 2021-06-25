# 1. poem.txt contains famous poem "Road not taken" by poet Robert Frost.
#    You have to read this file in your python program and find out words with maximum occurance.
import re

word_value = {}

with open("poem.txt", "r") as f:
    i = 0
    for line in f:
        word_split = re.split(pattern=" |[.,:—!:;]", string=line.strip()) # strip() new line
        i+=1
        print("line", i)

        print("Before strip:", line)
        print("After strip:", line.strip()) # strip() newline character

        print("Before remove empty string:", word_split)

        # remove empty string after split word
        while "" in word_split:
            word_split.remove("")
        print("After remove empty string:", word_split)

        # add word and its occurance into dictionary
        for word in word_split:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1

# print key value pair of the dictionary
for key, val in word_value.items():
    print(f"{key} {val}")

print("Max value:", max(list(word_value.values())))
max = max(list(word_value.values())) # maximum value of occurance word

for key, value in word_value.items():
    if value == max:
        print(f"Max key and value: {key} {value}")

# 2. stocks.csv contains stock price, earnings per share and book value.
#    You are writing a stock market application that will process this file
#    and create a new file with financial metrics such as pe ratio and price to book ratio.
#    These are calculated as,

# pe ratio = price / earnings per share
# price to book ratio = price / book value
import csv

dic = {} # key "Company Name", "PE Ratio", "PB Ratio"

with open("stocks.csv", "r") as f:
    with open("output.csv", "w", newline="") as o:
        fieldName = ["Company Name", "PE Ratio", "PB Ratio"]
        writer = csv.DictWriter(o, fieldnames=fieldName) # user DictWrite() to write csv file with dictionary
        writer.writeheader() # include header with fieldname that already included

        for row in csv.DictReader(f): # DictReader() to read dictionary
            pe_ratio = int(row["Price"]) / int(row["Earnings Per Share"])
            price_to_book_ratio = int(row["Price"]) / int(row[" Book Value"])
            company_name = row["Company Name"]

            dic["Company Name"] = company_name
            dic["PE Ratio"] = round(pe_ratio, 2)
            dic["PB Ratio"] = round(price_to_book_ratio, 2)

            writer.writerow(dic) # write to each row



