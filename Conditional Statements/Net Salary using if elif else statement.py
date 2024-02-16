Basic_Sal = float(input("Enter the basic salary of an individual: "))
percent_of_Allownce = float(input("Enter the percentage of allowance in the salary of an individual: "))
percent_of_Deductns = float(input("Enter the percentage of deductions in the salary of an individual: "))
Net_Sal = Basic_Sal + (Basic_Sal * percent_of_Allownce/100) - (Basic_Sal * percent_of_Deductns/100)
print("The Net Salary of an individual: ",Net_Sal)
if(percent_of_Allownce > percent_of_Deductns):
  print("The Net Salary will be greater than that of Basic Salary.")
elif(percent_of_Allownce == percent_of_Deductns):
    print("The Net Salary will be same as that of Basic Salary.")
else:
    print("The Net Salary will be lower than that of Basic Salary.")
