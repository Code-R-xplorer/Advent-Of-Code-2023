import re

from utils import read_file

values = read_file(1, str, False)

final_numbers_part_1 = []
final_numbers_part_2 = []

for value in values:
    # Splits the line into individual characters
    split = [*value]
    numbers = []
    for v in split:
        # Only grab integers and not the random text
        if v.isnumeric():
            numbers.append(int(v))
    # If a line only contains one number then the number is duplicated
    if len(numbers) == 1:
        final_numbers_part_1.append(int(f'{numbers[0]}{numbers[0]}'))
    # Get the first and last number to create the final number
    else:
        final_numbers_part_1.append(int(f'{numbers[0]}{numbers[len(numbers) - 1]}'))

# Part 1 54667
print(sum(final_numbers_part_1))


text_to_number = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }


for value in values:
    # Regular Expression to find all the numbers in the line in a worded format i.e one = 1
    matches = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', value)
    numbers = []
    for match in matches:
        if match.isdigit():
            # If multiple numbers are together split them into single digits
            if len(match) > 1:
                ms = [*match]
                for m in ms:
                    numbers.append(int(m))
            else:
                numbers.append(int(match))
        else:
            numbers.append(text_to_number[match])
    # Same as part 1
    if len(numbers) == 1:
        final_numbers_part_2.append(int(f'{numbers[0]}{numbers[0]}'))
    else:
        final_numbers_part_2.append(int(f'{numbers[0]}{numbers[len(numbers) - 1]}'))

# Part 2 54203
print(sum(final_numbers_part_2))
