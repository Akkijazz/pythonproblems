"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject with highest marks scored.
"""

from typing import Dict

dictionary: Dict[str, int] = {
    "physics": 54,
    "chemistry": 43,
    "maths": 98,
    "English": 76,
    "EVS": 142,
}
highest_marks = 0
highest_subject = ""

for subject, marks in dictionary.items():
    if highest_marks < marks:
        highest_marks = marks
        highest_subject = subject

print(f"Highest marks scored is {highest_marks} in {highest_subject} subject")
