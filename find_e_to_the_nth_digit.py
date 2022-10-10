"""
Find e(Euler's number) to the Nth Digit -
Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.
"""
# The decimal module provides support for fast correctly rounded decimal floating point arithmetic
from decimal import Decimal, getcontext
from math import factorial


def find_e():
    """
    Function to find e.
    Limit of precition set to 1001.
    For loop with range 1000 will give more accurate result of e
    """
    getcontext().prec = 1001
    num_e = 0
    for k in range(1000):
        num_e += (1 / Decimal(factorial(k)))
    return num_e


def nth_digit():
    """
    Function to ask for non-negative integer as nth digit,
    which greater then 0 and within limit 1000.
    """
    while True:
        try:
            decim_places = int(input("""
            \rGet result of Euler's number up to that many decimal places. Limit is 1000.
            \rPlease enter a non-negative integer number.
            \rHow many decimal places? : """))
            if 0 < decim_places <= 1000:
                return decim_places
            print(
                "\nError.More than limit or non-negative integer numbers greater then 0")
            continue
        except ValueError:
            print("\nError. Please use nonnegative integer numbers")
            continue


# Data type of find_e function will convert into string.
# Slicing will help to get as many decimal places as asked in nth_digit function.
# First two symbols will always print.

PROGRESS = "y"
while PROGRESS == "y":
    print(str(find_e())[:(nth_digit() + 2)])
    while True:
        PROGRESS = input("\nContinue? y/n ")
        if PROGRESS.lower() == "n" or PROGRESS.lower() == "y":
            break
        print("\nError. Please use letters 'y' for yes and 'n' for no")
