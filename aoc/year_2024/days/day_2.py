class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.lines = [[int(n) for n in l.split()] for l in parser.get_lines()]

    def is_safe(self, line, tolerate=False):
        increasing = (line[1] > line[0])
        for index, (a, b) in enumerate(zip(line, line[1:])):
            if (b > a) != increasing or abs(b - a) < 1 or abs(b - a) > 3:
                # Don't tolerate because only 1 can be removed
                if not tolerate:
                    return False
                trial_a = line[:]
                del trial_a[index]
                trial_b = line[:]
                del trial_b[index + 1]
                return (self.is_safe(trial_a) or self.is_safe(trial_b))

        return True

    def is_safe_tolerate(self, line):
        return (self.is_safe(line, True) or self.is_safe(line[1:], False))

    def calculate(self):
        pass

    def part_1(self):
        return sum(self.is_safe(l) for l in self.lines)

    def part_2(self):
        return sum(self.is_safe_tolerate(l) for l in self.lines)
