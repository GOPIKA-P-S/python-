AB = float(input("Enter the length of side AB: "))
BC = float(input("Enter the length of side BC: "))
AC = float(input("Enter the length of side AC: "))
if(AC == ((AB**2) + (BC**2))**(0.5)):
  print("The given triangle is a right-angled triangle.")
else:
  print("The given triangle is not a right-angled triangle.")
