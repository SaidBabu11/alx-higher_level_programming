#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))


if __name__ == "__main__":
    main()


def submain():
    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, sub(a, b)))
