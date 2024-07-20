# create a function countOddEven that accepts list of an integers and print how many even and odd are there
from typing import List


def countOddEven(lst: List[int]) -> int:
    evenCount: int = 0
    oddCount: int = 0
    for index in range(0, len(lst)):
        if lst[index] % 2 == 0:
            evenCount += 1
        else:
            oddCount += 1
    return evenCount, oddCount


# my_list: List[int] = [32, 45, 66, 7, 77, 89, 80, 60, 45, 18, 333]
# count1, count2 = countOddEven(my_list)
# print(f"Even:{count1}")
# print(f"Odd:{count2}")


# create a function sumCountOddEven that accepts list of an integers and print sum of even and sum of odd numbers
def sumCountOddEven(lst: List[int]) -> int:
    evenSum: int = 0
    oddSum: int = 0
    for index in range(0, len(lst)):
        if lst[index] % 2 == 0:
            evenSum += lst[index]
        else:
            oddSum += lst[index]
    return evenSum, oddSum


# my_list: List[int] = [32, 45, 66, 7, 77, 89, 80, 60, 45, 18, 333]
# evenSum, oddSum = sumCountOddEven(my_list)
# print(f"Even numbers sum : {evenSum}")
# print(f"Odd numbers sum : {oddSum}")


# create a function findsmallest that accepts list of an integers and print smallest number of list


def findsmallest(lst: List[int]) -> int:
    num: int = lst[0]
    for index in range(len(lst)):
        if lst[index] <= num:
            num = lst[index]
    return num


# my_list: List[int] = [32, 45, 66, 7, 77, 89, 80, 60, 45, 18, 333, 1]
# largeNumber: int = findsmallest(my_list)
# print(f"The smallest number is {largeNumber}")


# create a function findLargest that accepts list of an integers and print largest number of list


def findLargest(lst: List[int]) -> int:
    num: int = 0
    for index in range(len(lst)):
        if lst[index] >= num:
            num = lst[index]
    return num


# my_list: List[int] = [32, 45, 66, 7, 77, 89, 80, 60, 45, 18, 333, 1, 1, 0]
# largeNumber: int = findLargest(my_list)
# print(f"The largest number is {largeNumber}")


def calculatePrime(lst: List[int]) -> None:
    for i in range(1, len(lst)):
        factors: int = 0
        num: int = lst[i]
        for j in range(1, num + 1):
            if num % j == 0:
                factors += 1
        if factors == 2:
            print(num, end=" ")


# my_list: List[int] = [32, 45, 66, 7, 77, 89, 80, 60, 45, 18, 333, 1, 1, 0]
# calculatePrime(my_list)


s1 = "akshay"
my_dict = dict()
for i, j in enumerate(s1):
    my_dict[j] = i
    print(f"index:{i} & value:{j}")

print(f"{my_dict=}")
