
def SimpleCalculator(num1, num2, operation):
    if operation == '+' :
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Error")
        return 0

print("Enter operator:")
operation = input()
result = SimpleCalculator(10 ,5, operation)
print(result)
