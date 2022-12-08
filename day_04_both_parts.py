with open("day_04.txt", "r") as file:
    data = file.read().splitlines()
    p1, p2 = 0, 0
    for row in data:
        rng = []
        a, b = row.split(",")
        for z in [a, b]:
            c, d = z.split("-")
            rng.append(list(range(int(c), int(d) + 1)))
        if any(min(rng[x]) <= min(rng[y]) and max(rng[x]) >= max(rng[y]) for x, y in ((0,1), (1,0))):
            p1 += 1
        if set(rng[0]) & set(rng[1]):
            p2 += 1
    print("day 4: ", p1, p2)