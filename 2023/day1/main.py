# Open the file in read mode
import re

file_path = 'input.txt'
with open(file_path, 'r') as file:
    # Read the content of the file
    content = file.read().split('\n')
    print(type(content))

# Create a mapping from string to value
numbers = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)

import re

import re

# Create a mapping from string to value
numbers_mapping = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)


def find_and_combine_number(s):
    # Use regular expression to find all consecutive digits and spelled-out numbers in the string
    digits = re.findall(r'\d+|\b(?:' + '|'.join(numbers_mapping.keys()) + r')\b', s)

    # Combine the first and last digits or spelled-out numbers if at least one pair is found
    if digits:
        combined_str = str(digits[0]) + str(digits[-1])
        # Ensure only 2-digit numbers are considered
        if len(combined_str) == 2:
            result = int(combined_str)
            return result
    return None


def process_string_list(string_list):
    # Initialize a list to store combined numbers
    combined_numbers = []

    # Process each string in the list
    for s in string_list:
        number = find_and_combine_number(s)
        if number is not None:
            combined_numbers.append(number)

    return combined_numbers


# Example usage with a list of strings
string_list = [
    "eight47srvbfive",
    "slconeightfoureight557m38",
    "2qlljdqcbeight",
    "onetwothreefourfivesixseveneightnine"
]

combined_numbers = process_string_list(content)

# Calculate and print the sum of the combined numbers
total_sum = sum(combined_numbers)
print(f"Combined Numbers: {combined_numbers}")
print(f"Sum of Combined Numbers: {total_sum}")
