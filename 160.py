#Update Dictionary
# the update() method will update the dictionary
# with the items from the given argument

# the argument must be a dictionary
# or an iterable object with key:value pairs
# update the "year" of the car by using the update() method

thisdict = {
    "brand": "Ford",
    "model": "mustang",
    "year":1956,

}
thisdict.update({"year":2020})
print(thisdict)