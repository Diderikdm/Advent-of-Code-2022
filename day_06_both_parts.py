with open("day_06.txt", "r") as file:
    data = file.read()
    result = []
    for x in (4, 14):
        result.append(next((i for i in range(x, len(data) + 1) if len(set(data[i - x : i])) == x)))
    print("Day 6: ", result[0], result[1])