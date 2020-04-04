"""
問題文
青木君は任意の整数 xに対し、以下の操作を行うことができます。

操作:
xをxとKの差の絶対値で置き換える。

整数Nの初期値が与えられます。
この整数に上記の操作を0回以上好きな回数行った時にとりうるNの最小値を求めてください。

制約
0≤N≤10^18
1≤K≤10^18
入力は全て整数
===================
tried-01:

improvement:
"""

# === tried-01 ===
n, k = map(int, input().split())
plus_min = n % k

print(min(plus_min, abs(plus_min - k)))

# === improvement ===
