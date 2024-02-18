"""
Enter a number = 10
Enter a number = 7
Enter a number = 5
Enter a number = 0

total = 22
"""


def calSum() -> None:
    total: int = 0
    while True:
        num: int = int(input(f"Enter a number="))
        total += num
        if num == 0:
            break

    print(f"Total={total}")


calSum()
