n=int(input("Enter the num:"))


for i in range(2,n):
  if(n%i==0):
    print("no is not prime")
    
    break

else:
  print("no is prime")
  