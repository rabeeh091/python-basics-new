#Arbitrary Arguments, *args

#If you do not know how many arguments that will
# be passed into your function,
# add a * before the parameter name in the function definition.

#This way the function will receive a tuple of arguments,
# and can access the items accordingly:

#If the number of arguments is unknown,
# add a * before the parameter name:

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("emil", "tobies","linus","amal")

#print("The kids are:")
#    for x in kids:
#       print(x)