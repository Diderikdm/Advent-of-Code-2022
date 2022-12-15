def line_intersect(Ax1, Ay1, Ax2, Ay2, Bx1, By1, Bx2, By2):
    if (d := (By2 - By1) * (Ax2 - Ax1) - (Bx2 - Bx1) * (Ay2 - Ay1)):
        if 0 <= (uA := ((Bx2 - Bx1) * (Ay1 - By1) - (By2 - By1) * (Ax1 - Bx1)) / d) <= 1 \
        and 0 <= (uB := ((Ax2 - Ax1) * (Ay1 - By1) - (Ay2 - Ay1) * (Ax1 - Bx1)) / d) <= 1:
            return int(Ax1 + uA * (Ax2 - Ax1)), int(Ay1 + uA * (Ay2 - Ay1))
    
def find(set_y):
    x_ranges = set()
    m, wn, ws, ne, se = [], [], [], [], []
    for sensor, beacon in data:
        m.append((manhattan := sum(abs(a - b) for a, b in zip(sensor, beacon))))
        wn.append(((w := (sensor[0] - manhattan - 1, sensor[1])), (n := (sensor[0], sensor[1] - manhattan - 1))))
        ws.append((w, (s := (sensor[0], sensor[1] + manhattan + 1))))
        ne.append((n, (e := (sensor[0] + manhattan + 1, sensor[1]))))
        se.append((s, e))
        if (man_y := abs(sensor[1] - set_y)) <= manhattan:
            x_ranges.add((sensor[0] - (man_x := manhattan - man_y), sensor[0] + man_x))
    total_range = []
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
    return m, wn, ws, ne, se, sum(abs(x[1] - x[0]) + 1 for x in total_range) - sum([x[1] == set_y for x in beacons])
        
with open("day_15.txt", "r") as file:
    set_y = 2000000
    data = [((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":")) for y in [2, 3, -2, -1]])[:2], z[2:]) for x in file.read().splitlines()]
    beacons = set(tuple(x[1]) for x in data)
    m, wn, ws, ne, se, p1 = find(set_y)
    points = set()
    p2 = None
    while not p2:
        for a, b in wn + se:
            for c, d in ws + ne:
                if (hit := line_intersect(*a, *b, *c, *d)) and 0 <= min(hit) and max(hit) <= 4000000:
                    for e, (sensor, beacon) in enumerate(data):
                        if sum(abs(a - b) for a, b in zip(sensor, hit)) <= m[e]:
                            break
                    else:
                        p2 = hit[0] * 4000000 + hit[1]
    print("day 15: ", p1, p2)