from collections import defaultdict

adj = {
    "N" : lambda x, y: (x, y - 1),
    "NE": lambda x, y: (x + 1, y - 1),
    "E" : lambda x, y: (x + 1, y),
    "SE": lambda x, y: (x + 1, y + 1),
    "S" : lambda x, y: (x, y + 1),
    "SW": lambda x, y: (x - 1, y + 1),
    "W" : lambda x, y: (x - 1, y),
    "NW": lambda x, y: (x - 1, y - 1)
}

directions = [
    lambda e, x, y: adj["N"](x, y) if not any(z in e for z in (adj[d](x, y) for d in ["NW", "N", "NE"])) else None,
    lambda e, x, y: adj["S"](x, y) if not any(z in e for z in (adj[d](x, y) for d in ["SW", "S", "SE"])) else None,
    lambda e, x, y: adj["W"](x, y) if not any(z in e for z in (adj[d](x, y) for d in ["NW", "W", "SW"])) else None,
    lambda e, x, y: adj["E"](x, y) if not any(z in e for z in (adj[d](x, y) for d in ["NE", "E", "SE"])) else None
]

with open("Day_23.txt", "r") as file:
    data = file.read().splitlines()
    elves = set((x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "#")
    direction = -1
    i = 0
    while True:
        copy = set(elves)
        direction = (direction + 1) % 4
        proposed_moves = defaultdict(list)
        for elf in elves:
            if any(z in elves for z in (adj[x](*elf) for x in adj)):
                for trial in range(direction, direction + 4):
                    if (move := directions[trial % 4](elves, *elf)):
                        proposed_moves[move].append(elf)
                        break
        for move, moving in proposed_moves.items():
            if len(moving) == 1:
                elves.remove(moving[0])
                elves.add(move)
        if i == 9:
            p1 = (max(x[0] for x in elves) + 1 - min(x[0] for x in elves)) * (max(x[1] for x in elves) + 1 - min(x[1] for x in elves)) - len(elves)
        elif elves == copy:
            break
        i += 1
    print("Day 23: ", p1, i + 1)