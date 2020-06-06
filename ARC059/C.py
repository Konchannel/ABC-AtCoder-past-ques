"""

===================
tried-01:

improvement:
"""

# === tried-01 ===
n = int(input())
ps = list(map(int, input().split()))

p_avg = round(sum(ps) / len(ps))

print(sum([abs(p - p_avg) ** 2 for p in ps]))

# === improvement ===
