with open("Day_25.txt", "r") as file:
    data = file.read().splitlines()
    total, i, five, snafu = 0, 1, 5, ""
    for x in data:
        for y in range(len(x), 0, -1):
            total += (five ** (y - 1)) * (int(x[index]) if x[(index := len(x) - y)].isdigit() else (-1 if x[index] == "-" else -2))
    while five ** i < total:
        i += 1
    for x in range(i - 1, -1, -1):
        trial = {}
        for y in range(2, -3, -1):
            trial[y] = (abs(total - (5 ** x * y)), (5 ** x * y))
        z = min(trial.items(), key=lambda a: a[1][0])
        snafu += (str(s) if (s := z[0]) >= 0 else ("-" if s == -1 else "="))
        total -= z[1][1]
    print("Day 25: ", snafu)