# PRIME No. OR NOT
n = int(input("Enter the input: "))
for i in range(2,n):
  if n % i == 0:
   print("The given no. is not a prime number.")
   break
  else:
    print("The given no. is a prime number.")
