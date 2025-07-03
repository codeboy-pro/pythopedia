try:
  a=int(input("Hey,Enter a number:"))
  print(a)

except ValueError as v:
  print("Enter only number")
  

except Exception as e:
  print(e)




print("Thank you")
