with open("day_02.txt", "r") as file:
    guide = {"A" : ["Y", "Z", "X"], "B" : ["Z", "X", "Y"], "C" : ["X", "Y", "Z"]}
    points = {"X" : 1, "Y" : 2, "Z" : 3}
    win_lose_draw_points = {0 : 6, 1 : 0, 2: 3}
    lose_draw_win = {"X" : 1, "Y": 2, "Z" : 0}
    data = [x.split(" ") for x in file.read().splitlines()]
    p1, p2 = 0, 0
    for e, (x, y) in enumerate(data):
        p1 += points[y] + win_lose_draw_points[guide[x].index(y)]
        p2 += win_lose_draw_points[lose_draw_win[y]] + points[guide[x][lose_draw_win[y]]]
    print("Day 2: ", p1, p2)