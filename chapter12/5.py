a=int(input("Enter 1st number:"))
b=int(input("Enter the 2nd number:"))

if(b==0):
  raise ZeroDivisionError("Hey our programme is not meant to devide by zero")



print(f"The division by {a}/{b} is {a/b}")