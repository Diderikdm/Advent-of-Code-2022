from heapq import heapify, heappop, heappush
from collections import defaultdict

adj = lambda g, x, y: (z for z in ((x, y), (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)) if z in g)

def path_finder(grid, start, ends, steps=0, p1=None):
    free = set(["."])
    best_for_coord = {}
    queue = [(steps, start)]
    end = ends.pop(0)
    heapify(queue)
    while queue:
        steps, current = heappop(queue)
        if current == end:
            p1 = p1 or steps
            if not ends:
                return p1, steps
            return path_finder(grid, end, ends, steps, p1)
        steps += 1
        for x, y in adj(grid, *current):
            if (x, y) in (start, end) or set([right[y][((-steps + (x - 1))) % w], 
                                              left[y][(steps + (x - 1)) % w], 
                                              up[x][(steps + (y - 1)) % h], 
                                              down[x][(-steps + (y - 1)) % h]]) == free:
                if best_for_coord.get((key := ((x,y), steps % w, steps % h)), steps + 1) > steps:
                    best_for_coord[key] = steps
                    heappush(queue, (steps, (x, y)))

with open("day_24.txt", "r") as file:
    data = file.read().splitlines()
    grid = {(x, y) : data[y][x] for x in range(len(data[0])) for y in range(len(data)) if data[y][x] != "#"}
    right, left, up, down = defaultdict(list), defaultdict(list), defaultdict(list), defaultdict(list)
    start, end = (s := sorted(grid, key=lambda x: x[1]))[0], s[-1]
    for y in range(start[1] + 1, end[1]):
        for x in range(start[0], end[0] + 1):
            point = grid[x, y]
            for direction, char, z in ((right, ">", y), (left, "<", y), (up, "^", x), (down, "v", x)):
                direction[z].append(point if point == char else ".")
    w, h = len(data[0]) - 2, len(data) - 2
    print("Day 24: ", path_finder(grid, start, [end, start, end]))