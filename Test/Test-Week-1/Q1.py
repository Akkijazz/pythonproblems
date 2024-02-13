"""
Q1. Write a program to print absolute vlaue of a number entered by user.
Example 1
Input = -18
Output = 18
Example 2
Input = 9
Output = 9
"""
import math

number: int = int(input("Enter any number ="))
abs_number = int(math.fabs(number))
print(f"{abs_number=}")
