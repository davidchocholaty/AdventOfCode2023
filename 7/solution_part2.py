from functools import cmp_to_key

NUM_OF_CARDS = 5
LABELS = 'AKQT98765432J'


def get_hand_type(hand):
    sorted_hand = sorted(hand)

    count_of_symbol = [0] * NUM_OF_CARDS

    prev_card = sorted_hand[0]
    idx_symbols_list = 0

    joker_count = 0

    for card in sorted_hand:
        if card == 'J':
            joker_count = joker_count + 1
        else:

            if card != prev_card:
                idx_symbols_list = idx_symbols_list + 1

            count_of_symbol[idx_symbols_list] = count_of_symbol[idx_symbols_list] + 1
        prev_card = card

    count_of_symbol.sort(reverse=True)

    count_of_symbol[0] = count_of_symbol[0] + joker_count

    if count_of_symbol[0] == 5:
        return 6  # Five of a kind
    elif count_of_symbol[0] == 4:
        return 5  # Four of a king
    elif count_of_symbol[0] == 3:
        if count_of_symbol[1] == 2:
            return 4  # Full house
        else:
            return 3  # Three of a kind
    elif count_of_symbol[0] == 2:
        if count_of_symbol[1] == 2:
            return 2  # Two pair
        else:
            return 1  # One pair

    return 0  # High card


def compare(first_hand, first_hand_type, second_hand, second_hand_type):
    if first_hand_type == second_hand_type:
        if first_hand == second_hand:
            return 0
        for first_hand_card, second_hand_card in zip(first_hand, second_hand):
            first_hand_card_idx = LABELS.index(first_hand_card)
            second_hand_card_idx = LABELS.index(second_hand_card)

            if first_hand_card_idx < second_hand_card_idx:
                return 1
            if first_hand_card_idx > second_hand_card_idx:
                return -1

        return -1
    elif first_hand_type > second_hand_type:
        return 1
    return -1


def main():
    with open('input') as f:
        lines = f.readlines()
        hands_w_bids = [(line.split()[0], line.split()[1], -1) for line in lines]

        # Fill type pass.
        for i in range(len(hands_w_bids)):
            hands_w_bids[i] = (hands_w_bids[i][0], hands_w_bids[i][1], get_hand_type(hands_w_bids[i][0]))

        # Sort by type descendent.
        hands_w_bids.sort(key=lambda x: x[2], reverse=True)

        # Sort by comparisons.
        hands_w_bids = sorted(hands_w_bids, key=cmp_to_key(lambda x, y: compare(x[0], x[2], y[0], y[2])))

        # Calculate the result.
        result_value = 0

        for i in range(len(hands_w_bids), 0, -1):
            result_value = result_value + i * int(hands_w_bids[i-1][1])

        print('The result is: ' + str(result_value))


if __name__ == "__main__":
    main()
