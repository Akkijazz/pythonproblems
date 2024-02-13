"""
Q5. Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
Example 1
Enter bill amount = 80000
You got 30% discount
Your final bill is Rs. 56000"""

amount: int = int(input("Enter the amount ="))
final_amount: float = 0.0
if amount >= 50000:
    print("The discount you get is 30 %")
    final_amount = amount - (amount * 0.3)
    print(f"The final amount after the discount is {final_amount: .2f}")
elif amount >= 40000 or amount <= 4999:
    print("The discount you get is 25 %")
    final_amount = amount - (amount * 0.25)
    print(f"The final amount after the discount is {final_amount: .2f}")
elif amount >= 30000 or amount <= 39999:
    print("The discount you get is 20 %")
    final_amount = amount - (amount * 0.2)
    print(f"The final amount after the discount is {final_amount: .2f}")
elif amount >= 10000 or amount <= 29999:
    print("The discount you get is 10 %")
    final_amount = amount - (amount * 0.1)
    print(f"The final amount after the discount is {final_amount: .2f}")
elif amount >= 1 or amount <= 9999:
    print("Sorry no discount")
    final_amount = amount
    print(f"The final amount is {final_amount: .2f}")
else:
    print(f"Please continue the shopping")
