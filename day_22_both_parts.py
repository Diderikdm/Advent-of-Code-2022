directions = {
    0 : lambda g, d, s, j, x, y : (d, z) if (z := (x + 1, y)) in g else (j[divmod(z[0], s), z[1] // s](s, x, y) if j else (d, min(g, key=lambda a: (abs(a[1] - y), a[0])))),
    1 : lambda g, d, s, j, x, y : (d, z) if (z := (x, y + 1)) in g else (j[z[0] // s, divmod(z[1], s)](s, x, y) if j else (d, min(g, key=lambda a: (abs(a[0] - x), a[1])))),
    2 : lambda g, d, s, j, x, y : (d, z) if (z := (x - 1, y)) in g else (j[divmod(z[0], s), z[1] // s](s, x, y) if j else (d, min(g, key=lambda a: (abs(a[1] - y), -a[0])))),
    3 : lambda g, d, s, j, x, y : (d, z) if (z := (x, y - 1)) in g else (j[z[0] // s, divmod(z[1], s)](s, x, y) if j else (d, min(g, key=lambda a: (abs(a[0] - x), -a[1]))))
}

get_jumps = lambda size : {
    ((3, 0), 0) :           lambda s, x, y : (2, (2 * s - 1, (3 * s) - 1 - y)),             #A to H  
    (2, (-1, size - 1)) :   lambda s, x, y : (3, (x % s, (4 * s) - 1)),                     #D to M            ------ ------
    (2, (1, 0)) :           lambda s, x, y : (2, ((s * 2) - 1, s + (x % s))),               #E to F           |   B  |  D   |
    (1, (-1, size - 1)) :   lambda s, x, y : (0, (0, (s * 3) + (x % s))),                   #B to N           |C     |  E  A|
    ((0, size - 1), 0) :    lambda s, x, y : (0, (0, (s * 3) - 1 - y)),                     #C to K            ------ ------
    ((0, size - 1), 1) :    lambda s, x, y : (1, ((y % s), s * 2)),                         #G to J           |     F|
    ((2, 0), 1) :           lambda s, x, y : (3, ((s * 2) + (y % s), s - 1)),               #F to E           |G     |
    (0, (1, size - 1)) :    lambda s, x, y : (0, (s, s + x)),                               #J to G     ------ ------
    ((-1, size - 1), 2) :   lambda s, x, y : (0, (s, s - 1 - (y % s))),                     #K to C    |   J  |     H|
    ((-1, size - 1), 3) :   lambda s, x, y : (1, (s + y % s, 0)),                           #N to B    |K     |  I   |
    (0, (4, 0)) :           lambda s, x, y : (1, (s * 2 + x, 0)),                           #M to D     ------ ------   
    ((1, 0), 3) :           lambda s, x, y : (3, (s + (y % s), s * 3 - 1)),                 #L to I    |N    L|
    (1, (3, 0)) :           lambda s, x, y : (2, (s - 1, s * 3 + (x % s))),                 #I to L    |   M  |
    ((2, 0), 2) :           lambda s, x, y : (2, (s * 3 - 1, s - 1 - (y % s)))              #H to A     ------
}

def walk(instructions, grid, direction, size, current, jump=None):
    while instructions:
        instruction = instructions[:(i := next((e for e, x in enumerate(instructions) if x.isalpha()), len(instructions))) + 1]
        instructions = instructions[i + 1:]
        steps, turn = '', ''
        for x in instruction:
            steps, turn = (steps + x, turn) if x.isdigit() else (steps, x)
        if steps:
            for _ in range(int(steps)):
                if grid[(nxt := directions[direction](grid, direction, size, jump, *current))[1]] != "#":
                    direction, current = nxt
                else:
                    break
        if turn:
            direction = (direction + (1 if turn == "R" else -1)) % 4
    return 1000 * (current[1] + 1) + 4 * (current[0] + 1) + next((e for e, x in enumerate(directions) if direction == x))

with open("Day_22.txt", "r") as file:
    data, instructions = file.read().split("\n\n")
    data = data.splitlines()
    size = min(len(x.replace(" ", "")) for x in data)
    grid = {(x, y) : data[y][x] for x in range(max(len(x) for x in data)) for y in range(len(data)) if x < len(data[y]) and data[y][x] != " "}
    current = min(grid, key=lambda x: (x[1], x[0]))
    print("day 22: ", walk(instructions[:], grid, 0, size, current), walk(instructions[:], grid, 0, size, current, get_jumps(size)))