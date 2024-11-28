from .. import utils

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def string_after(self, string, i):
        if i < len(string) - 1:
            return string[i+1:]
        return ""

    @utils.memoize
    def arrangements(self, springs, counts, spring_count=0):
        counts = [int(x) for x in counts.strip("[]").split(", ")]
        for i, char in enumerate(springs):
            if char == ".":
                if spring_count == 0:
                    continue
                elif spring_count == counts[0]:
                    if len(counts) == 1:
                        return 1 if "#" not in self.string_after(springs, i) else 0
                    return self.arrangements(self.string_after(springs, i), str(counts[1:]))
                else:
                    return 0
            elif char == "#":
                spring_count += 1
            elif char == "?":
                return (
                    self.arrangements("."+self.string_after(springs, i), str(counts), spring_count) +
                    self.arrangements("#"+self.string_after(springs, i), str(counts), spring_count)
                )

        # ends with #
        if len(counts) == 1 and spring_count == counts[0]:
            return 1
        else:
            return 0

    def calculate(self):
        self.records = [(l.split()[0], [int(x) for x in l.split()[1].split(",")]) for l in self.parser.get_lines()]

    def count_arrangements(self, records):
        arrangements = 0
        for springs, counts in records:
             a = self.arrangements(springs, str(counts))
             arrangements += a
        return arrangements

    def part_1(self):
        return self.count_arrangements(self.records)

    def part_2(self):

        records = [("?".join([a] * 5), b*5) for a, b in self.records]
        print(records)
        return self.count_arrangements(records)
