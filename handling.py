# this is used for how many line in the code
with open('assert.py', "r") as f:
    lines = f.readlines()

    print(f'total lines: {len(lines)}')

# this is used for reading the file
    with open ("assert.py")as f:
        print(f.read())

# readline can display the first line
f = open('assert.py', "r")
print(f.readline())
print(f.readline())

# using loop to read whole file line byline
with open ("assert.py")as f:
    for x in f:
        print(x)
# write i sused to write the new line in the file
with open ("assert.py", "a") as f:
    f.write ("this is the new line in the code\n")
with open("assert.py")as f:
    print(f.read())    

 # over writing the file
with open ("assert.py", "w") as f:
    f.write ("this is the new line in the code\n") 

# create is used for creating the new file
   



        
