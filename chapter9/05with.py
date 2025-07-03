f=open("file.txt")
print(f.read())

f.close()

# the same can be written using with statement 

with open("file.txt") as f:
  print(f.read())



# you don't have to explictely close the file
  



