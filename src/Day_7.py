from collections import Counter
from enum import Enum

from utils import read_file


class HandTypes(Enum):
    high_card = 1
    one_pair = 2
    two_pair = 3
    three_of_a_kind = 4
    full_house = 5
    four_of_a_kind = 6
    five_of_a_kind = 7


CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


class Hand:
    def __init__(self, cards):
        self.cards = list(cards)
        self.card_set = set(self.cards)
        self.card_counter = Counter(self.cards)
        self.value = self.get_value()

    def get_value(self):
        # Five Of a Kind
        if len(self.cards) == 1:
            return HandTypes.five_of_a_kind

        if len(self.cards) == 2:
            # Four of a Kind
            if any(c for c in self.card_counter.values() if c == 4):
                return HandTypes.four_of_a_kind

            # Full House
            has_three_of_a_kind = any(c for c in self.card_counter.values() if c == 3)
            has_two_pair = any(c for c in self.card_counter.values() if c == 2)
            if has_three_of_a_kind and has_two_pair:
                return HandTypes.full_house

        # Three of a kind
        if any(c for c in self.card_counter.values() if c == 3):
            return HandTypes.three_of_a_kind

        # Two Pair
        if len([c for c in self.card_counter.values() if c == 2]) == 2:
            return HandTypes.two_pair

        # One Pair
        if len([c for c in self.card_counter.values() if c == 2]) == 1:
            return HandTypes.one_pair

        return HandTypes.high_card

    def __gt__(self, other):
        print(self.value, other.value)
        if self != other:
            return self.value.value > other.value.value
        else:
            for i in range(len(self.cards)):
                card_value = CARD_VALUES[self.cards[i]]
                other_card_value = CARD_VALUES[other.cards[i]]
                print(card_value, other_card_value)
                if card_value == other_card_value:
                    continue
                else:
                    return card_value > other_card_value

    def __eq__(self, other):
        return self.value.value == other.value.value

    def __repr__(self):
        return f'<Hand: {"".join(self.cards)} {self.value}>'


lines = read_file(7, str, True)

hands = []

for line in lines:
    cards, bid = line.split(' ')
    bid = int(bid)
    hand = Hand(cards)
    hands.append((hand, bid))

print(hands[2][0] == hands[3][0])
# print(hands[2][0].value.value)
# print(hands[3][0].value.value)

total_winnings = 0
for count, (hand, bid) in enumerate(sorted(hands)):
    print(count, hand, bid)
    total_winnings += bid * count + 1

print(total_winnings)
