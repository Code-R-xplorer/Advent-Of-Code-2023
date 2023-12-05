from utils import read_file
from collections import namedtuple

values = read_file(3, str, False)

Position = namedtuple('Position', ['x', 'y'])


class Gear:
    def __init__(self, pos: Position):
        self.pos = pos
        self.connected_parts = 0
        self.part_numbers = []

    def connect_part(self, part_number):
        self.connected_parts += 1
        self.part_numbers.append(part_number)

    def get_connected_parts(self) -> int:
        return self.connected_parts

    def get_gear_ratio(self) -> int:
        return self.part_numbers[0] * self.part_numbers[1]


Grid = []
gears = {}


Symbols = "*@#-=/+%$&"


class EngineNumber:
    def __init__(self, number: int, pos: Position, length: int):
        self.number = number
        self.pos = pos
        self.length = length

    def check_vertical(self) -> bool:
        # Below
        if self.pos.y != len(Grid) - 1:
            for i in range(self.length):
                if any(c in Symbols for c in Grid[self.pos.y + 1][self.pos.x + i]):
                    if Grid[self.pos.y + 1][self.pos.x + i] == '*':
                        gears.get(Position(self.pos.x + i, self.pos.y + 1)).connect_part(self.number)
                    return True

        # Above
        if self.pos.y != 0:
            for i in range(self.length):
                if any(c in Symbols for c in Grid[self.pos.y - 1][self.pos.x + i]):
                    if Grid[self.pos.y - 1][self.pos.x + i] == '*':
                        gears.get(Position(self.pos.x + i, self.pos.y - 1)).connect_part(self.number)
                    return True

        return False

    def check_next_to(self) -> bool:
        # Left
        if self.pos.x != 0:
            if any(c in Symbols for c in Grid[self.pos.y][self.pos.x - 1]):
                if Grid[self.pos.y][self.pos.x - 1] == '*':
                    gears.get(Position(self.pos.x - 1, self.pos.y)).connect_part(self.number)
                return True

        # Right
        if (self.pos.x + self.length - 1) != len(Grid[0]) - 1:
            if any(c in Symbols for c in Grid[self.pos.y][(self.pos.x + self.length - 1) + 1]):
                if Grid[self.pos.y][(self.pos.x + self.length - 1) + 1] == '*':
                    gears.get(Position((self.pos.x + self.length - 1) + 1, self.pos.y)).connect_part(self.number)
                return True

        return False

    def check_diagonal(self) -> bool:
        # Upper Left
        if self.pos.x != 0 and self.pos.y != 0:
            if any(c in Symbols for c in Grid[self.pos.y - 1][self.pos.x - 1]):
                if Grid[self.pos.y - 1][self.pos.x - 1] == '*':
                    gears.get(Position(self.pos.x - 1, self.pos.y - 1)).connect_part(self.number)
                return True

        # Upper Right
        if (self.pos.x + self.length - 1) != len(Grid[0]) - 1 and self.pos.y != 0:
            if any(c in Symbols for c in Grid[self.pos.y - 1][(self.pos.x + self.length - 1) + 1]):
                if Grid[self.pos.y - 1][(self.pos.x + self.length - 1) + 1] == '*':
                    gears.get(Position((self.pos.x + self.length - 1) + 1, self.pos.y - 1)).connect_part(self.number)
                return True

        # Lower Left
        if self.pos.x != 0 and self.pos.y != len(Grid) - 1:
            if any(c in Symbols for c in Grid[self.pos.y + 1][self.pos.x - 1]):
                if Grid[self.pos.y + 1][self.pos.x - 1] == '*':
                    gears.get(Position(self.pos.x - 1, self.pos.y + 1)).connect_part(self.number)
                return True

        # Lower Right
        if (self.pos.x + self.length - 1) != len(Grid[0]) - 1 and self.pos.y != len(Grid) - 1:
            if any(c in Symbols for c in Grid[self.pos.y + 1][(self.pos.x + self.length - 1) + 1]):
                if Grid[self.pos.y + 1][(self.pos.x + self.length - 1) + 1] == '*':
                    gears.get(Position((self.pos.x + self.length - 1) + 1, self.pos.y + 1)).connect_part(self.number)
                return True

        return False

    def check_adjacent(self) -> bool:
        return self.check_vertical() or self.check_next_to() or self.check_diagonal()



current_y = 0

engine_numbers = []


for value in values:
    line = [*value]
    Grid.append(line)
    row_length = len(line)
    current_number_str = ""

    for count, character in enumerate(line):
        if character == '*':
            gears[Position(count, current_y)] = Gear(Position(count, current_y))
        if character.isnumeric():
            if current_number_str == "":
                starting_pos = Position(count, current_y)
            current_number_str += character
        if any(s in Symbols for s in character) and len(current_number_str) > 0:
            engine_numbers.append(EngineNumber(int(current_number_str), starting_pos, len(current_number_str)))
            current_number_str = ""
        if character == '.' and len(current_number_str) > 0:
            engine_numbers.append(EngineNumber(int(current_number_str), starting_pos, len(current_number_str)))
            current_number_str = ""
        if count == len(line) - 1 and len(current_number_str) > 0:
            engine_numbers.append(EngineNumber(int(current_number_str), starting_pos, len(current_number_str)))
            current_number_str = ""
    current_y += 1

total = 0

for engineNumber in engine_numbers:
    if engineNumber.check_adjacent():
        total += engineNumber.number

# Part 1 = 544664
print(total)

gear_ratio_sum = 0

for position in gears:
    if gears[position].get_connected_parts() == 2:
        gear_ratio_sum += gears[position].get_gear_ratio()

# Part 2 = 84495585
print(gear_ratio_sum)



