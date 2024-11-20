"""Q1 Make a dictionary with keys as subject name (physics, chemistry, etc.) 
and values as their marks. Print the highest marks scored"""

from typing import Dict

dictionary: Dict[str, int] = {
    "physics": 54,
    "chemistry": 43,
    "maths": 98,
    "English": 76,
    "EVS": 142,
}


def find_highest_marks(d: Dict[str, int]) -> int:
    highest = 0

    for marks in d.values():
        if highest < marks:
            highest = marks

    return highest


result = find_highest_marks(dictionary)
print(f"The highest marks in the dictionary is {result}")
