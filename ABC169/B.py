"""

===================
tried-01:

improvement:
"""

# === tried-01 ===
_ = input()
nums = list(map(int, input().split()))
ans = 1

for num in nums:
    if num == 0 or ans <= 10 ** 18:
        ans *= num
    else:
        pass

print(ans if ans <= 10 ** 18 else -1)

# === improvement ===
