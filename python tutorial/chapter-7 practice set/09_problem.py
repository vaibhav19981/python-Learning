n = int(input("Enter a number:"))

print("*"*(n))

for i in range(n-2):
  print("*"+" "*(n-2)+"*")
  
if n>1:
  print("*"*(n))