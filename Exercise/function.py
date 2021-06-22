# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
# Equation of an area of a triangle is, area = (1/2)*base*height
# def calculate_area(base, height):
#     return (1/2)*base*height

# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is, rectangle area=length*width
def calculate_area(base, height, type="triangle"):
    area = 0
    if type == "triangle":
        area = (1/2)*base*height
    elif type == "rectangle":
        area = base*height
    return area

# print(calculate_area(4,4))

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
def print_pattern(num):
    for i in range(num+1):
        s = ""
        for j in range(i):
            s+="*"
        print(s)

print_pattern(3)