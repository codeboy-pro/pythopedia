with open("lorem.txt") as f:
  content1=f.read()

with open("lorem_copy.txt") as f:
  content2=f.read()

if(content1==content2):
  print("Yes these files are identical")

else:
  print("no , these two files arenot identical")
  