try:
  a=int(input("Hey,Enter a number:"))
  print(a)

except ValueError as v:
  print("Enter only number")
  

else:
  print("I am inside else")
  
