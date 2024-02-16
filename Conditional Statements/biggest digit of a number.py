n = 7865
largest_digit = 0
for digit in str(n):# i in place of digit
  digit = int(digit)
  if(digit > largest_digit):
   largest_digit = digit
print("The biggest digit is: ",largest_digit)

