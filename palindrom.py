def find_palindromes(number):
    number_str = str(number)
    palindromes = []
    for i in range(len(number_str)):
        for j in range(i + 1, len(number_str) + 1):
            substring = number_str[i:j]
            if substring == substring[::-1] and len(substring) > 1:
                palindromes.append(int(substring))
    return palindromes


# Example usage:
input_number = 1234567890  # Replace this with any 10-digit number
result = find_palindromes(input_number)
print("Input number:", input_number)
if result:
    print("List of palindromes:", result)
else:
    print("No palindromes found.")
