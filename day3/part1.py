import copy
# NOTE: nth, number to coordinate mapping system?


global_count = 0
special_characters = "!@#$%^&*()-+?_=,<>/"

def get_adjacent_values(matrix, row, col):
    adjacent_values = []

    # Define relative positions of adjacent elements (including diagonals)
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0),  # Right, Down, Left, Up
        (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonals
    ]

    # Iterate over directions
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc

        # Check if the new coordinates are within bounds
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            adjacent_values.append(matrix[new_row][new_col])

    return adjacent_values


if __name__ == '__main__':
    with open('./day3/input.txt', 'r') as file:
        array_block = file.read()

    lines = array_block.strip().split('\n')
    two_dim_arr = [list(line) for line in lines]
    two_dim_arr_check = copy.deepcopy(two_dim_arr)

    # loop through two dimensional array
    for row in range(len(two_dim_arr)):
        for col in range(len(two_dim_arr[row])):
            # check if current character is a number
            if two_dim_arr[row][col].isdigit() and two_dim_arr_check[row][col] != 'x':
                num = ''
                adjacent_values = get_adjacent_values(two_dim_arr, row, col)
                # check if adjacent values are special characters
                for adjacent_value in adjacent_values:
                    if adjacent_value in special_characters:
                        # logic to retrieve the full number
                        # middle digit (there is a digit to the left and right)
                        if col + 1 < len(two_dim_arr[row]) and col - 1 >= 0:
                            if two_dim_arr[row][col + 1].isdigit() and two_dim_arr[row][col - 1].isdigit():
                                num = two_dim_arr[row][col - 1] + two_dim_arr[row][col] + two_dim_arr[row][col + 1]
                                # mark all as visited
                                modified_row = list(two_dim_arr_check[row])
                                modified_row[col] = 'x'
                                modified_row[col - 1] = 'x'
                                modified_row[col + 1] = 'x'
                                two_dim_arr_check[row] = ''.join(modified_row)
                        # leftmost digit
                        elif col + 2 < len(two_dim_arr[row]):
                            if two_dim_arr[row][col + 2].isdigit():
                                num = two_dim_arr[row][col] + two_dim_arr[row][col + 1] + two_dim_arr[row][col + 2]
                                # mark all as visited
                                modified_row = list(two_dim_arr_check[row])
                                modified_row[col] = 'x'
                                modified_row[col + 1] = 'x'
                                modified_row[col + 2] = 'x'
                                two_dim_arr_check[row] = ''.join(modified_row)
                        # left digit
                        elif col + 1 < len(two_dim_arr[row]):
                            if two_dim_arr[row][col + 1].isdigit():
                                num = two_dim_arr[row][col] + two_dim_arr[row][col + 1]
                                # mark all as visited
                                modified_row[col] = 'x'
                                modified_row[col + 1] = 'x'
                                two_dim_arr_check[row] = ''.join(modified_row)
                        # rightmost digit
                        elif col - 2 >= 0:
                            if two_dim_arr[row][col - 2].isdigit():
                                num = two_dim_arr[row][col - 2] + two_dim_arr[row][col - 1] + two_dim_arr[row][col]
                                # mark all as visited
                                modified_row = list(two_dim_arr_check[row])
                                modified_row[col - 2] = 'x'
                                modified_row[col - 1] = 'x'
                                modified_row[col] = 'x'
                                two_dim_arr_check[row] = ''.join(modified_row)
                        # right digit
                        elif col - 1 >= 0:
                            if two_dim_arr[row][col - 1].isdigit():
                                num = two_dim_arr[row][col - 1] + two_dim_arr[row][col]
                                # mark all as visited
                                modified_row = list(two_dim_arr_check[row])
                                modified_row[col - 1] = 'x'
                                modified_row[col] = 'x'
                                two_dim_arr_check[row] = ''.join(modified_row)
                        # single digit
                        else:
                            num = two_dim_arr[row][col]
                            # mark all as visited
                            modified_row = list(two_dim_arr_check[row])
                            modified_row[col] = 'x'
                            two_dim_arr_check[row] = ''.join(modified_row)

                if num != '':
                    global_count += int(num)
    print(global_count)