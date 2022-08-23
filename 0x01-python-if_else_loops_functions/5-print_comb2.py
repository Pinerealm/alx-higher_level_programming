#!/usr/bin/python3
for i in range(100):
    delimiter = ", " if i < 99 else "\n"
    if i < 10:
        print('{}'.format(0), end="")
    print('{}'.format(i), end=delimiter)
