with open("Advent-of-Code-2022\day02.txt", "r") as file:
    guide = {"A" : ["Y", "Z", "X"], "B" : ["Z", "X", "Y"], "C" : ["X", "Y", "Z"]}
    points = {"X" : 1, "Y" : 2, "Z" : 3}
    win_lose_draw_points = {0 : 6, 1 : 0, 2: 3}
    lose_draw_win = {"X" : 1, "Y": 2, "Z" : 0}
    data = [x.split(" ") for x in file.read().splitlines()]
    score = 0
    score_two = 0
    for e, (x, y) in enumerate(data):
        score += points[y] + win_lose_draw_points[guide[x].index(y)]
        score_two += win_lose_draw_points[lose_draw_win[y]] + points[guide[x][lose_draw_win[y]]]
    print(score)
    print(score_two)