def compute_dest(dest_src_map, seed_source) -> int:
    for k, v in dest_src_map.items():
        # check destination in range for provided map
        if (seed_source >= k) and (seed_source <= k + v[1] - 1):
            # compute destination distance based on source distance
            diff = seed_source - k
            dest = v[0] + diff
            return dest
    return seed_source


if __name__ == '__main__':
    with open('./day5/input.txt', 'r') as file:
        array_block = file.read()
    lines = array_block.strip().split('\n\n')
    seed_str = lines[0]
    seed_list = [int(seed) for seed in seed_str.split(' ')[1:]]
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
    for seed in seed_list:
        dest = 0
        for idx, dest_src_map in enumerate(all_maps):
            if idx == 0:
                dest = compute_dest(dest_src_map, seed)
            else:
                dest = compute_dest(dest_src_map, dest)
        locations.append(dest)

    print(min(locations))