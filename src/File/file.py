#when we use a file in python we first make to know the modes 
#modes are 
# 'r' - read mode
# 'w' - write mode
# 'a' - append mode 
# 'r+' - read and write mode
# 'w+' - write and read mode    
# 'a+' - append and read mode       
# 'b' - binary mode 
# 't' - text mode 
# 'U' - universal newline mode 
# 'x' - exclusive creation mode 
# and this format is not change always open("filename", "mode")

#Reading files 
file = open("example.txt", "r")
content =file.read()
print(content)

#read line by line 
file = open("example.txt", "r")
content = file.readlines()
for line in content:
    print(line)

#read into a list
file = open("example.txt", "r")
lines = file.readlines()
print(lines)  # ['First line\n', 'Second line\n', ...]
file.close()

#write a files 
file = open("example.txt", "w")
file.write("Hello, world!")
file.close

#append to a file 
file = open("example.txt", "a")
file.write("Hello, world!")
file.close

#with and as 
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

#to read in the binnary file format 
with open("photo.jpg", "rb") as f:
    data = f.read()

#to write in binnary file format 
with open("copy.jpg", "wb") as f:
    f.write(data)

#conut lines in a file 
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(len(lines))