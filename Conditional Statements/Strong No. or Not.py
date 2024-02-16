# STRONG No. OR NOT

n = int(input("Enter the input: "))
temp = n
sum =0
while(n>0):
    digit = n % 10

    fact = 1
    for i in range(1, digit + 1):
       fact *= i

    sum += fact

    n //= 10

print(sum)

if( temp == sum ):
  print("The given no. is a strong number.")
  
else:
  print("The given no. is not a strong number.")
