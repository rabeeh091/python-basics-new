#The continue statement

#with the continue statement we can stop the current iteration,
#and continue with the next:

#continue to the next iteration if i is 3?

i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
