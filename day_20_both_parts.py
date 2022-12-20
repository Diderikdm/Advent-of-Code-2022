def find(data, shuffle, y):
    for x in data:
        shuffle.insert(((i := shuffle.index(x)) + x[1]) % y, shuffle.pop(i))
    zero = next((e for e, x in enumerate(shuffle) if x[1] == 0))
    return sum(shuffle[(zero + (x * 1000)) % (y + 1)][1] for x in [1, 2, 3])

with open("day_20.txt", "r") as file:
    p1 = list(enumerate(int(x) for x in file.read().splitlines()))
    p2 = [(x[0], x[1] * 811589153) for x in p1]
    print("day 20 :", find(p1, p1[:], len(p1) - 1), find(p2 * 10, p2[:], len(p2) - 1))