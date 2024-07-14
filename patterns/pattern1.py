# start = int(input("Enter nums:"))
# end = int(input("Enter nums:"))
# sum = 0
# for i in range(20, 51):
#     if i % 4 == 0:
#         # print(i, end=" ")
#         sum += i
# print(f"sum:{sum}")


def pattern(n):
    for i in range(1, n + 1):
        for _ in range(1, i + 1):
            print(_ - 1, end=" ")
        print()


pattern(9)
