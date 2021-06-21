# take an example of Generator in python

# define a function
# def remote_control():
#     yield "BBC" # yield is like return keyword
#     yield "CNN"
#
# itr = iter(remote_control()) # return an iterator object
# print(next(itr))
# print(next(itr))
# print(next(itr))

# create fibonacci in Generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

# use generator
for num in fib():
    if num > 100:
        break
    print(num)