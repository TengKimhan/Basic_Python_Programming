# raise an Exception
# user defince exceptions class
# finally statement

# 1. Raise an Exception
# try:
#     raise MemoryError("memory error")
# except MemoryError as e:
#     print(e)

# 2. user define exception class
# user define exception inherit from generic class Exception
# class Accident(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     # print the exception message
#     def print(self):
#         print(self.msg)
#
# try:
#     raise Accident("Here is the accident error")
# except Accident as e:
#     e.print()

# 3. finally statement
# try:
#     f = open("test.txt")
#     # error
#     x = 1/0
# except FileNotFoundError as e:
#     print("Inside the try")
# f.close()
# print("Already close the file") # it doesn't reach to this point because it has an error

# that's why we use finally statement
try:
    f = open("test.txt")
    # error
    x = 1/0
except FileNotFoundError as e:
    print("Inside the try")
finally:
    f.close()
    print("Already close the file") # now we can close the file
