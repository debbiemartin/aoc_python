class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def history(self, line, index):
        differences = [line[i+1]-line[i] for i in range(len(line)-1)]
        if all(x == 0 for x in differences):
            return 0 + line[index]
        else:
            if index == -1:
                return self.history(differences, index) + line[index]
            elif index == 0:
                return line[index] - self.history(differences, index)

    def calculate(self):
        self.lines = [[int(l) for l in line.split()] for line in self.parser.get_lines()]

    def part_1(self):
        return sum(self.history(line, index=-1) for line in self.lines)

    def part_2(self):
        return sum(self.history(line, index=0) for line in self.lines)
