"""Ask a number from user. Print if the number is ODD or EVEN"""
num = eval(input(f"Enter number ="))
if num % 2 != 0:
    print(f"{num} is odd")
else:
    print(f"{num} is even")
