# 12 red; 13 green; 14 blue
# Look for all games that possibly have that config
# sum of the ids of the games

global_count = 0

def is_game_valid(line: str) -> (bool):
    line_no_pref = line.split(': ', maxsplit=1)
    game = line_no_pref[1].strip()
    subsets = game.split('; ')
    for subset in subsets:
        subset_split = subset.split(', ')
        for num_col in subset_split:
            num_col_split = num_col.split(' ')
            if num_col_split[1] == 'red' and int(num_col_split[0]) > 12:
                return False
            if num_col_split[1] == 'green' and int(num_col_split[0]) > 13:
                return False
            if num_col_split[1] == 'blue' and int(num_col_split[0]) > 14:
                return False
    return True



if __name__ == '__main__':
    with open('./input.txt', 'r') as file:
        for idx, line in enumerate(file, start=1):
            striped_line = line.strip()
            if is_game_valid(striped_line):
                global_count += idx
    print(global_count)