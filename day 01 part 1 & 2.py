with open("day1.txt", "r") as file:
    data = [[int(y) for y in x.splitlines()] for x in file.read().split("\n\n")]
    print(max(sum(x) for x in data))
    print(sum(sorted(sum(x) for x in data)[-3:]))