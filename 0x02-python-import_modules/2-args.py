#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    argc = len(argv[1:])
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argc))

    for index in range(argc):
        print("{:d}: {}".format(index + 1, argv[index + 1]))
