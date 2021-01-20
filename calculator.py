"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
user_input = input(">")
tokens = user_input.split(" ")

if tokens[0]== 'pow':
    answer = float(tokens[1]) ** float(tokens[2])
    print(answer)
print(tokens)