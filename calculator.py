"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
user_input = input("Enter your equation>")
token= user_input.split(" ")
operator = token[0]

if operator == 'q':
    quit
else:
    num1 = token[1]

    if operator == 'square':
        result = square(float(num1))

    elif operator == 'cube':
        result = cube(float(num1))

    else:
        num2 = token[2]
        if operator == '+':
            result = add(float(num1),float(num2)) 

        elif operator== '-':
            result = subtract(float(num1),float(num2))

        elif operator == '*':
            result = multiply(float(num1), float(num2))
            
        elif operator == '/':
            result = divide(float(num1), float(num2))

        elif operator == 'pow':
            result = pow(float(num1), float(num2))

        elif operator == 'mod':
            result = mod(float(num1), float(num2))
    print(result)