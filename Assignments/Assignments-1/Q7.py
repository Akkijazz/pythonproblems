"""Check if the number entered by User is divisible by 3 or not"""

num = eval(input("Enter number ="))
if num % 3 == 0:
    print(f"{num} is divisible by 3")
else:
    print(f"{num} is not devisible by 3")
