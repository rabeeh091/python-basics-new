#Order the Result

# The json.dumps() method has parameters to order the keys in the result:
#Use the sort_keys parameter
# to specify if the result should be sorted or not:



import json

x = {
    "name": "john",
    "age":30,
    "married":True,
    "divorced":False,
    "childern":("Ann","Billy"),
    "pets":None,
    "cars": [
        {"model":" 230", "mpg": 27.5},
        {"model":"ford edge", "mpg":25.2}
    ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=5, sort_keys=True))