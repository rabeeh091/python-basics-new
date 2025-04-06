# Global Variables

#create a variables outside of a function, and use it inside
#the function & outside the function.

x = "awesome" #scope of x is global

def myfunc():

    print("python is " + x)

myfunc()
print(x)