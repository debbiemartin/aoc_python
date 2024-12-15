from ... import utils


class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def dir_to_coord(self, dir):
        if dir == "v":
            return (0, 1)
        if dir == "^":
            return (0, -1)
        if dir == "<":
            return (-1, 0)
        if dir == ">":
            return (1, 0)

    def calculate(self):
        self.plot = self.parser.get_sections_list()[0]

        self.dirs = [
            self.dir_to_coord(d)
            for line in self.parser.get_sections_list()[1]
            for d in line
        ]

    def part_1(self):
        boxes = set()
        walls = set()
        for y, line in enumerate(self.plot):
            for x, char in enumerate(line):
                if char == "@":
                    robot = (x, y)
                if char == "#":
                    walls.add((x, y))
                if char == "O":
                    boxes.add((x, y))
        assert (robot)

        for d in self.dirs:
            neighbour = utils.add_coord(robot, d)

            # Wall
            if neighbour in walls:
                continue

            # Step
            if neighbour not in boxes:
                robot = neighbour
                continue

            # Try to move boxes
            coord = neighbour
            while True:
                coord = utils.add_coord(coord, d)
                if coord in walls:
                    break
                if coord not in boxes:
                    # Robot moves by dir in 1 step, first box after the robot
                    # moves into coord
                    boxes.add(coord)
                    boxes.remove(neighbour)
                    robot = neighbour
                    break

        return sum(100*y+x for x, y in boxes)

    def part_2(self):
        boxes = set()
        walls = set()
        for y, line in enumerate(self.plot):
            for x, char in enumerate(line):
                if char == "@":
                    robot = (2*x, y)
                if char == "#":
                    walls.add((2*x, y))
                    walls.add((2*x+1, y))
                if char == "O":
                    boxes.add((2*x, y))
        assert (robot)

        for d in self.dirs:
            # for y in range(10):
            #     for x in range(20):
            #         if (x, y) in walls:
            #             print("#", end="")
            #         elif (x, y) in boxes:
            #             print("[", end="")
            #         elif (x-1, y) in boxes:
            #             print("]", end="")
            #         elif (x, y) == robot:
            #             print("@", end="")
            #         else:
            #             print(".", end="")
            #     print()
            # print(d)

            neighbour = utils.add_coord(robot, d)

            # Wall
            if neighbour in walls:
                continue

            # Step
            if neighbour not in boxes and utils.add_coord(neighbour, (-1, 0)) not in boxes:
                robot = neighbour
                continue

            # Try to move boxes
            move = set()
            coords = [utils.add_coord(robot, d)]

            while coords:
                coord = coords.pop(0)
                if coord in walls:
                    break
                coord_neighbour = utils.add_coord(coord, (-1, 0))

                box = None
                if coord in boxes:
                    box = coord
                elif coord_neighbour in boxes:
                    box = coord_neighbour
                else:
                    continue

                move.add(box)

                if d == (1, 0):
                    coords.append(utils.add_coord(box, (2, 0)))
                if d == (-1, 0):
                    coords.append(utils.add_coord(box, (-1, 0)))
                if d == (0, 1):
                    coords.append(utils.add_coord(box, (0, 1)))
                    coords.append(utils.add_coord(box, (1, 1)))
                if d == (0, -1):
                    coords.append(utils.add_coord(box, (0, -1)))
                    coords.append(utils.add_coord(box, (1, -1)))
            else:
                robot = utils.add_coord(robot, d)
                # Move by 1
                for box in move:
                    boxes.remove(box)
                for box in move:
                    boxes.add(utils.add_coord(d, box))

        return sum(100*y+x for x, y in boxes)
