from datetime import datetime

now = datetime.now()
import day_01_both_parts
d1 = datetime.now()
print(d1 - now, "\n-------------")
import day_02_both_parts
d2 = datetime.now()
print(d2 - d1, "\n-------------")
import day_03_both_parts
d3 = datetime.now()
print(d3 - d2, "\n-------------")
import day_04_both_parts
d4 = datetime.now()
print(d4 - d3, "\n-------------")
import day_05_both_parts
d5 = datetime.now()
print(d5 - d4, "\n-------------")
import day_06_both_parts
d6 = datetime.now()
print(d6 - d5, "\n-------------")
import day_07_both_parts
d7 = datetime.now()
print(d7 - d6, "\n-------------")
import day_08_both_parts
d8 = datetime.now()
print(d8 - d7, "\n-------------")

print("total: ", d8 - now) 