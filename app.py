def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2


if __name__ == "__main__":
    print("Hello from jenkins")
    print("Addition: ", add(10, 5)) 
    print("Subtraction: ", subtract(10, 5))
    print("Multiplication: ", multiply(10, 5))
    print("Division: ", divide(10, 5))