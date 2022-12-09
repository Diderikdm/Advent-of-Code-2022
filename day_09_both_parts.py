directions = {
    "R" : lambda x, y : (x + 1, y),
    "D" : lambda x, y : (x, y + 1),
    "L" : lambda x, y : (x - 1, y),
    "U" : lambda x, y : (x, y - 1)
}
with open("day_09.txt", "r") as file:
    data = (((y := x.split(" "))[0], int(y[1])) for x in file.read().splitlines())
    lst = [(0,0) for x in range(11)]
    prev_lst = [set() for x in range(11)]
    for direction, steps in data:
        for _ in range(steps):
            for e, z in enumerate(lst):
                if not e:
                    lst[e] = directions[direction](*lst[e])
                    prev_lst[e].add(lst[e])
                else:
                    x = lst[e - 1][0] - lst[e][0]
                    y = lst[e - 1][1] - lst[e][1]
                    if abs(x) > 1 or abs(y) > 1:
                        x //= abs(x or 1)
                        y //= abs(y or 1)
                        lst[e] = (lst[e][0] + x, lst[e][1] + y)
                    prev_lst[e].add(lst[e])
    print("day 9: ", len(prev_lst[1]), len(prev_lst[9]))