#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_digit = number % 10 if number >= 0 else (number % -10)

msg = "Last digit of {} is {}"
if last_digit > 5:
    print(msg.format(number, last_digit), "and is greater than 5")
elif last_digit == 0:
    print(msg.format(number, last_digit), "and is 0")
else:
    print(msg.format(number, last_digit), "and is less than 6 and not 0")
