with open("Advent-of-Code-2022\day1.txt", "r") as file:
    data = [[int(y) for y in x.splitlines()] for x in file.read().split("\n\n")]
    sorted_data = sorted(sum(x) for x in data)
    print(max(sorted_data))
    print(sum(sorted_data[-3:]))