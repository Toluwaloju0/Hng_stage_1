#!/usr/bin/env python3
"""A modue to check if a number is a perfect number"""

def is_perfect(num):
    """A function to check if a number is a perfect number"""

    sum = 0
    for a in range(1, (num // 2) + 1):
        if num % a == 0:
            sum += a
    return sum == num
