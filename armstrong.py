#/usr/bin/env python3
"""A module to check if a number is an armstrong number"""

def armstrong(num):
    """Afunction to check if a number is an armstrong number"""

    sum = 0
    count = len(str(num))
    temp = num
    while temp > 0:
        a = temp % 10
        sum += a ** count
        temp = temp // 10
    return sum == num

def is_even(num):
    """To check if a number is even or odd"""

    if num % 2 == 0:
        return True
    return False