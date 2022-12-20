def find(data, shuffle, y, z):
    for _ in range(z):
        for x in data:
            if x[1] == 0:
                zero = x
            shuffle.pop(i := shuffle.index(x))
            shuffle.insert((i + x[1]) % y, x)
    zero = shuffle.index(zero)
    return sum(shuffle[zero + (x * 1000)][1] for x in [1, 2, 3])
    
with open("day_20.txt", "r") as file:
    p1 = list(enumerate(int(x) for x in file.read().splitlines()))
    p2 = [(x[0], x[1] * 811589153) for x in p1]
    print(find(p1, p1[:], len(p1) - 1, 1), find(p2, p2[:], len(p2) - 1, 10))