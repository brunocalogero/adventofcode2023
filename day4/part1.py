
win_count = 0

if __name__ == '__main__':
    with open('./day4/input.txt', 'r') as file:
        for card in file:
            # for each card get winning numbers and our numbers
            card_split = card.strip().split(' ')
            card_numbers = []
            for val in card_split:
                if val.isdigit():
                    card_numbers.append(int(val))

            winning_numbers = card_numbers[:10]
            our_numbers = card_numbers[10:]

            our_winning_numbers = []
            for num in our_numbers:
                if num in winning_numbers:
                    our_winning_numbers.append(num)

            # 2 ** n - 1
            if len(our_winning_numbers) == 0:
                continue

            win_count += (2 ** (len(our_winning_numbers) - 1))
    print(win_count)