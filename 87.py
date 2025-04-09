#Another way to join two list
#is by appending all the items from list2 into list ,one by one!

#Append list2 ant list1

list1 = ["a","b","c"]
list2 = [1,2,3]

for x in list2:
    list1.append(x)

print(list1)