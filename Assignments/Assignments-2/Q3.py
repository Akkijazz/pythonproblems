"""
Write a program to check if number is divisible by 2 and 3 but not 8
"""

number: int = int(input("Enter the number ="))

if (number % 2 == 0 and number % 3 == 0) and (number % 8 != 0):
    print(f"The {number = } is divisible by 2 and 3 but not 8")

else:
    print(f"The {number} is not matching the above condition ")
