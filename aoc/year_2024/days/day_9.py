class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def calculate(self):
        line = (int(i) for i in self.parser.get_lines()[0].strip())

        self.disk = []
        self.frees = []
        file = True
        start = 0
        for length in line:
            if file:
                self.disk.append((start, length))
            else:
                self.frees.append((start, length))
            file = not file
            start += length

    def part_1(self):
        disk = [(start, length, i)
                for i, (start, length) in enumerate(self.disk)]
        frees = self.frees[:]

        # Move the files leftward
        while disk[-1][0] > frees[0][0]:
            free = frees[0]
            file = disk[-1]
            if free[0] >= file[0]:
                break

            if file[1] >= free[1]:
                frees.pop(0)
            if file[1] <= free[1]:
                disk.pop()

            move_blocks = min(file[1], free[1])

            if file[1] > free[1]:
                # Decrease file space
                disk[-1] = (file[0], file[1]-free[1], file[2])

            if file[1] < free[1]:
                # Decrease free space
                frees[0] = (free[0]+file[1], free[1]-file[1])

            # Just put at the start, doesn't matter for csum
            disk.insert(0, (free[0], move_blocks, file[2]))

        return sum(
            (start+i)*index
            for (start, length, index) in disk
            for i in range(length)
        )

    def part_2(self):
        frees = self.frees[:]
        disk = self.disk[:]

        # Move the files leftward keeping whole files intact
        for index, file in reversed(list(enumerate(disk))):
            free_space = None
            for j, free in enumerate(frees):
                if file[0] <= free[0]:
                    break
                if file[1] <= free[1]:
                    free_space = j
                    break

            if free_space is not None:
                if frees[free_space][0] == file[0]:
                    # Remove
                    del frees[free_space]
                else:
                    # Decrement the free
                    free = frees[free_space]
                    frees[free_space] = (free[0]+file[1], free[1]-file[1])
                # Move the file in the disk
                disk[index] = (free[0], file[1])

        return sum(
            (start+i)*index
            for index, (start, length) in enumerate(disk)
            for i in range(length)
        )
