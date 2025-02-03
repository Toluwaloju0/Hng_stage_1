#!/usr/bin/env python3
""" A module to get the sum of the digits of a num"""

def digit_sum(num):
    """A function to sum the digits in a num"""

    sum = 0
    while num > 0:
        sum += (num % 10)
        num = num // 10

    return sum