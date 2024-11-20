# Q1 make your own list and also make 2 lists empty and separate the odd and even elementsfrom original list
from typing import List

even_list: List[int] = []
odd_list: List[int] = []


def even_odd_lists(lst: List[int]) -> None:
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)


# original_list: List[int] = [12, 33, 44, 34343, 4556, 77, 7878, 89, 90, 123, 45, 678]
# even_odd_lists(original_list)

# print(even_list)
# print(odd_list)


# Q2 write a function to remove duplicates from list and print them.

duplicates_list: List[int] = []


def remove_duplicates_from_list(lst: List[int]) -> None:
    for i in lst:
        if lst.count(i) > 0:
            if i not in duplicates_list:
                duplicates_list.append(i)
    print(f"{duplicates_list=}")


# original_list: List[int] = [12, 12, 33, 44, 34343, 4556, 77, 7878, 89, 1, 1, 2, 2, 5, 5]
# remove_duplicates_from_list(original_list)
# print(f"{original_list=}")


# Q3 Write a function that takes 2 lists and returns true if that have atleast 1 common element
lst1: List[int] = [34, 11, 91, 59, 33, 22]
lst2: List[int] = [78, 14, 23, 22]


def find_common_element(l1: List[int], l2: List[int]) -> bool:
    for i in range(0, len(l2)):
        if l2[i] in l1:
            return True
    return False


# x = find_common_element(lst1, lst2)
# print(x)

# Q4 write a python program to find sum and average of List in python


def sum_avg_list(lst: List[int]) -> None:
    sum_of_elements: int = 0
    for i in lst:
        sum_of_elements += i
    print(f"sum:{sum_of_elements=}")
    print(f"avg:{sum_of_elements/len(lst)}")


# original_list: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum_avg_list(original_list)


lst1: List[int] = [34, 11, 91, 59, 33, 22]
lst2: List[int] = [78, 14, 23, 22]


def find_common_element(l1: List[int], l2: List[int]) -> List:
    for i in range(0, len(l2)):
        if l2[i] in l1:
            return True
    return False


# Q6 write a program to remove nth element from a list


def remove_nth_element_list(lst: List[int], index: int) -> None:
    try:
        lst.pop(index)
    except IndexError:
        print(f"index does not exists")


# original_list: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# remove_nth_element_list(original_list, 3)
# print(original_list)

sum_list: List[int] = []


def addition(l1: List[int], l2: List[int]) -> List[int]:
    for i in range(0, len(l1)):
        sum_list.append(l1[i] + l2[i])
    return sum_list


lst1: List[int] = [10, 25, 30, -10, 1, 9]
lst2: List[int] = [58, 11, -15, 20, 6, 1]

x: List[int] = addition(lst1, lst2)
print(x)
