"""
Q1. Create a class called Employee with attributes such as name, age,
gender, and phone number. Implement a constructor to initialize these
attributes.
Include methods to calculate monthly and yearly salary based on hourly
rate and hours worked. Ask hourly rate and hours worked inside the
method (local variable).
Create 2 objects and check your code.
"""


class Employee:
    def __init__(self) -> None:
        self.name: str = input("Enter  name =")
        self.age: int = int(input("Enter age ="))
        self.gender: str = input("Enter gender =")
        while True:
            phone_number: int = input("Enter phone number =")
            if len(int(phone_number)) == 10:
                self.phone_number = phone_number
                break

    def calculate_monthly_salary(self) -> int:
        hours: int = int(input("Enter hours="))
        hour_rate: int = int(input("Enter hours rate ="))
        salary: int = hour_rate * hours
        return salary
