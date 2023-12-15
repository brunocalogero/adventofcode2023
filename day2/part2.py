# 12 red; 13 green; 14 blue
# Look for all games that possibly have that config
# sum of the ids of the games

global_count = 0

def game_power_count(line: str) -> (int):
    red = 1
    green = 1
    blue = 1

    line_no_pref = line.split(': ', maxsplit=1)
    game = line_no_pref[1].strip()
    subsets = game.split('; ')
    for subset in subsets:
        subset_split = subset.split(', ')
        for num_col in subset_split:
            num_col_split = num_col.split(' ')
            if num_col_split[1] == 'red':
                if red < int(num_col_split[0]):
                    red = int(num_col_split[0])
            if num_col_split[1] == 'green':
                if green < int(num_col_split[0]):
                    green = int(num_col_split[0])
            if num_col_split[1] == 'blue':
                if blue < int(num_col_split[0]):
                    blue = int(num_col_split[0])
    return red * green * blue


if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        for idx, line in enumerate(file, start=1):
            striped_line = line.strip()
            global_count += game_power_count(striped_line)
    print(global_count)