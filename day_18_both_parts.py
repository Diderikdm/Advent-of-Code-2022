adj = lambda s, x, y, z: (a for a in ((x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)) if a not in s)

with open("day_18.txt", "r") as file:
    data = [tuple(int(y) for y in x.split(",")) for x in file.read().splitlines()]
    p1, p2 = 0, 0
    seen = set()
    for drop in data:
        for side in adj(seen, *drop):
            if side not in data:
                p1 += 1
    min_x, max_x = (x := sorted(x[0] for x in data))[0] - 1, x[-1] + 1
    min_y, max_y = (y := sorted(x[1] for x in data))[0] - 1, y[-1] + 1
    min_z, max_z = (z := sorted(x[2] for x in data))[0] - 1, y[-1] + 1
    queue = [(min_x, min_y, min_z)]
    p2 = 0
    while queue:
        x, y, z = queue.pop(0)
        if (x, y, z) not in seen:
            seen.add((x, y, z))
            for next_x, next_y, next_z in adj(seen, x, y, z):
                if min_x <= next_x <= max_x and min_y <= next_y <= max_y and min_z <= next_z <= max_z:
                    if (next_x, next_y, next_z) in data:
                        p2 += 1
                    else:
                        queue.append((next_x, next_y, next_z))
    print("day 18 : ", p1, p2)