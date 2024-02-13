"""
Ask a number from user.
Print YES - if it is divisible by 5 and 6
NO
"""

number: int = int(input("Enter number ="))
if number % 5 == 0 and number % 6 == 0:
    print(f"yes")
else:
    print(f"no")
