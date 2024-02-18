"""
Q1. Create a function named factorial which takes a integer as an input and
returns the factorial of that number.
Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120
"""

# def fact(num: int) -> int:
#     if num == 0 or num == 1:
#         return 1
#     else:
#         i: int = 1
#         fact: int = 1
#         while i <= num:
#             fact *= i
#             i += 1
#         return fact


# fact1 = fact(0)
# print(fact1)


"""
Q2. Create a function named pattern which takes an integer as an input
and print the following pattern.
pattern(4)
output -> 10 20 30 40
pattern(11)
output -> 10 20 30 40 50 60 70 80 90 100 110
"""


# def pattern(num: int) -> None:
#     i: int = 1
#     while i <= num:
#         print(i * 10, end=" ")
#         i += 1
#     print()


# pattern(4)
# pattern(11)

"""Q3. Create a function named pattern which takes an integer as an input
and print the following pattern.
pattern(4)
output -> 1 2 4 8
pattern(7)
output -> 1 2 4 8 16 32 64
"""


# def patttern(num: int) -> None:
#     i: int = 0
#     while i <= num - 1:
#         print(2**i, end=" ")
#         i += 1
#     print()


# patttern(4)
# patttern(7)

"""
Q4. Don’t create a function, just print the following pattern
1 11 111 1111 11111....n times (Ask n from user)
"""
# n = int(input("Enter number = "))
# i: int = 1
# num: int = 1
# while i <= n:
#     print(num, end=" ")
#     num = (num * 10) + 1
#     i += 1


"""
Q5. Keep asking numbers from user until the user enters 0. Then display
the average of all numbers.
"""


# def avg() -> int:
#     total: int = 0
#     count: int = 0
#     while True:
#         num: int = int(input("Enter a number="))
#         if num == 0:
#             break
#         else:
#             count += 1
#             total += num
#     avg = total / count
#     return avg


# a = avg()
# print(a)

"""
Q6. Write a function named pattern which accepts an integer n as an
argument. Then print the following pattern.
pattern(4)
output -> 1 4 9 16
pattern(10)
output -> 1 4 9 16 25 36 49 64 81 100
"""


def pattern(num: int) -> None:
    i: int = 1
    while i <= num:
        print(i * i, end=" ")
        i += 1
    print()


pattern(4)
pattern(10)
