with open("day 06.txt", "r") as file:
    data = file.read()
    for x in (4, 14):
        print(next((i for i in range(x, len(data) + 1) if len(set(data[i - x : i])) == x)))