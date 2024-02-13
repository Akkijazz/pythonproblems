"""
Write a Python program that takes a student's score as input and
prints the corresponding grade. Use the following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
"""

student_score: int = int(input("Enter student score ="))

if student_score >= 90 and student_score <= 100:
    print("A")
elif student_score >= 80 and student_score <= 89:
    print("B")
elif student_score >= 70 and student_score <= 79:
    print("C")
elif student_score >= 60 and student_score <= 69:
    print("D")
elif student_score < 60:
    print("F")
