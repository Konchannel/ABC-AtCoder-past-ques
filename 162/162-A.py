"""
問題文
3桁の整数Nが与えられます。
Nのいずれかの桁に数字の7は含まれますか？
含まれるなら Yes を、含まれないなら No を出力してください。

制約
100≤N≤999
===================
tried-01:

improvement:
"""

# === tried-01 ===
ns = list(map(int, input()))
print('Yes' if 7 in ns else 'No')

# === improvement ===
