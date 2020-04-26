"""
問題文
くじ引きをN回行い、
i回目には種類が文字列
Siで表される景品を手に入れました。
何種類の景品を手に入れましたか？

制約
1≤N≤2×10^5
Siは英小文字のみからなり、長さは1以上10以下

===================
tried-01:

improvement:
"""

# === tried-01 ===
n = int(input())
sets = set()

for i in range(n):
    sets.add(input())

print(len(sets))

# === improvement ===
