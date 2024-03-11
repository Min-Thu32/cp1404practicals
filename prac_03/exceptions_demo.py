"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    ValueError will occur when the user input string and decimal value.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError occurs when user input 0 for denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, the possibility of a ZeroDivisionError can be avoided by adding a check
    so that the denominator is not zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Denominator cannot be zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")