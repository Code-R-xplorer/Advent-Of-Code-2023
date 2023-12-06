import math

from utils import read_file


class Map:
    def __init__(self, source_start, destination_start, range_length):
        self.source_start = source_start
        self.destination_start = destination_start
        self.range_length = range_length

    def map_value(self, source):
        if source >= self.source_start and source <= self.source_start + self.range_length:
            n = source - self.source_start
            return self.destination_start + n
        else:
            return source


seed_to_soil_maps = []
soil_to_fertilizer_maps = []
fertilizer_to_water_maps = []
water_to_light_maps = []
light_to_temperature_maps = []
temperature_to_humidity_maps = []
humidity_to_location_maps = []

seeds = []

lines = read_file(5, str, False)


current_map = 0

for line in lines:
    if 'seeds:' in line:
        _, values = line.split(': ')
        seed_ranges = values.split(' ')
        seed_ranges = [int(i) for i in seed_ranges]
        for seed_range in range(0, len(seed_ranges), 2):
            for i in range(seed_ranges[seed_range], seed_ranges[seed_range + 1] + seed_ranges[seed_range]):
                seeds.append(i)
        continue
    if 'seed-to-soil map:' in line:
        current_map = 1
        continue
    if 'soil-to-fertilizer map:' in line:
        current_map = 2
        continue
    if 'fertilizer-to-water map:' in line:
        current_map = 3
        continue
    if 'water-to-light map:' in line:
        current_map = 4
        continue
    if 'light-to-temperature map:' in line:
        current_map = 5
        continue
    if 'temperature-to-humidity map:' in line:
        current_map = 6
        continue
    if 'humidity-to-location map:' in line:
        current_map = 7
        continue
    if line != '':
        values = line.split(' ')
        values = [int(i) for i in values]
        if current_map == 1:
            seed_to_soil_maps.append(Map(values[1], values[0], values[2]))
        if current_map == 2:
            soil_to_fertilizer_maps.append(Map(values[1], values[0], values[2]))
        if current_map == 3:
            fertilizer_to_water_maps.append(Map(values[1], values[0], values[2]))
        if current_map == 4:
            water_to_light_maps.append(Map(values[1], values[0], values[2]))
        if current_map == 5:
            light_to_temperature_maps.append(Map(values[1], values[0], values[2]))
        if current_map == 6:
            temperature_to_humidity_maps.append(Map(values[1], values[0], values[2]))
        if current_map == 7:
            humidity_to_location_maps.append(Map(values[1], values[0], values[2]))

mapped_values = []


def map_helper(maps, from_value):
    _value = -1
    for _map in maps:
        if _map.map_value(from_value) != from_value:
            _value = _map.map_value(from_value)
            break
    if _value == -1:
        _value = from_value
    return _value


for seed in seeds:
    # soil, fertilizer, water, light, temperature, humidity, location = -1, -1, -1, -1, -1, -1, -1

    soil = map_helper(seed_to_soil_maps, seed)
    fertilizer = map_helper(soil_to_fertilizer_maps, soil)
    water = map_helper(fertilizer_to_water_maps, fertilizer)
    light = map_helper(water_to_light_maps, water)
    temperature = map_helper(light_to_temperature_maps, light)
    humidity = map_helper(temperature_to_humidity_maps, temperature)
    location = map_helper(humidity_to_location_maps, humidity)

    mapped_values.append([seed, soil, fertilizer, water, light, temperature, humidity, location])

# for value in mapped_values:
#     print(f'Seed {value[0]}, soil {value[1]}, fertilizer {value[2]}, water {value[3]}, light {value[4]}, temperature {value[5]}, humidity {value[6]}, location {value[7]}')

lowest_location = math.inf

for mapped_value in mapped_values:
    if mapped_value[7] < lowest_location:
        lowest_location = mapped_value[7]

print(lowest_location)


