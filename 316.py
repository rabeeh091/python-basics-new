#Open the file "demofile.txt" and overwrite the content ?

f = open("demofile.txt", "w")
f.write("woow! i so good person ")
f.close()

#open and read the file after the overwriting !

f = open("demofile.txt", "r")
print(f.read())
f.close()