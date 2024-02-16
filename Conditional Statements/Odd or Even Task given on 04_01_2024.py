n = int(input("Enter the value of: "))
if(n%2 == 0):
  print("Even")
  if(n>=2 and n<=5):
    print("Not Weird")
  elif(n>=6 and n<=20):
    print("Weird")
  else:
    print("Not Weird")
else:
  print("Odd")
