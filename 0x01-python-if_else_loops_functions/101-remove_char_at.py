#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    for i in range(len(str)):
        if i == n:
            str = str[:i] + str[i+1:]
    return str
