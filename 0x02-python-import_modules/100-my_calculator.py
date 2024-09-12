#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    ops = {'+': add, '-': sub, '*': mul, '/': div}

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {} {:d} = {:d}".format(a, operator, b, ops[operator](a, b)))
