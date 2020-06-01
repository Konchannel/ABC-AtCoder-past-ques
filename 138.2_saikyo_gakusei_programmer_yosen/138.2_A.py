"""

===================
tried-01:

improvement:
"""

# === tried-01 ===
m, d = map(int, input().split())
count = 0

for i in range(2, m+1):
    for j in range(20, d+1):
        dt, do = divmod(j, 10)
        if 1 < do and dt * do == i:
            count += 1

print(count)

# === improvement ===
