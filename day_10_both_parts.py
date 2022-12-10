with open("day_10.txt", "r") as file:
    data = file.read().splitlines()
    c, p1, add_flag, reg_x = 0, 0, 0, 1
    image = ''
    sprite = [reg_x - 1, reg_x, reg_x + 1]
    while data:
        image += "#" if c % 40 in sprite else " "
        p1 += reg_x * c if c < 221 and c % 40 and not c % 20 else 0
        if not add_flag:
            current = data.pop(0)
            if current.startswith("addx"):
                val = int(current.split(" ")[-1])
                add_flag = 1
        else:
            reg_x += int(val)
            sprite = [reg_x - 1, reg_x, reg_x + 1]
            add_flag = 0
        c += 1
    print("day 10: ", p1, "\n", '\n'.join([image[x:x + 40] for x in range(0, len(image), 40)]))     