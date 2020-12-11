#!/usr/bin/python3

from . import utils
import itertools

class SeatSim(object):
    """
    Seat simulator. Iterates the seat map in time intervals. 
    """
       
    def __init__(self):
        self.seatmap = {}

        lines = utils.get_lines(11)
        self.YMAX = len(lines)
        self.XMAX = len(lines[0])
        for y, line in enumerate(lines):
            for x in range(len(line)):
                if line[x] == "#":
                    self.seatmap[(x, y)] = True
                elif line[x] == "L":
                    self.seatmap[(x, y)] = False
        self.neighbour_incrs = set(itertools.permutations([-1,-1,0,1,1], 2))
    
    def __str__(self):
        str = ""
        for y in range(self.YMAX):
            for x in range(self.XMAX):
                str += (
                    "." if (x,y) not in self.seatmap else 
                    ("#" if self.seatmap[(x,y)] else "L")
                )
            str += "\n"

        return str
        
    def add_coord(self, coord1, coord2):
        return (coord1[0] + coord2[0], coord1[1] + coord2[1])
        
    def _iterate(self, part2):
        changes = []
        for y in range(self.YMAX):
            for x in range(self.XMAX):
                # don't process floor space
                if (x,y) not in self.seatmap:
                    continue
           
                if not part2:
                    n_adj = sum(
                        1 for n in self.neighbour_incrs if 
                        self.add_coord(n, (x,y)) in self.seatmap and self.seatmap[self.add_coord(n, (x,y))]
                    )
                else:
                    n_adj = 0
                    for n in self.neighbour_incrs:
                        # go in inc until 
                        coord = (x,y)
                        while (coord[0] >= 0 and coord[0] <= self.XMAX and 
                               coord[1] >= 0 and coord[1] <= self.YMAX):
                            coord = self.add_coord(coord, n)
                            if coord in self.seatmap:
                                if self.seatmap[coord]:
                                    n_adj += 1
                                break
                
                # Empty or fill seat depending on number adjacent
                if ((self.seatmap[(x,y)] and 
                    (n_adj >= 5 or n_adj == 4 and not part2)) or 
                    (not self.seatmap[(x,y)] and n_adj == 0)):
                    changes.append((x,y))
        
        # Apply the changes to seatmap
        for coord in changes:
            self.seatmap[coord] = not self.seatmap[coord]
         
        return len(changes) != 0
               
    def iterate_until_static(self, part2=False):
        while True:
            #print(self) # for debug
            if not self._iterate(part2):
                break
        
        return sum(1 for seat in self.seatmap.values() if seat)

def main():  
    s = SeatSim()
    
    print("PART 1:")
    print(s.iterate_until_static())
    
    s = SeatSim()
    
    print("PART 2:")
    print(s.iterate_until_static(True))
    