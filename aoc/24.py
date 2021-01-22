from . import utils 
from collections import defaultdict

dirs = {
    "se": (1,-1),
    "e":  (2,0),
    "ne": (1,1),
    "nw": (-1,1),
    "w":  (-2,0),
    "sw": (-1,-1),
}

@utils.memoize
def get_neighbours(coord):
    return [utils.add_coord(coord, dirval) for dirval in dirs.values()]

def get_initial(lines):
    tiles = defaultdict(lambda: 0)
    
    for line in lines:
        coord = (0,0)

        while len(line) > 0:
            for dirname, dirval in dirs.items():
                if line.startswith(dirname):
                    coord = utils.add_coord(coord, dirval)
                    line = line[len(dirname):]
        
        # Flip it - 1->0, 0->1
        tiles[coord] = 1 - tiles[coord]
        
    # Make the initial to_check list: all black tiles and their neighbours
    to_check = set()
    for key, val in ((key, val) for (key, val) in tiles.items() if val == 1):
        to_check.add(key)
        for n in get_neighbours(key):
            to_check.add(n)

    return tiles, to_check

def play_day(tiles, to_check):
    new_to_check = set()
    to_flip = []
    
    for tile in to_check:
        black_neighbours = sum(1 for n in get_neighbours(tile) if tiles[n] == 1)
        flip = ((tiles[tile] == 0 and black_neighbours == 2) or 
                (tiles[tile] == 1 and 
                (black_neighbours == 0 or black_neighbours > 2)))
        
        if flip:            
            to_flip.append(tile) 
            for n in get_neighbours(tile):
                new_to_check.add(n)
    
    # Flip tiles simultaneously
    for tile in to_flip:
        tiles[tile] = 1 - tiles[tile]
    
    return new_to_check
    
def main():
    tiles, to_check = get_initial(utils.get_lines(24))
        
    print("PART 1:")    
    print(sum(1 for t in tiles.values() if t == 1))
    
    for i in range(100):
        to_check = play_day(tiles, to_check)

    print("PART 2:")
    print(sum(1 for t in tiles.values() if t == 1))