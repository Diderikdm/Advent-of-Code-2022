adj = lambda s, x, y, z: (a for a in ((x - 1, y, z), (x + 1, y, z), (x, y - 1, z), (x, y + 1, z), (x, y, z - 1), (x, y, z + 1)) if a not in s)

with open("day_18.txt", "r") as file:
    data = [tuple(int(y) for y in x.split(",")) for x in file.read().splitlines()]
    p1, p2 = 0, 0
    seen = set()
    for drop in data:
        for side in adj(seen, *drop):
            if side not in data:
                p1 += 1
    min_x = min(x[0] - 1 for x in data)
    max_x = max(x[0] + 1 for x in data)
    min_y = min(x[1] - 1 for x in data)
    max_y = max(x[1] + 1 for x in data)
    min_z = min(x[2] - 1 for x in data)
    max_z = max(x[2] + 1 for x in data)
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