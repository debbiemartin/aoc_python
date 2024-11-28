import re

MASK_LEN = 36
BITS_SET = 2**(MASK_LEN) - 1


class Decoder(object):
    def __init__(self, lines):
        self.mem = {}
        self.lines = lines

    @staticmethod
    def set_1(val, bit):
        return val | (1 << bit)

    @staticmethod
    def set_0(val, bit):
        return val & (BITS_SET ^ (1 << bit))

    def run(self):
        r = re.compile(r"^mem\[(?P<loc>[0-9]+)\] = (?P<val>[0-9]+)$")
        for line in self.lines:
            if line.startswith("mask"):
                mask = line.strip("mask = ")
            else:
                m = r.match(line)
                assert(m is not None)
                for val, mem in self.apply_mask(int(m.group("val")),  int(m.group("loc")), mask):
                    self.mem[mem] = val

        return sum(val for val in self.mem.values())

    def apply_mask(self, val, mem, mask):
        raise NotImplementedError


class DecoderV1(Decoder):
    def __init__(self, lines):
        super().__init__(lines)

    def apply_mask(self, val, mem, mask):
        for i in range(MASK_LEN):
            if mask[MASK_LEN - 1 - i] == "1":
                val = self.set_1(val, i)
            elif mask[MASK_LEN - 1 - i] == "0":
                val = self.set_0(val, i)

        yield (val, mem)

class DecoderV2(Decoder):
    def __init__(self, lines):
        super().__init__(lines)

    def apply_mask(self, val, mem, mask):
        # process 1s
        for i in range(MASK_LEN):
            if mask[MASK_LEN - 1 - i] == "1":
                mem = self.set_1(mem, i)

        # process Xs
        memlist = [mem]
        for i in range(MASK_LEN):
            if mask[MASK_LEN - 1 - i] == "X":
                zero_list = [self.set_0(m, i) for m in memlist]
                one_list = [self.set_1(m, i) for m in memlist]
                memlist = zero_list + one_list

        return list(map(lambda m: (val, m), memlist))

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.lines = self.parser.get_lines()

    def part_1(self):
        d = DecoderV1(self.lines)
        return d.run()

    def part_2(self):
        d = DecoderV2(self.lines)
        return d.run()
