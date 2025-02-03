#!/usr/bin/env python3
"""A module to check if a number is prime"""

def is_prime(num):
    """The function to check for prime number"""

    for a in range(2, num // 2):
        if num % a == 0:
            return False
    return True