class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def eat(self, eat) -> None:
        print(f"{self.name} is eating :{self.eat}")


class dog(Animal):
    def fetch(self, thing) -> None:
        self.thing = thing
        print(f"{self.name} goes after {self.thing}")


# d = dog("Ranger")
# d.fetch("ball")
# Create a class where the object represents a bag with beans. There are two types of beans, green and blue. A bag contains beans of only one color. Add a method for updating the object by removing a random number of beans: between 10 and 30 for green beans and between 20 and 40 for blue beans.
# Create an array of bags, where 100 bags contain green beans and 150, blue beans. The number of beans in each bag is a random number: between 1000 and 3000 for green beans, and between 2000 and 4000 for blue beans.
# Run 80 iterations, where on each iteration all elements of the array are updated once.
# After all those iterations are finished, remove array elements (i.e., bags) that contain less than 50 beans. Count the removed bags and beans in them, keeping separate counts for green and blue beans, Print those counts. Save information about the other bags in a text file named “bean_bags.txt”.
# Use a lambda function when convenient; at least once.
# Write as much code as you can in 20 minutes.

import random


class BeanBag:
    def __init__(self, color, initial_beans):
        self.color = color
        self.beans = initial_beans

    def update_beans(self):
        if self.color == "green":
            beans_removed = random.randint(10, 30)
        elif self.color == "blue":
            beans_removed = random.randint(20, 40)
        self.beans -= beans_removed
        self.beans = max(self.beans, 0)  # Ensure beans do not go below 0


# Initialize bags
bags = [BeanBag("green", random.randint(1000, 3000)) for _ in range(100)] + [
    BeanBag("blue", random.randint(2000, 4000)) for _ in range(150)
]
# print(f"{bags =}")
# Run 80 iterations
for _ in range(80):
    for bag in bags:
        bag.update_beans()

# Separate bags with less than 50 beans
removed_green_bags = 0
removed_blue_bags = 0
removed_green_beans = 0
removed_blue_beans = 0

remaining_bags = []

for bag in bags:
    if bag.beans < 50:
        if bag.color == "green":
            removed_green_bags += 1
            removed_green_beans += bag.beans
        elif bag.color == "blue":
            removed_blue_bags += 1
            removed_blue_beans += bag.beans
    else:
        remaining_bags.append(bag)

# Print counts
print(f"Removed green bags: {removed_green_bags}, beans in them: {removed_green_beans}")
print(f"Removed blue bags: {removed_blue_bags}, beans in them: {removed_blue_beans}")

# Save information about the remaining bags to a file
with open("bean_bags.txt", "w") as file:
    for bag in remaining_bags:
        file.write(f"Color: {bag.color}, Beans: {bag.beans}\n")
