def run(times, monkeys, inspect, use_mod):
    for _ in range(times):
        for e, monkey in monkeys.items():
            m = monkey["i"]
            while m:
                inspect[e] += 1
                item = m.pop(0)
                item = operation(item, monkey["op"])
                item = item // 3 if not use_mod else item % mod
                monkeys[test(item, monkey["bool"])]["i"].append(item)
    return sorted(inspect.values())[-2:]

with open("day_11.txt", "r") as file:
    data = file.read().split('\n\n')
    monkeys1, monkeys2 = {}, {}
    operation = lambda x, y: (x + (int(y[1]) if y[1].isdigit() else x)) if y[0] == "+" else (x * (int(y[1]) if y[1].isdigit() else x))
    test = lambda x, y: [y[1], y[0]][not x % y[2]]
    mod = 1
    for e, monkey in enumerate(data):
        monkey = monkey.splitlines()[1:]
        items = [int(x) for x in monkey[0].split(": ")[1].split(", ")]
        op = monkey[1].split(" ")[-2:]
        z = [int(monkey[3].split(" ")[-1]), int(monkey[4].split(" ")[-1]), int(monkey[2].split(" ")[-1])]
        mod *= z[-1]
        monkeys1[e] = {"i" : items, "op" : op, "bool" : z}
        monkeys2[e] = {"i" : items[:], "op" : op[:], "bool" : z[:]}
    p1 = run(20, monkeys1, {e : 0 for e in range(len(data))}, False)
    p2 = run(10000, monkeys2, {e : 0 for e in range(len(data))}, True)
    print("Day 11: ", p1[0] * p1[1], p2[0] * p2[1])
