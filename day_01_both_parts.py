with open("day_01.txt", "r") as file:
    data = [[int(y) for y in x.splitlines()] for x in file.read().split("\n\n")]
    sorted_data = sorted(sum(x) for x in data)
    print("day 1: ", max(sorted_data), sum(sorted_data[-3:]))