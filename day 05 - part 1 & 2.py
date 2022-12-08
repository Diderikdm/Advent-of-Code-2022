with open("day 05.txt", "r") as file:
    stack, data = file.read().split("\n\n")
    stack = stack.splitlines()[:-1][::-1]
    stack = [[x[e] for x in stack if x[e] != " "] for e in range(1, len(stack[0]), 4)]
    p1 = [x[:] for x in stack]
    p2 = [x[:] for x in stack]
    for row in data.splitlines():
        e, x, y = [int(x) for x in row.split(" ") if x.isdigit()]
        for z in range(e):
            p1[y - 1].append(p1[x - 1].pop(-1))
        for z in range(e, 0, -1):
            p2[y - 1].append(p2[x - 1].pop(-z))
    print(''.join([x[-1] for x in p1]))
    print(''.join([x[-1] for x in p2]))