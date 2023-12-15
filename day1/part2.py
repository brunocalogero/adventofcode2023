import os
from collections import OrderedDict

global_count = 0
digits_map = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}
digit_char_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def first_and_last(line: str) -> (str):
    first_idx = 0
    last_idx = 0
    first_letter_digit_idx = 0
    last_letter_digit_idx = 0
    found_digit_chars = OrderedDict()

    if len(line) == 0:
        return '0'

    if len(line) == 1:
        if line[0] in digits_map:
            return line[0]

    # Find indexes of first and last digits
    for idx, char in enumerate(line):
        if char in digits_map:
            first_idx = idx
            break

    # NOTE: I was cheeky here, can range with a negative step (this is more idiomatic/pythonic though)
    for idx2, char2 in enumerate(reversed(line)):
        if char2 in digits_map:
            # we need to use the original index here
            last_idx = len(line) - idx2 - 1
            break


    # Find indexes of first and last letter digits
    # TODO: add to other for loop? (more efficient)
    # TODO: make more pythonic with a has-prefix utility?
    # NOTE: off by 1 error here was the most challenging thing
    for idx in range(0, len(line) - 1):
        if (idx + 3 <= len(line)) and line[idx:idx+3] in digit_char_map:
            found_digit_chars[idx] = line[idx:idx+3]
        if (idx + 4 <= len(line)) and line[idx:idx+4] in digit_char_map:
            found_digit_chars[idx] = line[idx:idx+4]
        if (idx + 5 <= len(line)) and line[idx:idx+5] in digit_char_map:
            found_digit_chars[idx] = line[idx:idx+5]

    # Compare indexes of first and last digits with first and last letter digits
    if len(found_digit_chars) > 0:

        if len(found_digit_chars) == 1 and len(found_digit_chars) == len(line):
            first_found_chars = next(iter(found_digit_chars))
            return digit_char_map[first_found_chars] + digit_char_map[first_found_chars]


        first_letter_digit_idx = next(iter(found_digit_chars))
        last_letter_digit_idx = next(reversed(found_digit_chars))

        if first_letter_digit_idx < first_idx and last_letter_digit_idx > last_idx:
            first_found_chars = found_digit_chars[first_letter_digit_idx]
            last_found_chars = found_digit_chars[last_letter_digit_idx]
            return digit_char_map[first_found_chars] + digit_char_map[last_found_chars]

        if first_letter_digit_idx < first_idx and last_letter_digit_idx < last_idx:
            first_found_chars = found_digit_chars[first_letter_digit_idx]
            return digit_char_map[first_found_chars] + line[last_idx]

        if first_letter_digit_idx > first_idx and last_letter_digit_idx > last_idx:
            last_found_chars = found_digit_chars[last_letter_digit_idx]
            return line[first_idx] + digit_char_map[last_found_chars]

        if first_letter_digit_idx > first_idx and last_letter_digit_idx < last_idx:
            return line[first_idx] + line[last_idx]



    # NOTE: check if same index for first and last
    if first_idx == last_idx:
        return line[first_idx] + line[first_idx]


    return line[first_idx] + line[last_idx]


if __name__ == '__main__':
    with open('./day1/input.txt', 'r') as file:
        for line in file:
            striped_line = line.strip()
            line_digit = first_and_last(striped_line)
            global_count += int(line_digit)
    print(global_count)