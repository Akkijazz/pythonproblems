"""
Write a Python function to find the Maximum and minimum of three
numbers. Use 3 parameters. Make 2 different functions named as maxi and
mini.
"""


def maxi(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print(f"The number {num1} is greater")
    elif num2 >= num3:
        print(f"The number {num2} is grater")
    else:
        print(f"The number {num3} is greater")


def mini(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        print(f"The number {num1} is smaller")
    elif num2 <= num3:
        print(f"The number {num2} is smaller")
    else:
        print(f"The number {num3} is smaller")


if __name__ == "__main__":
    first_number: int = int(input("Enter 1st number = "))
    secomd_number: int = int(input("Enter 2nd number = "))
    third_number: int = int(input("Enter 3rd number = "))
    maxi(first_number, secomd_number, third_number)
    mini(first_number, secomd_number, third_number)
