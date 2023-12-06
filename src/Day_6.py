from utils import read_file

lines = read_file(6, str, False)

# Time
line = lines[0]
_, values_string = line.split(':')
values_string = values_string.strip()
values = values_string.split(' ')
values = filter(None, values)
times = [int(i) for i in values]

# Distance
line = lines[1]
_, values_string = line.split(':')
values_string = values_string.strip()
values = values_string.split(' ')
values = filter(None, values)
distances = [int(i) for i in values]

beat_record_totals = []

for i in range(len(times)):
    beaten_record = 0
    for j in range(times[i] + 1):
        time_left = times[i] - j
        distance_covered = time_left * j
        if distance_covered > distances[i]:
            beaten_record += 1
    beat_record_totals.append(beaten_record)


def multiply_list(_list):
    # Multiply elements one by one
    result = 1
    for x in _list:
        result = result * x
    return result

# Part 1 = 2612736
print(multiply_list(beat_record_totals))
