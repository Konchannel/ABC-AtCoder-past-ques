"""

===================
tried-01:

improvement:
"""

# === tried-01 ===
n = int(input())
txt = input()

print(txt[:n]+"..." if bool(txt[n:]) else txt)

# === improvement ===
