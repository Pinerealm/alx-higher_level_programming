#!/usr/bin/python3
import sys


def main():
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
    print(result)


if __name__ == "__main__":
    main()
