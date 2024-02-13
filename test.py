# """rock paper sissor game"""
# import random

# options = ["rock", "paper", "sissor"]
# computer_guess = random.choice(options)
# print(f"{computer_guess=}")
# user_gguess = input("Enter any one option rock/paper/sissor =")
# print(f"{user_gguess=}")
# if user_gguess.lower() == "rock" and computer_guess != "rock":
#     print("You Won")
# elif user_gguess.lower() == "sissor" and computer_guess == "paper":
#     print("You Won")
# elif user_gguess.lower() == "paper" and computer_guess != "paper":
#     print("You lose")
# elif user_gguess.lower() == "sissor" and computer_guess == "rock":
#     print("You lose")
# elif user_gguess.lower() == "rock" and computer_guess == "rock":
#     print("Tie")
# elif user_gguess.lower() == "sissor" and computer_guess == "sissor":
#     print("Tie")
# elif user_gguess.lower() == "paper" and computer_guess == "paper":
#     print("Tie")
# else:
#     print("something is wrong please try again later:")
###########################################################################################################


# def add(num1, num2, num3, num4):
#     print(num1 + num2 + num3 + num4)


# def mul(num1, num2, num3):
#     print(num1 * num2 * num3)
def add(a: int, b: int, c: int):
    print(a + b + c)


def greet(name: str, age: int, gender: str):
    print(f"my name is {name}")
    print(f"my age is {age}")
    print(f"my gender is {gender}")


if __name__ == "__main__":
    name = input("Enter name=")
    age = int(input("Enter age="))
    gender = input("Enter gender=")
    greet(name, age, gender)
