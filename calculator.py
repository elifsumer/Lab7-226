import math_utils


def main():
    try:
        x = float(input("Enter a number: "))
        y = float(input("Enter a number: "))
        op = input("Select the operation (+, -, *, /, **, %): ")

        operations = {
            '+': math_utils.add,
            '-': math_utils.subtract,
            '*': math_utils.multiply,
            '/': math_utils.divide,
            '**': math_utils.power,
            '%': math_utils.mod
        }

        if op in operations:
            result = operations[op](x, y)
            print("Result:", result)
        else:
            print("Invalid entry.")

    except ValueError:
        print("Please enter a invalid number.")

if __name__ == "__main__":
    main()
