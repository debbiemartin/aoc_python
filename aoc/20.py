from . import utils
from functools import reduce
import math

class Monster(object):
    MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
    ]
    width = len(MONSTER[0])
    length = len(MONSTER)
    hashs = [(i,j) for i, line in enumerate(MONSTER) for j, char in enumerate(line) if char == "#"]       
    

class Tile(object):
    tile_size = 0
    
    def __init__(self, lines):
        self.id = lines[0].strip(":").strip("Tile ")
        
        self.lines = lines[1:]
        self.size = len(self.lines[0])
    
    @property
    def sides(self):
        return [self.lines[0], "".join(line[-1] for line in self.lines), 
                self.lines[-1][::-1], "".join([line[0] for line in reversed(self.lines)])]
    
    def strip_edges(self):
        # Strip one line off all the edges. This irreversibly changes 
        # self.lines
        self.lines = list(map(lambda line: line[1:-1], self.lines[1:-1]))
        if Tile.tile_size == 0:
            Tile.tile_size = len(self.lines)
    
    def _try_rotation(self, sides, matches):
        # 1 CONSTRAINT
        # Position the tile with the matching side as the side number specified
        for i in range(4):
            if all(self.sides[side] in matches for side in sides):
                return True
            self.lines = utils.rotate(self.lines)

    def orientate(self, sides, matches):
        # sides is the indices of the end orientation, in which the sides of 
        # specified indices must appear in the matches list
        
        if not self._try_rotation(sides, matches):
            self.lines = utils.flip(self.lines)
            assert(self._try_rotation(sides, matches))

class Board(object):
    def __init__(self, tiles):
        self.tiles = {tile.id: tile for tile in tiles}
        self.extent = int(math.sqrt(len(tiles)))
        self.grid = self._solve()
        self.image = self._glue_grid()
    
    def _traverse(self, get_current, get_prev, side_current, side_prev, grid):
        # traverse a row or column by supplying get_current and get_prev 
        # accessors, matching a tile with specified sides each time. Assumes
        # sides direct oppositely
        for i in range(1, self.extent):
            side = self.tiles[grid[get_prev(i)]].sides[side_prev]
            for t2_id, t2 in ((t2_id, t2) for (t2_id, t2) in self.tiles.items() if t2_id not in grid.values()):
                if any(side == side2 or side == side2[::-1] for side2 in t2.sides):
                    grid[get_current(i)] = t2_id
                    t2.orientate([side_current], [side[::-1]])
                    break
            else:
                # didn't find a match
                assert(False)
       
    def _solve(self):
        grid = {}
        # Find a corner - a tile which matches only 2 other tiles
        for t1_id, t1 in self.tiles.items():
            # count up the number of sides which match
            matches = []
            for side in t1.sides:
                for t2_id, t2 in ((t2_id, t2) for (t2_id, t2) in self.tiles.items() if t2_id != t1_id):
                    if any(side == side2 or side == side2[::-1] for side2 in t2.sides):
                        matches.append(side)
                        break
            
            if len(matches) == 2:
                grid[(0,0)] = t1_id
                break
        else:
            # Didn't find a corner
            assert(False)                
        
        # Position the corner
        self.tiles[grid[(0,0)]].orientate([1, 2], matches)
        
        # Solve the 0th row
        # Match the side 3 (left) of a new tile to side 1 (right) of the 
        # leftwards tile.
        self._traverse(lambda i: (0,i), lambda i: (0,i-1), 3, 1, grid)
        
        # Solve all columns downwards
        # Match the side 0 (up) of a new tile to side 2 (down) of the upwards
        # tile.
        for col in range(self.extent):
            self._traverse(lambda i: (i,col), lambda i: (i-1,col), 0, 2, grid)
        
        return grid
    
    def _glue_grid(self):
        # Strip the tiles and glue them together into the image as specified in
        # self.grid. The tiles must already be orientated
        for t in self.tiles.values():
            t.strip_edges()

        lines = []
        for row in range(self.extent):
            # Glue the row together:
            lines += ["".join(self.tiles[self.grid[(row, i)]].lines[j] for i in range(self.extent)) for j in range(Tile.tile_size)]
        
        return lines
    
    def get_corners(self):
        # Retrieve product of tile IDs of each of the 4 corners of the grid
        corners = [(0,0), (0,self.extent-1), (self.extent-1,0), (self.extent-1,self.extent-1)]
        
        return reduce(lambda a, b: int(a) * int(b), (self.grid[c] for c in corners))
       
    def _search_monsters(self):
        # Search the image for monsters
        found = False
        for i in range(len(self.image) - Monster.length):
            for j in range(len(self.image) - Monster.width):
                if all(self.image[i + im][j + jm] == "#" for (im, jm) in Monster.hashs):
                    # Found a monster: mark it
                    found = True
                    for (im, jm) in Monster.hashs:
                        line = list(self.image[i + im])
                        line[j + jm] = "O"
                        self.image[i + im] = "".join(line)

        return found  
        
    def _try_rotation(self):
        # Search for sea monsters in the 4 rotations of the image
        for i in range(4):
            if self._search_monsters():
                return True
            self.image = utils.rotate(self.image)
        return False
    
    def find_monsters(self):
        # Search for sea monsters in the 2x flipped * 4x rotation states of the
        # image. Return the water roughness i.e. how many hashs are not a part
        # of a sea monster 
        if not self._try_rotation():
            self.image = utils.flip(self.image)
            assert(self._try_rotation())
        
        return sum(1 for line in self.image for char in line if char == "#")

def main():
    sections = utils.get_sections(20)
    
    tiles = [Tile(section.split("\n")) for section in sections]
    board = Board(tiles)
    
    print("PART 1:")
    print(board.get_corners())

    print("PART 2:")
    print(board.find_monsters())