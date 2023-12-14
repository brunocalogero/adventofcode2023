import os


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
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def first_and_last(line: str) -> (str):
    first_idx = 0
    last_idx = 0

    if len(line) == 0:
        return '0'

    if len(line) == 1:
        if line[0] in digits_map:
            return line[0]

    for idx, char in enumerate(line):
        if char in digits_map:
            first_idx = idx
            break

    # I was cheeky here, can range with a negative step
    for idx2, char2 in enumerate(reversed(line)):
        if char2 in digits_map:
            # we need to use the original index here
            last_idx = len(line) - idx2 - 1
            break

    # check if same index for first and last
    if first_idx == last_idx:
        return line[first_idx] + line[first_idx]


    return line[first_idx] + line[last_idx]


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        for line in file:
            striped_line = line.strip()
            line_digit = first_and_last(striped_line)
            global_count += int(line_digit)
    print(global_count)