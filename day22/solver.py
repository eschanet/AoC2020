from functools import wraps
from datetime import datetime
from collections import deque
import copy

total_time = []


def measure_time(func):
    @wraps(func)
    def _func(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        total_time.append((end - start).total_seconds())
        return result

    return _func


class Deck:
    def __init__(self, cards):
        self.cards = deque(cards)
        self.history = [self.cards.copy()]

    def insert_at_bottom(self, cards, sort=True):
        sorted_cards = reversed(sorted(cards)) if sort else cards
        for card in sorted_cards:
            self.cards.appendleft(card)
        self.history.append(self.cards.copy())

    def get_card(self):
        return self.cards.pop()


@measure_time
def parse(raw_data):
    decks = raw_data.strip().split("\n\n")
    d1_cards, d2_cards = list(map(int, decks[0].split("\n")[1:])), list(
        map(int, decks[1].split("\n")[1:])
    )
    deck1 = Deck(reversed(d1_cards))
    deck2 = Deck(reversed(d2_cards))
    return (deck1, deck2)


# PART 1
@measure_time
def solve1(data):

    deck1, deck2 = copy.deepcopy(data[0]), copy.deepcopy(data[1])
    while len(deck1.cards) != 0 and len(deck2.cards) != 0:
        card1, card2 = deck1.get_card(), deck2.get_card()
        if card1 > card2:
            deck1.insert_at_bottom([card1, card2])
        else:
            deck2.insert_at_bottom([card1, card2])

    deck = deck1 if len(deck1.cards) > 0 else deck2

    return sum(card * (i + 1) for i, card in enumerate(list(deck.cards)))


# PART 2
@measure_time
def solve2(data):
    deck1, deck2, player_win = recursive_game(
        copy.deepcopy(data[0]), copy.deepcopy(data[1])
    )
    deck = deck1 if player_win == 1 else deck2
    return sum((i + 1) * card for i, card in enumerate(list(deck.cards)))


def recursive_game(deck1, deck2):
    while True:
        # check if one of the players has no cards left
        if len(deck1.cards) == 0:
            return deck1, deck2, 2
        if len(deck2.cards) == 0:
            return deck1, deck2, 1

        # else, get top card and have fun!
        card1 = deck1.get_card()
        card2 = deck2.get_card()

        # player 1(!) wins every time a given queue of cards already existed previously
        if deck1.cards in deck1.history[:-1]:
            return deck1, deck2, 1
        if deck2.cards in deck2.history[:-1]:
            return deck1, deck2, 1

        if card1 > len(deck1.cards) or card2 > len(deck2.cards):
            if card1 > card2:
                deck1.insert_at_bottom([card1, card2])
            else:
                deck2.insert_at_bottom([card1, card2])
        else:
            subdeck1 = Deck(list(deck1.cards)[-card1:].copy())
            subdeck2 = Deck(list(deck2.cards)[-card2:].copy())
            subdeck1, subdeck2, player_win = recursive_game(subdeck1, subdeck2)
            if player_win == 1:
                deck1.insert_at_bottom([card1, card2], False)
            else:
                deck2.insert_at_bottom([card2, card1], False)


if __name__ == "__main__":
    import sys

    data = parse(open("input.txt").read().strip())

    print("Part 1: {}".format(solve1(data)))
    print("Part 2: {}".format(solve2(data)))

    print("total time: {}s".format(sum(total_time)))
