"""

===================
tried-01:

improvement:
"""

# === tried-01 ===
n, k = map(int, input().split())
ps = sorted(list(map(int, input().split())))

print(sum(ps[:k]))

# === improvement ===
