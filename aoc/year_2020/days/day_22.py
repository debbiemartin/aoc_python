from collections import deque
import copy

class Day(object):
    def __init__(self, parser):
        self.parser = parser

    def get_score(self, player):
        return sum(card * (len(player) - i) for i, card in enumerate(player))

    def play(self, cards1, cards2, recursive):
        cards1 = copy.deepcopy(cards1)
        cards2 = copy.deepcopy(cards2)
        scores_to_date = set()

        while len(cards1) > 0 and len(cards2) > 0:
            # Check to see whether this card configuration has appeared in the
            # game before - if it has, player 1 wins.
            scores = (self.get_score(cards1), self.get_score(cards2))
            if scores in scores_to_date:
                return 1, self.get_score(cards1)
            else:
                scores_to_date.add(scores)

            c1 = cards1.popleft()
            c2 = cards2.popleft()

            if recursive and c1 <= len(cards1) and c2 <= len(cards2):
                # Truncate the cards to the value of the
                winner = self.play(deque(list(cards1)[0:c1]), deque(list(cards2)[0:c2]), True)[0]
            else:
                winner = (1 if c1 > c2 else 2)

            if winner == 1:
                cards1.extend([c1, c2])
            else:
                cards2.extend([c2, c1])

        if len(cards1) > 0:
            return 1, self.get_score(cards1)
        else:
            return 2, self.get_score(cards2)

    def calculate(self):
        sections = self.parser.get_sections()

        self.player1 = deque(map(lambda x: int(x), sections[0].split("\n")[1:]))
        self.player2 = deque(map(lambda x: int(x), sections[1].split("\n")[1:]))

    def part_1(self):
        return self.play(self.player1, self.player2, False)[1]

    def part_2(self):
        return self.play(self.player1, self.player2, True)[1]
