choice = input("Enter choice (+,-,*,/,%,**,//): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '+':
    print("Result:", num1 + num2)
elif choice == '-':
    print("Result:", num1 - num2)
elif choice == '*':
    print("Result:", num1 * num2)
elif choice == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
elif choice == '%':
    if num2 != 0:
        print("Result:", num1 % num2)
    else:
        print("Error! Modulus by zero is not allowed.")
elif choice == '**':
    print("Result:", num1 ** num2)
elif choice == '//':
    if num2 != 0:
        print("Result:", num1 // num2)
    else:
        print("Error! Floor division by zero is not allowed.")
else:
    print("Invalid choice!")