import math

class Day(object):
    def __init__(self, parser):
        self.parser = parser
        self.jokers_valid = True

    def remove_jokers(self, cards):
        if "J" in cards:
           j_count = cards["J"]
           del(cards["J"])
           if len(cards) == 0:
               # any card
               cards = {"A": 0}
           max_card = max(cards, key=cards.get)
           cards[max_card] += j_count
        return cards

    def hand_score(self, hand):
        score = 0

        # score based on card values
        for i, char in enumerate(hand[0][::-1]):
            score += math.pow(len(self.cards), i) * (len(self.cards) - self.cards.index(char))
        # score based on hand
        cards = {}
        for char in hand[0]:
            cards[char] =cards.get(char, 0) + 1

        if not self.jokers_valid:
            cards = self.remove_jokers(cards)

        card_counts = list(cards.values())
        card_counts.sort(reverse=True)
        for i, hand_type in enumerate([[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]):
            if card_counts == hand_type:
                score += math.pow(len(self.cards), 6) * i
                return score
        assert(False)

    def calculate(self):
        pass

    def get_score(self):
        hands = [(l.split()[0], l.split()[1]) for l in self.parser.get_lines()]
        hands.sort(key=self.hand_score)
        return sum((i+1)*int(bid) for i, (hand, bid) in enumerate(hands))


    def part_1(self):
        self.cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        return self.get_score()

    def part_2(self):
        self.cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
        return self.get_score()
