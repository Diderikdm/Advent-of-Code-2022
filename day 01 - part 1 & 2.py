with open("Advent-of-Code-2022\day01.txt", "r") as file:
    data = sorted(sum(int(y) for y in x.splitlines()) for x in file.read().split("\n\n"))
    print(data[-1])
    print(sum(data[-3:]))