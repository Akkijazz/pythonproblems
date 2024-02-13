"""Write a program that takes two numbers as input and checks if the first number is divisible by the second"""
first_number: int = int(input("Enter first number = "))
second_number: int = int(input("Enter second number = "))

if first_number % second_number == 0:
    print(f"The {first_number} is divisble by {second_number}")

else:
    print(f"The {first_number} is not divisble by {second_number}")
