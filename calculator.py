"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


# Replace this with your code


while True:
    user_input = input("Enter your equation>")
    token= user_input.split(" ")
    operator = token[0]
   
    if operator == 'q':
        print("You will exit.")
        break

    elif len(token) < 2:
        print("You have not given enough inputs. Try again")
        continue

    num1 = token[1]

    if len(token) < 3:
        num2 = "0"

    else:
        num2 = token[2]
    
    result = None

    if not num1.isdigit() or not num2.isdigit():
        print("These are not numbers. Try again.")
        continue

    elif operator == '+':
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
    elif operator == 'square':
            result = square(float(num1))

    elif operator == 'cube':
            result = cube(float(num1))
    print(result)