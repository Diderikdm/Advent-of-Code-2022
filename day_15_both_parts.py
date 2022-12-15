def find(set_y, p2=False):
    x_ranges = set()
    for sensor, beacon in data:
        manhattan = sum(abs(a - b) for a, b in zip(sensor, beacon))
        if (man_y := abs(sensor[1] - set_y)) <= manhattan:
            x_ranges.add(tuple(sorted([sensor[0] - (man_x := manhattan - man_y), sensor[0] + man_x])))
    total_range = []
    beacons_in_y = sum([x[1] == set_y for x in beacons])
    ranges = sorted(x_ranges)
    start, end = ranges[0]
    for x, y in ranges[1:]:
        if x > end:
            total_range.append((start, end))
            start, end = x, y
            continue
        if y > end:
            end = y
    if (start, end) not in total_range:
        total_range.append((start, end))
    if not p2:
        return sum(abs(x[1] - x[0]) + 1 for x in total_range) - beacons_in_y
    else:
        if len(total_range) > 1:
            return (total_range[0][1] + 1) * 4000000 + set_y
        return None
        
with open("day_15.txt", "r") as file:
    set_y = 2000000
    data = [((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":")) for y in [2, 3, -2, -1]])[:2], z[2:]) for x in file.read().splitlines()]
    beacons = set(tuple(x[1]) for x in data)
    print(find(set_y))
    for y in range(4000000):
        if not y % 10000:
            print(y)
        if (result := find(y, True)):
            break
    print(result)
