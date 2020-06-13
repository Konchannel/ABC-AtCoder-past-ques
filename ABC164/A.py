"""
問題文
羊がS匹、狼がW匹います。
狼の数が羊の数以上のとき、羊は狼に襲われてしまいます。
羊が狼に襲われるなら unsafe、襲われないなら safe を出力してください。

制約
1≤S≤100
1≤W≤100

===================
tried-01:

improvement:
"""

# === tried-01 ===
s, w = map(int, input().split())
print('safe' if w < s else 'unsafe')

# === improvement ===
