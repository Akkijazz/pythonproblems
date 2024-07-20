# Create a class where the object represents a bag with beans. There are two types of beans, green and blue. A bag contains beans of only one color. Add a method for updating the object by removing a random number of beans: between 10 and 30 for green beans and between 20 and 40 for blue beans.
# Create an array of bags, where 100 bags contain green beans and 150, blue beans. The number of beans in each bag is a random number: between 1000 and 3000 for green beans, and between 2000 and 4000 for blue beans.
# Run 80 iterations, where on each iteration all elements of the array are updated once.
# After all those iterations are finished, remove array elements (i.e., bags) that contain less than 50 beans. Count the removed bags and beans in them, keeping separate counts for green and blue beans, Print those counts. Save information about the other bags in a text file named “bean_bags.txt”.
# Use a lambda function when convenient; at least once.
# Write as much code as you can in 20 minutes.
from typing import List

# from random import randint
import random


class Bag:

    def add_beans(beans: List, colur: str) -> None:
        green_beans: List = 0
        blue_beans: List = 0
        if not beans:
            if colur.lower() == "green":
                green_beans.append(beans)
                print(f"green beans are added")
            if colur.lower() == "blue":
                green_beans.append(beans)
                print(f"blue beans are added")

    def update_count(num: int, colur: str) -> None:
        if colur.lower() == "green" and num >= 10 or num <= 30:
            print(f"green beans are updated")

        elif colur.lower() == "blue" and num >= 20 or num <= 40:
            print(f"blue beans are updated")

    def remove_beans(bean: int, colur: str) -> None:
        if not bean:
            if colur.lower() == "green":
                print(f"green beans are removed")
            if colur.lower() == "blue":
                print(f"blue beans are removed")

    def create_bags(bags: int, num: int) -> List[int]:
        lst_blue_bag = []

        print(f"bag is created and having {num} of beans")


green_bag = [i for i in range(random.randint(1000, 3000)) if i > 1000 and i < 3000]
# print(f"{green_bag =}")
blue_bag = [i for i in range(random.randint(2000, 4000)) if i > 2000 and i < 4000]
sample_bag = Bag()
sample_bag.add_beans(green_bag, "green")
sample_bag.add_beans(blue_bag, "blue")
