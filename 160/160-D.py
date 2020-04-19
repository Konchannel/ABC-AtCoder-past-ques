"""
問題文
1からNまでの番号がつけられたN個の頂点を持つ無向グラフGがあります。
Gには、以下のように合計N本の辺があります。
i=1,2,...,N−1について、頂点iと頂点i+1の間に辺があります
頂点Xと頂点Yの間に辺があります
k=1,2,...,N−1について、以下の問題を解いてください。

整数の組(i,j)(≤i<j≤N)であって、Gにおいて頂点iと頂点jの最短距離がkであるようなものの数を求めてください

制約
3≤N≤2×10^3
1≤X,Y≤N
X+1<Y
入力はすべて整数である。
===================
improvement:
"""
# === improvement ===

n, x, y = map(int, input().split())
k = [0]*n
for i in range(1, n):
    for j in range(1, n-i+1):
        t = min(j, abs(i-x)+abs(i+j-y)+1)
        k[t] += 1
for i in range(1, n):
    print(k[i])
