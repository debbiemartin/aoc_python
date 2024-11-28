import re

class Number(object):
    def __init__(self, value, row, start_col, end_col):
        self.value = value
        self.row = row
        self.start_col = start_col
        self.end_col = end_col
        self.adjacent = []

        for col in range(start_col-1, end_col+1):
            self.adjacent.append((row-1, col))
            self.adjacent.append((row+1, col))

        self.adjacent.append((row, start_col-1))
        self.adjacent.append((row, end_col))


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def is_symbol(self, row, col):
        if row < 0 or col < 0 or row >= self.num_rows or col >= self.num_cols:
            return False
        if self.lines[row][col] == ".":
            return False
        if self.lines[row][col].isnumeric():
            return False
        return True

    def is_part_number(self, number):
        # not a part number if all of the symbols around it are . or off the
        # grid
        return any(self.is_symbol(i, j) for (i, j) in number.adjacent)

    def calculate(self):
        self.lines = self.parser.get_lines()
        self.num_rows = len(self.lines)
        self.num_cols = len(self.lines[0])
        self.part_nums = []
        for i, row in enumerate(self.lines):
            for match in re.finditer(r"\d+", row):
                num = Number(int(match.group()), i, match.span()[0], match.span()[1])
                if self.is_part_number(num):
                    self.part_nums.append(num)

    def part_1(self):
        return sum(p.value for p in self.part_nums)

    def part_2(self):
        # go through the lines and find the * symbols. If it's next to 2 part
        # numbers then find the gear ratio by multiplying them
        gear_ratio_sum = 0
        for (i, j) in ((i, j) for (i, row) in enumerate(self.lines) for (j, char) in enumerate(row) if char == "*"):
          # If it's next to 2 part numbers then times them together
          part_nums = [p for p in self.part_nums if (i,j) in p.adjacent]
          if len(part_nums) == 2:
              gear_ratio_sum += part_nums[0].value * part_nums[1].value

        return gear_ratio_sum
