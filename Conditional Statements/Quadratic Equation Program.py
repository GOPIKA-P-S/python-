a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))
'''x = ((-b) +- (D))/2 *a
    a(x**2) + b(x) + c = 0'''
D = ((b**2)-(4 *a * c))**(0.5)
if(D>0):
  Root1 = (-b + D)/ 2* a
  Root2 = (-b - D)/ 2* a
  print("The equation will have two real Roots:- Root1 = ",Root1,"and Root2 = ",Root2)
elif(D == 0):
  Root1 = Root2 = (-b)/2 * a
  print("The equation will have one real Root:- Root1 = Root 2 = ",Root1)
else:
    print("The Roots are imaginary.")
