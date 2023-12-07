from dataclasses import dataclass

values_part1 = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
values_part2 = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, 'J': 1}

def repeatedCards(card, cards):
    return len([c for c in cards if c == card])

def getType(cards):
    highest_number = 0
    last_cards = ''
    for card in cards:
        if card not in last_cards:
            num = repeatedCards(card, cards)
            highest_number = num if highest_number < num else highest_number
            last_cards += card
    n_different_cards = len(last_cards)
    if n_different_cards == 5:
        return 0
    elif n_different_cards == 4:
        return 1
    elif n_different_cards == 3 and highest_number == 2:
        return 2
    elif n_different_cards == 3 and highest_number == 3:
        return 3
    elif n_different_cards == 2 and highest_number == 3:
        return 4
    elif n_different_cards == 2 and highest_number == 4:
        return 5
    elif n_different_cards == 1:
        return 6
    
def getTypePart2(cards):
    highest_number = 0
    last_cards = ''
    n_js = 0
    for card in cards:
        if card == 'J':
            n_js += 1
        if card not in last_cards and card != 'J': # J not included because it is every number at once
            num = repeatedCards(card, cards)
            highest_number = num if highest_number < num else highest_number
            last_cards += card
    n_different_cards = len(last_cards)
    highest_number += n_js
    if n_different_cards == 5:
        return 0, n_js
    elif n_different_cards == 4:
        return 1, n_js
    elif n_different_cards == 3 and highest_number == 2:
        return 2, n_js
    elif n_different_cards == 3 and highest_number == 3:
        return 3, n_js
    elif n_different_cards == 2 and highest_number == 3:
        return 4, n_js
    elif n_different_cards == 2 and highest_number == 4:
        return 5, n_js
    elif n_different_cards == 1:
        return 6, n_js
    elif n_different_cards == 0:
        return 6, n_js
    
    
def compareHands(self_hand, other_hand):
    ret = False
    if self_hand.type < other_hand.type:
        ret = True
        return ret
    if self_hand.type == other_hand.type:
        for i, card in enumerate(self_hand.cards):
            if card < other_hand.cards[i]:
                ret = True
                break
            if card > other_hand.cards[i]:
                break
    return ret

# I thought the number of J's was determinant to calculate if a hand was lower LOL wtf xD
        
@dataclass
class Hand:
    cards: list[int]
    type: int
    bid: int
    js: int

    def __lt__(self, other_hand):
        return compareHands(self, other_hand)


def readLines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


if __name__ == "__main__":
    lines = readLines("input.txt")
    hand_list = []
    for line in lines:
        hand_str = line.split()[0]
        hand_list.append(Hand([int(hand) if hand.isnumeric() else values_part1[hand] for hand in hand_str], getType(hand_str), int(line.split()[1]), 0))

    hand_list_sorted = sorted(hand_list)
    result = 0
    for i, hand in enumerate(hand_list_sorted):
        result += (i+1)*hand.bid
    print(f"part1: {result}")
    hand_list = []
    for line in lines:
        hand_str = line.split()[0]
        card_type, js = getTypePart2(hand_str)
        hand_list.append(Hand([int(hand) if hand.isnumeric() else values_part2[hand] for hand in hand_str], card_type, int(line.split()[1]), js))

    hand_list_sorted = sorted(hand_list)
    result = 0
    for i, hand in enumerate(hand_list_sorted):
        result += (i+1)*hand.bid
    print(f"part2: {result}")
