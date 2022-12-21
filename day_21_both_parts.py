ops = {"+" : float.__add__, "-" : float.__sub__, "*" : float.__mul__, "/" : float.__truediv__, "=" : float.__eq__}

with open("day_21.txt", "r") as file:
    data = [x.replace(":", "").split(" ") for x in file.read().splitlines()]
    monkeys = {}
    for monkey in data:
        if len(monkey) == 2:
            monkeys[monkey[0]] = lambda x=monkey[1]: float(x)
        else:
            monkeys[monkey[0]] = lambda x=monkey[2], y=monkey[1], z=monkey[3]: ops[x](monkeys[y](), monkeys[z]())
            if monkey[0] == "root":
                a, b = monkey[1], monkey[3]

    p1 = round(monkeys["root"]())

    start_x = monkeys[a]()
    start_y = monkeys[b]()

    start_value = monkeys["humn"]()
    end_value = max([start_x, start_y]) ** 2

    monkeys["humn"] = lambda x=end_value: float(x)

    end_x = monkeys[a]()
    end_y = monkeys[b]()

    relevant_start, relevant_end = next(((x, y) for x, y in [(start_x, end_x), (start_y, end_y)] if x != y))

    static = next((x for x in [start_x, start_y] if x != relevant_start))

    diff_end_and_start_values = abs(end_value - start_value)
    diff_relevant_end_and_start = abs(relevant_end - relevant_start)
    diff_start_values = abs(relevant_start - static)
    
    steps_per_increase = diff_relevant_end_and_start / diff_end_and_start_values

    print("Day 21: ", p1, round(diff_start_values / steps_per_increase + start_value))