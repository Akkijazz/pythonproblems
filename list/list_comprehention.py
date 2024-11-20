# 10,9,8,7,6...1

a = [i**3 if i % 2 == 0 else i**2 for i in range(1, 21)]
# print(a)

original_list = [2, 3.75, 0.04, 59.354, 6, 7.7777, 8, 9]
only_int = [i for i in original_list if type(i) == int]
only_float = [i for i in original_list if type(i) == float]

# print(only_int)
# print(only_float)


# add prime from given range 1...30
def check_prime(n: int) -> bool:
    factors: int = 0
    num: int = n
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
    if factors == 2:
        return True
    else:
        return False


my_list = [i for i in range(1, 51) if check_prime(i) == True]
print(my_list)
