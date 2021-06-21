import json
# read file
f = open("test.txt", "r")
s = f.read()
dic = json.loads(s) # load it as dictionary

for key in dic:
    print("Key", key)
    print("Value", dic[key])
