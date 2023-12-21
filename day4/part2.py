# win more scratchcards equal to the number of winning numbers you have.
# you win copies of the scratchcards below the winning card equal to the number of matches
# 10 were to have 5 matching -> cards 11, 12, 13, 14, and 15.


card_to_card_copies: dict[int, list[int]] = {}

def recursion(array, rec_count) -> int:
    # if rec_count == len(card_to_card_copies):
    #     return rec_count

    for item in array:
        rec_count = recursion(card_to_card_copies[item], rec_count + 1)
    return rec_count

with open('./day4/input.txt', 'r') as file:
    for idx, card in enumerate(file):
        # for each card get winning numbers and our numbers
        card_split = card.strip().split(' ')
        card_numbers = []
        for val in card_split:
            if val.isdigit():
                card_numbers.append(int(val))

        winning_numbers = card_numbers[:10]
        our_numbers = card_numbers[10:]

        card_copies = []
        card_idx_counter = idx + 1
        for num in our_numbers:
            if num in winning_numbers:
                card_idx_counter += 1
                card_copies.append(card_idx_counter)

        # build card id to card copies ids dict
        if len(card_copies) == 0:
            card_to_card_copies[idx + 1] = []
        else:
            card_to_card_copies[idx + 1] = card_copies

    count = 0
    for og_card_id, card_copy_ids in card_to_card_copies.items():
        rec_count = recursion(card_copy_ids, 0)
        count += rec_count
    print(count + len(card_to_card_copies))




