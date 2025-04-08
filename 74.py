#upper() using list comprehension
from types import new_class

#Set the values in the new list to upper case?

fruits = ["apple","banana","kiwi","cherry","mango"]

newlist = [x.upper() for x in fruits]

print(newlist)