f=open("poem.txt")


c=f.read()
if("twinkle" in c):
  print("twinkle is present in the content")
else:
    print("twinkle is not present in the content")




f.close()