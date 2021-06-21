# set and the frozen set
# in set no duplicate element and it is unordered
# set doesn't allow index to access

# we can initialize set
# s = set()
# print(type(s)) # <class 'set'>
#
# # do some operation
# s.add(9)
# s.add(10)
# print(s) # -> {9, 10}
#
# # we cannot access through index
# # eg: s[0] -> error
#
# # set is support list as an in input in constructor
# lst = [1, 2, 3, 3, 4, 4, 5]
# s2 = set(lst)
# print(s2) # -> {1, 2, 3, 4, 5}

# set contain operation like union, intersect, difference, subset
# union
s1 = {1, 2, 3}
s2 = {2, 2, 4}
union = s1 | s2
print(union)

# intersection
intersect = s1 & s2
print(intersect)

# difference
dif = s1-s2
print(dif)

# check if s3 is subset of s1
s3 = {1}
print(s3<s1)
print((s1<s3))
