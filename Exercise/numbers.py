# 1.You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
# 2.You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
# 3.You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
# 4.Print binary representation of number 17

# 1.
l = 92
wide = 48.8
area = l*wide
print(area)

# 2.
potato_packet = 9
each_packet = 1.49
give_cash = 20
real_pay = 9*1.49
print(give_cash - real_pay)

# 3.
tiles_length = 5.5
tile_area = tiles_length**2
total = tile_area * 500
print(total)

# 4.
print(bin(17))
print("Print binary use format", format(17, "b"))
