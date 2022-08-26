#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def exec_calc(operator, a, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return sub(a, b)
    elif operator == '*':
        return mul(a, b)
    elif operator == '/':
        return div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    result = exec_calc(operator, a, b)
    print('{} {} {} = {}'.format(a, operator, b, result))


if __name__ == "__main__":
    main()
