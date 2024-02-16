n = int(input("Enter the input: "))
sum = 0
for i in range(1,n):
  if n % i == 0:
   sum  = sum + i
if(sum == n):
  print("The given integer is a perfect number.")
else:
  print("The given integer is not a perfect number.")
