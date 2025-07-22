class Calculator:

    def __init__(self, num1, num2): 
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        print(f"Addition is : {self.num1} + {self.num2} = {result}")

    def sub(self):
        result = self.num1 - self.num2
        print(f"Subtraction is : {self.num1} - {self.num2} = {result}")

    def multi(self):
        result = self.num1 * self.num2
        print(f"Multiplication is : {self.num1} * {self.num2} = {result}")

    def rem(self):
        result = self.num1 % self.num2
        print(f"Remainder is : {self.num1} % {self.num2} = {result}")

    def div(self):
        if self.num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = self.num1 // self.num2
        print(f"Division is : {self.num1} / {self.num2} = {result}")


def operations():
    while True:
        try:
            print("\n----------- Welcome to Simple Calculator ----------\n")
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
            cal = Calculator(num1, num2)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Remainder (%)")
        print("5. Division (/)")

        while True:

            try:
                choice = int(input("Enter your choice (1/2/3/4/5): "))
            except ValueError:
                print("\nInvalid choice! Must be an integer from 1 to 5.")
                continue

            if choice == 1:
                cal.add()
                break
            elif choice == 2:
                cal.sub()
                break
            elif choice == 3:
                cal.multi()
                break
            elif choice == 4:
                cal.rem()
                break
            elif choice == 5:
                cal.div()
                break
            else:
                print("\nInvalid choice. Please try again!")

        while True:
            again = input("\nDo you want to calculate again? (yes/no): ").lower()
            if again == 'yes' or again == 'no':
                break
            print("Invalid input. Please enter 'yes' or 'no'.")

        if again == 'no':
            print("Thanks for using Simple Calculator.")
            break


operations()
