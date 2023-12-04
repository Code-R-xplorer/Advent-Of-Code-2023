from utils import read_file
from collections import namedtuple

values = read_file(3, str, False)

Position = namedtuple('Position', ['x', 'y'])

Grid = []

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
                    return True

        # Above
        if self.pos.y != 0:
            for i in range(self.length):
                if any(c in Symbols for c in Grid[self.pos.y - 1][self.pos.x + i]):
                    return True

        return False

    def check_next_to(self) -> bool:
        # Left
        if self.pos.x != 0:
            if any(c in Symbols for c in Grid[self.pos.y][self.pos.x - 1]):
                return True

        # Right
        if (self.pos.x + self.length - 1) != len(Grid[0]) - 1:
            if any(c in Symbols for c in Grid[self.pos.y][(self.pos.x + self.length - 1) + 1]):
                return True

        return False

    def check_diagonal(self) -> bool:
        # Upper Left
        if self.pos.x != 0 and self.pos.y != 0:
            if any(c in Symbols for c in Grid[self.pos.y - 1][self.pos.x - 1]):
                return True

        # Upper Right
        if (self.pos.x + self.length - 1) != len(Grid[0]) - 1 and self.pos.y != 0:
            if any(c in Symbols for c in Grid[self.pos.y - 1][(self.pos.x + self.length - 1) + 1]):
                return True

        # Lower Left
        if self.pos.x != 0 and self.pos.y != len(Grid) - 1:
            if any(c in Symbols for c in Grid[self.pos.y + 1][self.pos.x - 1]):
                return True

        # Lower Right
        if (self.pos.x + self.length - 1) != len(Grid[0]) - 1 and self.pos.y != len(Grid) - 1:
            if any(c in Symbols for c in Grid[self.pos.y + 1][(self.pos.x + self.length - 1) + 1]):
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
            print(starting_pos)
            engine_numbers.append(EngineNumber(int(current_number_str), starting_pos, len(current_number_str)))
            current_number_str = ""
    current_y += 1

# for engine in engine_numbers:
#     print(f'Number(value={engine.number}, start_position=({engine.pos.x}, {engine.pos.y}), length={engine.length})')

print(len(engine_numbers))

total = 0

for engineNumber in engine_numbers:
    if engineNumber.check_adjacent():
        total += engineNumber.number

# Part 1 = 544664
print(total)
