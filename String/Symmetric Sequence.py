#STRING SYMMETRY
a = str(input("Enter the input: "))
b = len(a)
if b % 2 == 0:
    print("The given string is a symmetric sequence.")
    x= a[:b//2]
    print("First half: ",x)
    x= a[b//2:b]
    print("Second half: ",x)
else:
    print("The given string is not a symmetric sequence.")
