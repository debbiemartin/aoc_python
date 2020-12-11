#!/usr/bin/python3

from . import utils
import itertools
from collections import namedtuple

class Seat(object):
    def __init__(self):
        self.n_adj = 0
        self.filled = False
        self.neighbours = []
    
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)
class SeatSim(object):
    """
    Seat simulator. Iterates the seat map in time intervals. 
    """
       
    def __init__(self, part2=False):
        self.seatmap = {}
        self.part2 = part2

        lines = utils.get_lines(11)
        self.YMAX = len(lines)
        self.XMAX = len(lines[0])
        for x, y in ((x, y) for y, line in enumerate(lines) for x in range(len(line)) if line[x] == "L"):
            self.seatmap[(x, y)] = Seat()
        self.neighbour_incrs = set(itertools.permutations([-1,-1,0,1,1], 2))
        
        # Work out each seat's neighbours up front
        for coord, seat in self.seatmap.items():
            if part2:
                for n in self.neighbour_incrs:
                    # find line of sights - make sure we don't leave the grid
                    ncoord = coord
                    while (ncoord[0] >= 0 and ncoord[0] <= self.XMAX and 
                           ncoord[1] >= 0 and ncoord[1] <= self.YMAX):
                        ncoord = self.add_coord(ncoord, n)
                        if ncoord in self.seatmap:
                            seat.add_neighbour(ncoord)
                            break
            else:
                # Nearest neighbours
                for neighbour in (self.add_coord(n, coord) for n in self.neighbour_incrs):
                    if neighbour in self.seatmap:
                        seat.add_neighbour(neighbour)
    
    def __str__(self):
        str = ""
        for y in range(self.YMAX):
            for x in range(self.XMAX):
                str += (
                    "." if (x,y) not in self.seatmap else 
                    ("#" if self.seatmap[(x,y)].filled else "L")
                )
            str += "\n"

        return str
        
    def add_coord(self, coord1, coord2):
        return (coord1[0] + coord2[0], coord1[1] + coord2[1])
        
    def _iterate(self):
        changes = []
        
        #@@@ could pass through an array to check - all first time then
        #    ones who've had n_adj changed the second
        for y in range(self.YMAX):
            for x in range(self.XMAX):
                # don't process floor space
                if (x,y) not in self.seatmap:
                    continue
                
                seat = self.seatmap[(x,y)]
                
                # Empty or fill seat depending on number adjacent
                if ((seat.filled and 
                    (seat.n_adj >= 5 or seat.n_adj == 4 and not self.part2)) or 
                    (not seat.filled and seat.n_adj == 0)):
                    changes.append((x,y))
        
        # Apply the changes to seatmap
        for coord in changes:
            seat = self.seatmap[coord]
            seat.filled = not seat.filled
            
            for neighbour in seat.neighbours:
                self.seatmap[neighbour].n_adj += (1 if seat.filled else -1)

        return len(changes) != 0
               
    def iterate_until_static(self):
        while True:
            #print(self) # for debug
            if not self._iterate():
                break
        
        return sum(1 for seat in self.seatmap.values() if seat.filled)
    
    #@@@ reset function instead of making fresh class for part 2?

def main():  
    s = SeatSim()
    
    print("PART 1:")
    print(s.iterate_until_static())
    
    s = SeatSim(True)
    
    print("PART 2:")
    print(s.iterate_until_static())
    