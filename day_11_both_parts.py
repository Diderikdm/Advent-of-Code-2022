def run(times, monkeys, inspect, div_or_mod, val_div_or_mod):
    for _ in range(times):
        for e, monkey in monkeys.items():
            m = monkey["i"]
            x, y, z = monkey["bool"]
            op, a = monkey["op"]
            lst = [y, x]
            while m:
                inspect[e] += 1
                item = div_or_mod(op((i := m.pop(0)), a or i), val_div_or_mod)
                monkeys[lst[not item % z]]["i"].append(item)
    return sorted(inspect.values())[-2:]

with open("day_11.txt", "r") as file:
    data = file.read().split('\n\n')
    monkeys1, monkeys2 = {}, {}
    mod = 1
    for e, monkey in enumerate(data):
        monkey = monkey.splitlines()[1:]
        items = [int(x) for x in monkey[0].split(": ")[1].split(", ")]
        operation = monkey[1].split(" ")[-2:]
        val = int(operation[1]) if operation[1].isdigit() else None
        op = [int.__add__ if operation[0] == "+" else int.__mul__, val]
        z = [int(monkey[3].split(" ")[-1]), int(monkey[4].split(" ")[-1]), int(monkey[2].split(" ")[-1])]
        mod *= z[-1]
        monkeys1[e] = {"i" : items, "op" : op, "bool" : z}
        monkeys2[e] = {"i" : items[:], "op" : op[:], "bool" : z[:]}
    p1 = run(20, monkeys1, {e : 0 for e in range(len(data))}, int.__floordiv__, 3)
    p2 = run(10000, monkeys2, {e : 0 for e in range(len(data))}, int.__mod__, mod)
    print("Day 11: ", p1[0] * p1[1], p2[0] * p2[1])