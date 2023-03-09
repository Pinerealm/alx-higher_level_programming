#!/usr/bin/python3
import sys


def main():
    argc = len(sys.argv) - 1
    end1 = 's' if argc != 1 else ''
    end2 = ':' if argc > 0 else '.'
    print("{} argument{}{}".format(argc, end1, end2))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
