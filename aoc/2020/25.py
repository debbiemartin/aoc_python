from sympy.ntheory.residue_ntheory import discrete_log

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    @staticmethod
    def get_key(loop_sz, sub_num=7):
        val = 1
        for _ in range(loop_sz):
            val *= sub_num
            val = val % 20201227

        return val

    @staticmethod
    def get_loop_sz(pub_key):
        return discrete_log(20201227, pub_key, 7)

    def calculate(self):
        self.door_pub_key = 3418282
        self.card_pub_key = 8719412
        self.card_loop = self.get_loop_sz(self.card_pub_key)
        self.door_loop = self.get_loop_sz(self.door_pub_key)

    def part_1(self):
        return (self.get_key(self.card_loop, sub_num=self.door_pub_key), self.get_key(self.door_loop, sub_num=self.card_pub_key))

    def part_2(self):
        return ""
