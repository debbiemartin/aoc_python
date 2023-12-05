class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        self.sections = self.parser.get_sections_list()

    def part_1(self):
        seeds = {int(x):int(x) for x in self.sections[0][0].split(": ")[1].split()}
        for section in self.sections[1:]:
            maps = section[1:]
            for seed, val in seeds.items():
                for m in maps:
                    dest, source, range_len = map(lambda x: int(x), m.split())
                    diff = val - source
                    if 0 <= diff < range_len:
                        seeds[seed] = dest + diff
                        break
        return min(seeds.values())

    def part_2(self):
        seed_list = self.sections[0][0].split(": ")[1].split()
        ranges = []
        for seed, range_len in zip(*[iter(seed_list)]*2):
            ranges.append((int(seed), int(seed)+int(range_len)-1))

        for section in self.sections[1:]:
            new_ranges = []
            maps = section[1:]
            for i, r in enumerate(ranges):
                if not r:
                    continue
                range_start, range_end = r
                for m in maps:
                    map_dest, map_source, map_range_len = map(lambda x: int(x), m.split())
                    # add the overlap to new_ranges
                    overlap = (max(map_source, range_start), min(map_source+map_range_len-1, range_end))
                    if overlap[0] < overlap[1]:
                        diff = map_dest-map_source
                        new_ranges.append((overlap[0]+diff, overlap[1]+diff))
                        # take it off the current range
                        if overlap[0] == range_start and overlap[1] == range_end:
                            ranges[i] = None
                        elif overlap[0] == range_start:
                            ranges[i] = (overlap[1], range_end)
                        elif overlap[1] == range_end:
                            ranges[i] = (range_start, overlap[0])
                        else:
                            ranges[i] = (range_start, overlap[0])
                            ranges.append((overlap[1], range_end))

            ranges += new_ranges

        return min(r[0] for r in ranges if r)
