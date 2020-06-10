"""
問題文
1が書かれたカードがA枚、0が書かれたカードがB枚、−1が書かれたカードがC枚あります。
これらのカードから、ちょうどK枚を選んで取るとき、取ったカードに書かれた数の和として、 ありうる値の最大値はいくつですか。

制約
入力は全て整数である。
0≤A,B,C
1≤K≤A+B+C≤2×10^9
===================
tried-01:

improvement:
"""

# === tried-01 ===
a, b, c, k = map(int, input().split())
max_total = 0

if k <= a:
    print(k)
elif k <= a+b:
    print(a)
else:
    print(2 * a - k + b)

# === improvement ===
