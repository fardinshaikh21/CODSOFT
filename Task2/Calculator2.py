
try:
    print("\n----------- Welcome to Simple Calculator ----------\n")
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
except ValueError:
    print("Invalid input! Please enter numeric values.")


print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Remainder (%)")
print("5. Division (/)")


try:
    choice = int(input("Enter your choice (1/2/3/4/5): "))
except ValueError:
    print("\nInvalid choice! Must be an integer from 1 to 5.")
    
if choice == 1:
    print(f"Addition is {num1} + {num2} = ",num1+num2)     
elif choice == 2:
    print(f"Subtraction is {num1} - {num2} = ",num1-num2)  
elif choice == 3:
    print(f"Multiplication is {num1} * {num2} = ",num1*num2) 
elif choice == 4:
    print(f"Remainder is {num1} % {num2} = ",num1%num2) 
elif choice == 5:
    print(f"Division is {num1} / {num2} = ",num1/num2)             
else:
  print("\nInvalid choice. Please try again!")    
  