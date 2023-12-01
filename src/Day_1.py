from utils import read_file

values = read_file(1, str, False)

final_numbers = []

for value in values:
    split = [*value]
    numbers = []
    for v in split:
        if v.isnumeric():
            numbers.append(int(v))
    if len(numbers) == 1:
        final_numbers.append(int(f'{numbers[0]}{numbers[0]}'))
    else:
        final_numbers.append(int(f'{numbers[0]}{numbers[len(numbers) - 1]}'))

print(sum(final_numbers))