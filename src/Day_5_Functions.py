import math
from datetime import datetime


def map_helper(maps, from_value):
    _value = -1
    for _map in maps:
        if _map.map_value(from_value) != from_value:
            _value = _map.map_value(from_value)
            break
    if _value == -1:
        _value = from_value
    return _value


def process_seed_range(seed_range, maps, lowest_values):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'Process Seed Started at {current_time}')
    _lowest = math.inf
    for _seed in range(seed_range[0], seed_range[0] + seed_range[1]):
        _soil = map_helper(maps[0], _seed)
        _fertilizer = map_helper(maps[1], _soil)
        _water = map_helper(maps[2], _fertilizer)
        _light = map_helper(maps[3], _water)
        _temperature = map_helper(maps[4], _light)
        _humidity = map_helper(maps[5], _temperature)
        _location = map_helper(maps[6], _humidity)
        if _location < _lowest:
            _lowest = _location
    lowest_values.append(_lowest)

