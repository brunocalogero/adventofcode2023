if __name__ == '__main__':
    with open('./day6/input.txt', 'r') as file:
        file_lines = []
        for line in file:
            file_lines.append(line)

        time_line_split = file_lines[0].split()
        distance_line_split = file_lines[1].split()

        time = ''
        for time_str in time_line_split[1:]:
            time += time_str
        times = [int(time)]

        distance = ''
        for dist_str in distance_line_split[1:]:
            distance += dist_str
        distances = [int(distance)]

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