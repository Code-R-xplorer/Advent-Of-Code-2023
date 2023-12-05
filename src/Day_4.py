from utils import read_file

values = read_file(4, str, False)


class ScratchCard:
    def __init__(self, ID, winningNumbers, cardNumbers):
        self.ID = ID
        self.winningNumbers = winningNumbers
        self.cardNumbers = cardNumbers

    def get_winners(self) -> int:
        return len(set(self.winningNumbers) & set(self.cardNumbers))


scratch_cards = []

for line in values:
    card, numbers = line.split(': ')
    cardID = int(card.split(' ').pop(-1))
    winning_numbers_string, card_numbers_string = numbers.split('| ')
    winning_numbers = winning_numbers_string.split(' ')
    winning_numbers = filter(None, winning_numbers)
    winning_numbers = [int(n) for n in winning_numbers]
    card_numbers = card_numbers_string.split(' ')
    card_numbers = filter(None, card_numbers)
    card_numbers = [int(n) for n in card_numbers]
    scratch_cards.append(ScratchCard(cardID, winning_numbers, card_numbers))

total_points = 0

for scratchCard in scratch_cards:
    card_total = 0

    if scratchCard.get_winners() > 0:
        card_total = 1

    for point in range(scratchCard.get_winners() - 1):
        card_total *= 2

    total_points += card_total

print(total_points)