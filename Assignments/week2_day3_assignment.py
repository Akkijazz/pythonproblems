"""
Q1. Create a function named div_by_3_and_5 which takes 2 integers as a
arguments (n1,n2), and print all the numbers divisible by 3 and 5 between
n1 and n2.
"""

# def div_by_3_and_5(n1: int, n2: int) -> None:
#     start = n1 if n1 < n2 else n2
#     end = n1 if n1 > n2 else n2
#     while start <= end:
#         if start % 3 == 0 and start % 5 == 0:
#             print(f"{start}", end=" ")
#         start += 1
#     print()


# div_by_3_and_5(1, 60)
# div_by_3_and_5(30, 60)
# div_by_3_and_5(60, 30)
######################################################################################################

"""Q2. Create a function named calSum() which takes 2 integers n1 and n2 as
a argument. Calculate the sum of all the numbers from n1 and n2 and
RETURN THAT SUM. Also make sure that n1 is smaller than n2. If it is not,
then return “n1 should be smaller”."""


# def calSum(n1: int, n2: int) -> int:
#     start, end = n1, n2
#     if start < end:
#         sum: int = 0
#         while start <= end:
#             sum += start
#             start += 1
#         return sum
#     else:
#         return "n1 should be smaller"


# sum = calSum(1, 120)
# print(f"{sum}")
# sum = calSum(30, 10)
# print(f"{sum}")

######################################################################################################
"""Q3. Create a function named multiplicationTable that takes an integer
num as an argument. Print the multiplication table of that number up to 10
numbers."""


# def multiplicationTable(num: int = 1) -> None:
#     i: int = 1
#     while i <= 10:
#         print(f"{num} X {i} = {num*i}")
#         i += 1
#     print()


# multiplicationTable(231)
# multiplicationTable()

######################################################################################################
"""
Q4. Create a function named calSum which takes an 2 integer (n1 and n2)
as an argument. Calculate the sum of all the numbers divisible by 5
between n1 and n2 and return that sum. (Make sure that n1 is less than n2).
"""


# def calSum(n1: int, n2: int) -> int:
#     if n1 < n2:
#         start = n1
#         sum = 0
#         while start <= n2:
#             if start % 5 == 0:
#                 sum += start
#             start += 1
#         return sum
#     else:
#         return f"n1 should be smaller than n2"


# ans = calSum(43, 68)
# print(f"{ans}")


"""
Q5. Create a function named printPattern that takes one integer (num) as
an argument. Print from -num to num. Also keep in mind number passed as
an argument can be negative or positive.
"""


def printPattern(num: int) -> None:
    start = -num if num > 0 else num
    end = num if num > 0 else -num
    while start <= end:
        print(start, end=" ")
        start += 1


printPattern(-9)
