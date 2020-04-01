"""
問題文
長さNの整数列
A1, A2, …, ANと正の整数 Sが与えられます。
1≤L≤R≤Nをみたす整数 (L,R)の組について、
f(L,R)を以下のように定めます。
・L≤x1<x2<⋯<xk≤Rかつ Ax1+Ax2+⋯+Axk=Sを満たすような整数列 (x1,x2,…,xk)の個数
1≤L≤R≤Nを満たす整数 (L,R)の組すべてに対するf(L,R)の和を求めてください。
ただし、答えは非常に大きくなることがあるので、998244353で割ったあまりを出力してください。

制約
入力は全て整数である。
1≤N≤3000
1≤S≤3000
1≤Ai≤3000
===================
tried-01:

improvement:
"""

# === tried-01 ===
n, s = map(int, input().split())
aaas = list(map(int, input().split()))
ans_total = 0

for i in range(n):
    for j in range(1, n-i):
        if aaas[i] + aaas[i+j] == s:
            # 何回使われるかの計算
            # print(i, aaas[i], j, aaas[i + j])
            ans_total += (i+1)*(n-j)

print(ans_total)

# === improvement ===
