from z3 import *

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def intersection(self, a, b, area=None, collision=False):
        # a = (a1, a2, a3) + (av1, av2, av3)*t
        # b = (b1, b2, b3) + (bv1, bv2, bv3)*t
        # a1 + av1*t1 = b1 + bv1*t2
        # a2 + av2*t1 = b2 + bv2*t2

        # intersection:
        #   t1 = (b1 - a1 + bv1*t2) / av1 = (b2 - a2 + bv2*t2) / av2
        #   av2(b1 - a1 + bv1*t2) = av1(b2 - a2 + bv2*t2)
        #   t2(av2*bv1 - av1*bv2) = av1*b2 - av1*a2 + av2*a1 - av2*b1

        print(a)
        print(b)
        a1, a2, a3 = a["x"]
        b1, b2, b3 = b["x"]
        av1, av2, av3 = a["v"]
        bv1, bv2, bv3 = b["v"]
        denominator = av2*bv1 - av1*bv2
        if denominator == 0:
            # parallel
            print("parallel")
            return False

        t2 = (av1*b2-av1*a2+av2*a1-av2*b1)/denominator
        t1 = (b1-a1+bv1*t2)/av1

        # See whether any is in the past
        if t1 < 0 and t2 < 0:
            print("both in past")
            return False
        if t1 < 0:
            print("a in past")
            return False
        if t2 < 0:
            print("b in past")
            return False
        if collision:
            if t1 != t2:
                return False
            # Check whether the z coordinates coincide
            return (a3+av3*t1 == b3+bv3*t1)

        i = ((a1 + av1*t1), (a2 + av2*t1))
        print(f"found intersection: {i}")
        if area:
            minimum, maximum = area
            return (minimum <= i[0] <= maximum) and (minimum <= i[1] <= maximum)

        return (i is not None)

    def calculate(self):
        lines = self.parser.get_lines()
        self.hailstones = []
        for line in lines:
            position = tuple(int(i) for i in line.split(" @ ")[0].split(","))
            velocity = tuple(int(i) for i in line.split(" @ ")[1].split(","))
            self.hailstones.append({"x": position, "v": velocity})


    def part_1(self):
        intersections = []
        area = (200000000000000, 400000000000000)
        for i in range(len(self.hailstones)):
            for j in range(i+1, len(self.hailstones)):
                intersections.append(
                    self.intersection(self.hailstones[i],
                                      self.hailstones[j],
                                      area=area)
                )

        return intersections.count(True)

    def part_2(self):
       solver = Solver()
       x,y,z,vx,vy,vz = Int('x'),Int('y'),Int('z'),Int('vx'),Int('vy'),Int('vz')
       collision_t = [Int(f'T{i}') for i in range(len(self.hailstones))]

       for i in range(len(self.hailstones)):
           solver.add(x + collision_t[i]*vx == self.hailstones[i]["x"][0] + collision_t[i]*self.hailstones[i]["v"][0])
           solver.add(y + collision_t[i]*vy == self.hailstones[i]["x"][1] + collision_t[i]*self.hailstones[i]["v"][1])
           solver.add(z + collision_t[i]*vz == self.hailstones[i]["x"][2] + collision_t[i]*self.hailstones[i]["v"][2])

       res = solver.check()
       m = solver.model()

       return m.eval(x+y+z)
