"""
Make a dictionary with keys as subject name (physics, chemistry, etc.)
and values as their marks. Print the name of the subject wiwhich has marks more than passing marks(33)
"""

from typing import Dict

dictionary: Dict[str, int] = {
    "physics": 54,
    "chemistry": 33,
    "maths": 28,
    "English": 76,
    "EVS": 142,
}

passing_marks = 33
passing_subject = ""

for subject, marks in dictionary.items():
    if marks >= passing_marks:
        print(f" You are passed in the {subject} subject with {marks} scored. ")
    else:
        print(f" You are failed in the {subject} subject with {marks} scored. ")
