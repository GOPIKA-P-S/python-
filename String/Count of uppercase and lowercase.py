#COUNT OF UPPER AND LOWER CASE LETTERS
a = str(input("Enter the input: "))
U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
L = "abcdefghijklmnopqrstuvwxyz"
j = 0
for i in range(0,len(a)):
    if(a[i] == U[j]):
      x = len(a[i])
      x += 1
    el:
      y = len(a[i].lower())
      y += 1
print(x)
print(y)
