"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%
Take following input from user
Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not
"""

classes_held: int = int(input("Enter the classes held = "))
classes_attended: int = int(input("Enter the classes attend = "))
attendance: float = (classes_attended / classes_held) * 100
print(f"The {attendance =}")
if attendance < 75:
    print("The student is not allowed")
else:
    print("The student is allowed")
