from typing import List, Tuple

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
        return None  # No common range



def compute_dest(dest_src_map, seed_source) -> List[int]:
    for k, v in dest_src_map.items():
        # check that seed range is in source range
        if seed_source[0] >= k and seed_source[1] <= (k + v[1] - 1):
            seed_vals = find_common_range((k, k + v[1] - 1), seed_source)
            # compute destination distance based on source distance
            if seed_vals != None:
                first_dest = v[0] + (seed_vals[0] - k)
                last_dest = v[0] + (seed_vals[1] - k)
                print(first_dest, last_dest)
                return (first_dest, last_dest)
    return seed_source


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

    # get location for each seed
    locations = []
    for seed_tuple in seed_list_tuple:
        dest = (0, 0)
        for idx, dest_src_map in enumerate(all_maps):
            if idx == 0:
                dest = compute_dest(dest_src_map, seed_tuple)
            else:
                # always return the range and then take the smallest dest before appending..
                dest = compute_dest(dest_src_map, dest)
        locations.append(min(dest))

    print(min(locations))