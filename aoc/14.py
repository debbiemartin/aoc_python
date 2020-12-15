from . import utils
import re

MASK_LEN = 36
BITS_SET = 2**(MASK_LEN) - 1

def set_1(val, bit):
    return val | (1 << bit)
    
def set_0(val, bit):
    return val & (BITS_SET ^ (1 << bit))

class Decoder(object):   
    def __init__(self, lines):
        self.mem = {}
        self.lines = lines
    
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
                val = set_1(val, i)
            elif mask[MASK_LEN - 1 - i] == "0":
                val = set_0(val, i)
        
        yield (val, mem)

class DecoderV2(Decoder):
    def __init__(self, lines):
        super().__init__(lines)

    def apply_mask(self, val, mem, mask):
        # process 1s         
        for i in range(MASK_LEN):
            if mask[MASK_LEN - 1 - i] == "1":
                mem = set_1(mem, i)
        
        # process Xs
        memlist = [mem]
        for i in range(MASK_LEN):
            if mask[MASK_LEN - 1 - i] == "X":
                zero_list = [set_0(m, i) for m in memlist]
                one_list = [set_1(m, i) for m in memlist]
                memlist = zero_list + one_list
        
        return list(map(lambda m: (val, m), memlist))


def main():
    lines = utils.get_lines(14)

    print("PART 1:")
    d = DecoderV1(lines)
    print(d.run())

    print("PART 2:")
    d = DecoderV2(lines)
    print(d.run())