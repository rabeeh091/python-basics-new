#Return "orange" instead of "banana"?

fruits = ["apple","banana","kiwi","mango","banana"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)