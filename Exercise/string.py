# 1. Create 3 variables to store street, city and country, now create address variable to store entire address.
#    Use two ways of creating this variable, one using + operator and the other using f-string.
#    Now Print the address in such a way that the street, city and country prints in a separate line
# 2. Create a variable to store the string "Earth revolves around the sun"
#    i. Print "revolves" using slice operator
#    ii. Print "sun" using negative index
# 3. Create two variables to store how many fruits and vegetables you eat in a day.
#    Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
#    Use python f string for this.
# 4. I have a string variable called s='maine 200 banana khaye'.
#    This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
#    Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

# 1.
street = "street"
city = "city"
country = "country"
address = street + " " + city + " " + country
address2 = f"{street} {city} {country}"
print("Address:", address)
print("Address2:", address2)

# 2.
str = "Earth revolves around the sun"
print("Silce operator:", str[6:14])
print("Negatice index:", str[-3:])

# 3.
x = "salad"
y = "apple"
str = f"I eat {x} veggies and {y} fruits daily"
print(str)

# 4. use replace in string
old_str = "maine 200 banana khaye"
old_str = old_str.replace("200", "10").replace("banana", "samosa")
print(old_str)
