# iterator
# names = ["Kimhan", "Huyly", "Nguon", "Tong"]
# for n in names: -> this call iterator
#     print(n)
#
# itr = iter(names) # we call iter() function from names list
# start = next(itr) # we call next() function from itr
# print(start)
#
# # Actually, eg: iter is __iter__ in python and we just write iter() then python will know
# # that we call __iter__ function

# create iteration class
class Iteration:
    def __init__(self, lst):
        self.lst = lst
        self.index = -1

    # python will know that we call this function
    # when we write iter()
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if self.index == len(self.lst):
            raise StopIteration
        return self.lst[self.index]

names = ["Kimhan", "Huyly", "Nguon", "Tong"]
itrClass = Iteration(names)
itr = iter(itrClass)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))
# print(next(itr))
