from typing import List, Tuple
from itertools import chain

def generate_ranges_from_seed_numbers(seed_numbers: List[int]) -> List[Tuple[int, int]]:
    ranges = []

    for i in range(0, len(seed_numbers), 2):
        start_seed = seed_numbers[i]

        if i + 1 < len(seed_numbers):
            num_values = seed_numbers[i + 1]
            end_seed = start_seed + num_values - 1
            ranges.append((start_seed, end_seed))

    return ranges

def find_common_range(range1, range2):
    # Find the common range
    common_start = max(range1[0], range2[0])
    common_end = min(range1[1], range2[1])

    # Check if there is a valid common range
    if common_start <= common_end:
        return common_start, common_end
    else:
        return None


def compute_dest(dest_src_map, seed_source) -> List[Tuple[int, int]]:
    dest_ranges = []
    for k, v in dest_src_map.items():
        if seed_source[1] > k:
            seed_vals = find_common_range((k, k + v[1] - 1), seed_source)
            if seed_vals != None:
                first_dest = v[0] + (seed_vals[0] - k)
                last_dest = v[0] + (seed_vals[1] - k)
                dest_ranges.append((first_dest, last_dest))
    if len(dest_ranges) > 0:
        return dest_ranges
    return [seed_source]


if __name__ == '__main__':
    with open('./day5/input.txt', 'r') as file:
        array_block = file.read()
    lines = array_block.strip().split('\n\n')
    seed_range_str = lines[0]
    seed_range_list = [int(seed) for seed in seed_range_str.split(' ')[1:]]
    seed_list_tuple = generate_ranges_from_seed_numbers(seed_range_list)

    destination_maps_str = lines[1:]

    # create an array of all source-destination maps (in order).
    all_maps = []
    for dest_map_str in destination_maps_str:
        computed_map = {}
        dest_map_split = dest_map_str.split('\n')[1:]
        for source_dest_range_str in dest_map_split:
            source_dest_range = source_dest_range_str.split(' ')
            computed_map[int(source_dest_range[1])] = (int(source_dest_range[0]), int(source_dest_range[2]))
        all_maps.append(computed_map)

    locations = []
    for seed_tuple in seed_list_tuple:
        dests = []
        for idx, dest_src_map in enumerate(all_maps):
            if idx == 0:
                dests = compute_dest(dest_src_map, seed_tuple)
            else:
                dests_temp = []
                for dest in dests:
                    dests_temp.append(compute_dest(dest_src_map, dest))
                dests = list(chain(*dests_temp))
        first_dests = [dest_tuple[0] for dest_tuple in dests]
        locations.append(min(first_dests))
    print(min(locations))