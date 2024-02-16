# factors of a number using for loop
n = int(input("Enter the input: "))
for i in range(1,n+1):
  if n % i == 0:
   print(i)
