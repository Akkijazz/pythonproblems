# def printFactors(num: int) -> int:
#     i: int = 1
#     while i <= num:
#         if num % i == 0:
#             print(i, end=" ")
#         i += 1


# printFactors(14)  # 1 ,2 , 3 , 4, 6 , 12


# def countFactors(num: int) -> int:
#     i: int = 1
#     count: int = 0
#     while i <= num:
#         if num % i == 0:
#             count += 1
#         i += 1
#     print()
#     return count


# count = countFactors(12)
# print(count)


# def calculateFactorsSum(n1: int, n2: int) -> None:
#     i: int = 1
#     sum: int = 0
#     while i <= n1:
#         if i % n2 == 0:
#             sum = sum + i
#         i += 1
#     print(sum)


# calculateFactorsSum(30, 7)


# 1 11 101 1001 10001 100001
def pattern(num: int) -> None:
    i: int = 0
    while i <= num - 1:
        if i == 0:
            print(10**i, end=" ")
        else:
            print(f"{(10**i)+1}", end=" ")
        i += 1
    print()


pattern(10)
