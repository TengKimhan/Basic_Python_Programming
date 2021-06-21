# try and catch the exeption

# user input
x = input("Enter x = ")
y = int(input("Enter y = "))

try:
    result = x/y
except ZeroDivisionError as e:
    print("ZeroDivisionError: ", e)
    result = None
except TypeError as e:
    print("Exception TypeError")
    result = None
print("Result: ", result)
