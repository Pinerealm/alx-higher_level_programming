#!/usr/bin/python3
def uppercase(str):
    for c in str:
        islower = ord(c) >= ord('a') and ord(c) <= ord('z')
        c = chr(ord(c) - 32 if islower else ord(c))
        print(c, end='')
    print('{}'.format('\n'), end='')
