with open("day 08.txt", "r") as file:
    data = file.read().splitlines()
    length = len(data)
    width = len(data[0])
    vert_data = [[x[e] for x in data] for e in range(width)]
    p1 = 0
    p2 = 0
    for y in range(length):
        for x in range(width):
            current = int(data[y][x])
            if not all((
                        any(int(z) >= current for z in data[y][:x]),
                        any(int(z) >= current for z in data[y][x + 1:]),
                        any(int(z) >= current for z in vert_data[x][:y]),
                        any(int(z) >= current for z in vert_data[x][y + 1:])
            )):
                p1 += 1
            dirs = []
            for func in (lambda y, x: (y - 1, x), lambda y, x: (y + 1, x), lambda y, x: (y, x - 1), lambda y, x: (y, x + 1)):
                b, a = y, x
                s = 0
                while True:
                    b, a = func(b, a)
                    if (c := 0 <= b < length and 0 <= a < width):
                        s += 1
                    if not c or int(data[b][a]) >= current:
                        dirs.append(s)
                        break
            p2 = max(p2, dirs[0] * dirs[1] * dirs[2] * dirs[3])
    print(p1)
    print(p2)