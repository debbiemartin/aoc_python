from . import utils
from collections import deque
import copy

def get_score(player):
    return sum(card * (len(player) - i) for i, card in enumerate(player))

def play(cards1, cards2, recursive):
    cards1 = copy.deepcopy(cards1)
    cards2 = copy.deepcopy(cards2)
    scores_to_date = set() 

    while len(cards1) > 0 and len(cards2) > 0:
        # Check to see whether this card configuration has appeared in the 
        # game before - if it has, player 1 wins.
        scores = (get_score(cards1), get_score(cards2))
        if scores in scores_to_date:
            return 1, get_score(cards1)
        else:
            scores_to_date.add(scores)
        
        c1 = cards1.popleft()
        c2 = cards2.popleft()
        
        if recursive and c1 <= len(cards1) and c2 <= len(cards2):
            # Truncate the cards to the value of the                 
            winner = play(deque(list(cards1)[0:c1]), deque(list(cards2)[0:c2]), True)[0]
        else:
            winner = (1 if c1 > c2 else 2)
        
        if winner == 1:
            cards1.extend([c1, c2])
        else:
            cards2.extend([c2, c1])
    
    if len(cards1) > 0:
        return 1, get_score(cards1)
    else:
        return 2, get_score(cards2)

def main():
    sections = utils.get_sections(22)
    
    player1 = deque(map(lambda x: int(x), sections[0].split("\n")[1:]))
    player2 = deque(map(lambda x: int(x), sections[1].split("\n")[1:]))
    
    print("PART 1:")
    print(play(player1, player2, False)[1])
    
    print("PART 2:")
    print(play(player1, player2, True)[1])