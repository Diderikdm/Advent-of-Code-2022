from heapq import heapify, heappop, heappush

def find_distances(start, data, interesting, queue, paths):
    heapify(queue)
    seen = set(start)
    while queue:
        steps, valve = heappop(queue)
        steps += 1
        for nxt in data[valve][1]:
            if nxt not in seen:
                seen.add(nxt)
                if nxt in interesting and nxt != start:
                    paths[nxt] = steps
                heappush(queue, [steps, nxt])
    return paths

def path_finder(data, distances, queue, part1=False, end=None):
    best = {}
    heapify(queue)
    while queue:
        time, release, p1, p2, seen = heappop(queue)
        if time == end + 1:
            break
        (time, valve), (time2, valve2) = (p1, p2) if part1 else sorted([p1, p2])
        if best.get((tup_seen := tuple(seen + [valve])), 1) > release:
            best[tup_seen] = release
            for k, v in distances[valve].items():
                if k not in seen and (next_time := time + v + 1) <= end:
                    next_release = release - (end - next_time) * data[k][0]
                    next_seen = sorted(seen + [k])
                    tup_seen = tuple(next_seen + [k])
                    if best.get(tup_seen, 1) > release:
                        best[tup_seen] = release
                        heappush(queue, [next_time, next_release, (next_time, k), (time2, valve2), next_seen])
    return -min(best.values())

with open("day_16.txt", "r") as file:
    data = {(z := x.split(" "))[1] : (int(z[4].strip("rate=").strip(";")), [y.strip(",") for y in z[9:]]) for x in file.read().splitlines()}
    interesting = set([k for k, v in data.items() if v[0] > 0] + ["AA"])
    distances = {x : find_distances(x, data, interesting, [tuple([0, x])], {}) for x in interesting}
    print("Day 16: ", path_finder(data, distances, (q := [(0, 0, (0, "AA"), (0, "AA"), ["AA"])])[:], part1=True, end=30), path_finder(data, distances, q[:], end=26))