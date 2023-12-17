from typing import TypedDict

gear_ratio_count: int = 0
special_character: str = "*"

def get_adjacent_gear_ratio(two_dim_arr: list[list[str]], row: list, col: list) -> int:
    adjacent_gear_values: list[str] = []
    local_gear_ratio: int = 1
    visited_coords: dict[tuple, bool] = {}

    # Define relative positions of adjacent elements (including diagonals)
    directions: list(tuple(int, int)) = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # Right, Down, Left, Up
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
    ]

    # Iterate over directions
    for dr, dc in directions:
        num: str = ''
        new_row, new_col = row + dr, col + dc

        # Check if the adjacent coordinates are within bounds
        if 0 <= new_row < len(two_dim_arr) and 0 <= new_col < len(two_dim_arr[0]):
            # Check if the adjacent value is a number and record it
            check = two_dim_arr[new_row][new_col]
            if two_dim_arr[new_row][new_col].isdigit():
                # leftmost digit
                if col + 2 < len(two_dim_arr[new_row]) and two_dim_arr[new_row][new_col + 1].isdigit() and two_dim_arr[new_row][new_col + 2].isdigit() and (new_row, new_col) not in visited_coords and (new_row, new_col + 1) not in visited_coords and (new_row, new_col + 2) not in visited_coords:
                    num = two_dim_arr[new_row][new_col] + two_dim_arr[new_row][new_col + 1] + two_dim_arr[new_row][new_col + 2]
                    visited_coords[(new_row, new_col)] = True
                    visited_coords[(new_row, new_col + 1)] = True
                    visited_coords[(new_row, new_col + 2)] = True
                # middle digit (there is a digit to the left and right)
                elif new_col + 1 < len(two_dim_arr[new_row]) and new_col - 1 >= 0 and two_dim_arr[new_row][new_col + 1].isdigit() and two_dim_arr[new_row][new_col - 1].isdigit() and (new_row, new_col) not in visited_coords and (new_row, new_col + 1) not in visited_coords and (new_row, new_col - 1) not in visited_coords:
                    num = two_dim_arr[new_row][new_col - 1] + two_dim_arr[new_row][new_col] + two_dim_arr[new_row][new_col + 1]
                    visited_coords[(new_row, new_col)] = True
                    visited_coords[(new_row, new_col - 1)] = True
                    visited_coords[(new_row, new_col + 1)] = True
                # rightmost digit
                elif new_col - 2 >= 0 and two_dim_arr[new_row][new_col - 2].isdigit() and two_dim_arr[new_row][new_col - 1].isdigit() and (new_row, new_col) not in visited_coords and (new_row, new_col - 2) not in visited_coords and (new_row, new_col - 1) not in visited_coords:
                    num = two_dim_arr[new_row][new_col - 2] + two_dim_arr[new_row][new_col - 1] + two_dim_arr[new_row][new_col]
                    visited_coords[(new_row, new_col)] = True
                    visited_coords[(new_row, new_col - 2)] = True
                    visited_coords[(new_row, new_col - 1)] = True
                # left digit
                elif new_col + 1 < len(two_dim_arr[new_row]) and two_dim_arr[new_row][new_col + 1].isdigit() and (new_row, new_col) not in visited_coords and (new_row, new_col + 1) not in visited_coords:
                    num = two_dim_arr[new_row][new_col] + two_dim_arr[new_row][new_col + 1]
                    visited_coords[(new_row, new_col)] = True
                    visited_coords[(new_row, new_col + 1)] = True
                # right digit
                elif new_col - 1 >= 0 and two_dim_arr[new_row][new_col - 1].isdigit() and (new_row, new_col) not in visited_coords and (new_row, new_col - 1) not in visited_coords:
                    num = two_dim_arr[new_row][new_col - 1] + two_dim_arr[new_row][new_col]
                    visited_coords[(new_row, new_col)] = True
                    visited_coords[(new_row, new_col - 1)] = True
                elif (new_row, new_col) not in visited_coords:
                    num = two_dim_arr[new_row][new_col]
                    visited_coords[(new_row, new_col)] = True
                if num != '':
                    adjacent_gear_values.append(num)

    # multiply all adjacent gear values
    if len(adjacent_gear_values) == 2:
        for adjacent_gear_value in adjacent_gear_values:
            local_gear_ratio *= int(adjacent_gear_value)

    if local_gear_ratio == 1:
        return 0

    return local_gear_ratio


if __name__ == '__main__':
    with open('./day3/input.txt', 'r') as file:
        array_block = file.read()

    lines = array_block.strip().split('\n')
    two_dim_arr = [list(line) for line in lines]

    # loop through two dimensional array
    for row in range(len(two_dim_arr)):
        for col in range(len(two_dim_arr[row])):
            if two_dim_arr[row][col] == special_character:
                # get adjacent vals
                local_gear_ratio = get_adjacent_gear_ratio(two_dim_arr, row, col)
                # add to global gear ratio
                gear_ratio_count += local_gear_ratio

    print(gear_ratio_count)