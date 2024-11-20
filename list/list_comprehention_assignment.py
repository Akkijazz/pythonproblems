# 1.write a python program to genrate a list of powers 2 less than 100 using list comprehension.
from math import sqrt


def power_list(i: int) -> bool:
    if i**2 < 1000:
        return True


my_list = [i**2 for i in range(1, int(sqrt(1000) + 1)) if power_list(i)]

# print(my_list)


def factorial(n: int) -> int:
    if n == 0:
        return 1
    fact: int = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


my_list = [factorial(i) for i in range(1, 11) if factorial(i) < 1000]
# print(my_list)


from typing import List


def sumOfDigits(n: int) -> int:
    total = 0
    while n > 0:
        last_digit = n % 10
        total = total + last_digit
        n = n // 10
    return total


def generateList(num: int) -> List[int]:
    return [i for i in range(1, num + 1) if i % sumOfDigits(i) == 0]


x = generateList(500)
print(x)


# for i in range(4):
#     print(f"{i=}", end=" ")


def calculate_time(l1: List[int]) -> int:
    max_val: int = max(l1)
    time_val: int = 0
    for i in range(len(l1)):
        if l1[i] < max_val:
            diff: int = max_val - l1[i]
            time_val += diff
    return time_val


my_list: List[int] = [1, 2, 3, 4]
res = calculate_time(my_list)
print(f"{res=}")


numbers = range(10)
complex_dict = {n: ("even" if n % 2 == 0 else "odd") for n in numbers}
print(
    complex_dict
)  # Output: {0: 'even', 1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd'}


a = [4, 3, 2, 6]
b = 3
c = 11
sub = []
for i in range(0, len(a)):
    sub = a[i : i + b]
    print(sub, end=" ")
    if len(sub) == 3 and sum(sub) == c:
        print("True")
    else:
        print("Flase")


class Test:
    a = 10

    def __init__(self):
        Test.b = 20

    def m1(self):
        Test.c = 30

    @classmethod
    def m2(cls):
        cls.d1 = 40
        Test.d2 = 400

    @staticmethod
    def m3():
        Test.e = 50
