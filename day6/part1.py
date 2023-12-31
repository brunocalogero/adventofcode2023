if __name__ == '__main__':
    with open('./day6/input.txt', 'r') as file:
        file_lines = []
        for line in file:
            file_lines.append(line)

        time_line_split = file_lines[0].split()
        distance_line_split = file_lines[1].split()
        times = [int(time_str) for time_str in time_line_split[1:]]
        distances = [int(dist_str) for dist_str in distance_line_split[1:]]

        records = []
        for idx, time in enumerate(times):
            record_race_count = 0
            for hold_time in range(1, time):
                dist = (time - hold_time) * hold_time
                if dist > distances[idx]:
                    record_race_count += 1
            records.append(record_race_count)

        error = 1
        for rec in records:
            error *= rec

        print(error)