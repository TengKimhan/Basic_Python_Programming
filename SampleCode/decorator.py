# Decorator
import time

# create decorator function to calculate time executing of function below
def time_dec(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs) # value of calculate square and cube
        end = time.time()
        print(func.__name__ + "Take", (end-start)*1000, "millisecon")
        return result
    return wrapper

# calculate square number
@time_dec # decorate on function that we prefer
def cal_square(numbers):
    result = [num*num for num in numbers]
    return result

# Calculate cube number
@time_dec
def cal_cube(numbers):
    result = [pow(num,3) for num in numbers]
    return result


numbers = range(1,10000)

square_numbers = cal_square(numbers)
cube_numbers = cal_cube(numbers)