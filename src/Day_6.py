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

# Part 2

new_time = ""
for time in times:
    new_time += str(time)

new_distance = ""
for distance in distances:
    new_distance += str(distance)

new_time = int(new_time)
new_distance = int(new_distance)

new_beaten_record = 0
# Very slow and needs to be improved later
for j in range(new_time + 1):
    time_left = new_time - j
    distance_covered = time_left * j
    if distance_covered > new_distance:
        new_beaten_record += 1

# Part 2 = 29891250
print(new_beaten_record)
