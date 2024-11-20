# dictionary = {
#     "name": "Akshay",
#     "gender": "male",
#     "age": 28,
#     "physics": 91,
#     "maths": 100,
#     "English": 98,
# }

# print(
#     f'Your total marks are:{dictionary["maths"] + dictionary["physics"] + dictionary["English"]}'
# )
# for k, v in dictionary.items():
#     print(f"{k}:{v}")

marks = {
    "hin": 98,
    "comp": 16,
    "science": 88,
    "physics": 98,
    "maths": 100,
    "chem": 10,
}

large = marks["hin"]
for v in marks.values():
    if v >= large:
        large = v
print(large)
