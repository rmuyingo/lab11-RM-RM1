"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Invalid base: must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Invalid argument: must be positive")
    return math.log(b, a)


def exponent(a, b):
    return a ** b
