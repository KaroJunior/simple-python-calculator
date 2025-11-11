"""
SIMPLE PYTHON CALCULATOR
A basic calculator that performs arithmetic operations.
"""

def calculator():
    print("=== KARO JUNIOR SIMPLE PYTHON CALCULATOR ===")
    
    try:
        number_1 = float(input("Enter first number: "))
        number_2 = float(input("Enter second number: "))
        sign = input("Enter operation (+, -, *, /): ").strip()
        
        if sign == "+":
            result = number_1 + number_2
        elif sign == "-":
            result = number_1 - number_2
        elif sign == "*":
            result = number_1 * number_2
        elif sign == "/":
            if number_2 == 0:
                print("Error: Cannot divide by zero!")
                return
            result = number_1 / number_2
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
            return
        
        print(f"Result: {number_1} {sign} {number_2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()
