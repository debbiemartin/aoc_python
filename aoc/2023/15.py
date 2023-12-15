from collections import OrderedDict

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def get_hash(self, string):
        current_value = 0
        for c in string:
            current_value += ord(c)
            current_value = current_value * 17
            current_value = current_value % 256

        return current_value

    def calculate(self):
        self.strings = "".join(self.parser.get_lines()).split(",")

    def part_1(self):
        score = 0
        self.boxes = {i:OrderedDict() for i in range(256)}
        for s in self.strings:
            current_value = self.get_hash(s)
            score += current_value
        return score

    def part_2(self):
        self.boxes = {i:OrderedDict() for i in range(256)}
        for s in self.strings:
            if s.endswith("-"):
                current_value = self.get_hash(s[:-1])
                if s[:-1] in self.boxes[current_value].keys():
                    self.boxes[current_value].pop(s[:-1])
            elif "=" in s:
                label = s.split("=")[0]
                current_value = self.get_hash(label)
                focal = int(s.split("=")[1])
                self.boxes[current_value][label] = focal

        score = 0
        for i, box in self.boxes.items():
            for slot, (lens, focal) in enumerate(box.items()):
                score += (i+1)*(slot+1)*focal

        return score
