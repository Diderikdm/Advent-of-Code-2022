from datetime import datetime

with open("personal_stats.txt", "r") as file:
    times = {i : ["00:00:00"] for i in range(1, 26)}
    for x in file.read().splitlines():
        z = x.split()
        d = [y for y in z if ":" in y]
        delta = datetime.strptime(d[1], "%H:%M:%S") - datetime.strptime(d[0], "%H:%M:%S")
        times[next((int(y) for y in z if y))] = "Completion times leaderboard: " + str([y for y in z if ":" in y] + ["delta: " + str(delta)])

now = datetime.now()
import day_01_both_parts
d1 = datetime.now()
print("Runtime: ", d1 - now, "\n" + times[1], "\n-------------")
import day_02_both_parts
d2 = datetime.now()
print("Runtime: ", d2 - d1, "\n" + times[2], "\n-------------")
import day_03_both_parts
d3 = datetime.now()
print("Runtime: ", d3 - d2, "\n" + times[3], "\n-------------")
import day_04_both_parts
d4 = datetime.now()
print("Runtime: ", d4 - d3, "\n" + times[4], "\n-------------")
import day_05_both_parts
d5 = datetime.now()
print("Runtime: ", d5 - d4, "\n" + times[5], "\n-------------")
import day_06_both_parts
d6 = datetime.now()
print("Runtime: ", d6 - d5, "\n" + times[6], "\n-------------")
import day_07_both_parts
d7 = datetime.now()
print("Runtime: ", d7 - d6, "\n" + times[7], "\n-------------")
import day_08_both_parts
d8 = datetime.now()
print("Runtime: ", d8 - d7, "\n" + times[8], "\n-------------")
import day_09_both_parts
d9 = datetime.now()
print("Runtime: ", d9 - d8, "\n" + times[9], "\n-------------")
import day_10_both_parts
d10 = datetime.now()
print("Runtime: ", d10 - d9, "\n" + times[10], "\n-------------")
import day_11_both_parts
d11 = datetime.now()
print("Runtime: ", d11 - d10, "\n" + times[11], "\n-------------")
import day_12_both_parts
d12 = datetime.now()
print("Runtime: ", d12 - d11, "\n" + times[12], "\n-------------")
import day_13_both_parts
d13 = datetime.now()
print("Runtime: ", d13 - d12, "\n" + times[13], "\n-------------")
import day_14_both_parts
d14 = datetime.now()
print("Runtime: ", d14 - d13, "\n" + times[14], "\n-------------")
import day_15_both_parts
d15 = datetime.now()
print("Runtime: ", d15 - d14, "\n" + times[15], "\n-------------")
import day_16_both_parts
d16 = datetime.now()
print("Runtime: ", d16 - d15, "\n" + times[16], "\n-------------")
import day_17_both_parts
d17 = datetime.now()
print("Runtime: ", d17 - d16, "\n" + times[17], "\n-------------")
import day_18_both_parts
d18 = datetime.now()
print("Runtime: ", d18 - d17, "\n" + times[18], "\n-------------")
import day_19_both_parts
d19 = datetime.now()
print("Runtime: ", d19 - d18, "\n" + times[19], "\n-------------")
import day_20_both_parts
d20 = datetime.now()
print("Runtime: ", d20 - d19, "\n" + times[20], "\n-------------")
import day_21_both_parts
d21 = datetime.now()
print("Runtime: ", d21 - d20, "\n" + times[21], "\n-------------")
import day_22_both_parts
d22 = datetime.now()
print("Runtime: ", d22 - d21, "\n" + times[22], "\n-------------")
import day_23_both_parts
d23 = datetime.now()
print("Runtime: ", d23 - d22, "\n" + times[22], "\n-------------")
import day_24_both_parts
d24 = datetime.now()
print("Runtime: ", d24 - d23, "\n" + times[22], "\n-------------")
import day_25_both_parts
d25 = datetime.now()
print("Runtime: ", d25 - d24, "\n" + times[22], "\n-------------")

print("Total runtime:", d25 - now, "\n-------------") 
