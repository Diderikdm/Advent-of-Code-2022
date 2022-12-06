with open("day 06.txt", "r") as file:
    data = file.read()
    for x in (3, 13):
        print(next((i + 1 for i in range(x, len(data) + 1) if len(set(data[i - x : i + 1])) == x + 1)))
    