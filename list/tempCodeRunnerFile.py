for i in range(0, len(a)):
    sub = a[i : i + b]
    print(sub, end=" ")
    if len(sub) == 3 and sum(sub) == c:
        print("True")
    else:
        print("Flase")