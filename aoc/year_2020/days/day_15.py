class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
       self.starts = self.parser.get_lines()[0].split(",")

    def run(self, lastindex_match):
       last_occ = {}
       for index, start in enumerate(self.starts[:-1]):
           last_occ[int(start)] = index + 1

       # Don't put the last spoken num in the last occurrences array so we can
       # compute the next number
       lastnum, lastindex = int(self.starts[-1]), len(self.starts)
       while True:
           newnum = (0 if lastnum not in last_occ
                       else (lastindex - last_occ[lastnum]))

           last_occ[lastnum] = lastindex

           lastnum = newnum
           lastindex += 1

           if lastindex == lastindex_match:
               return lastnum

    def part_1(self):
        return self.run(2020)

    def part_2(self):
        return self.run(30000000)
