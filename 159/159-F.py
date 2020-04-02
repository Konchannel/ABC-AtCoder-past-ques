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
import itertools

n, s = map(int, input().split())
aaas = list(map(int, input().split()))
sum_s_list = []

for i in range(1, n+1):
    for j in itertools.combinations(aaas, i):
        if sum(j) == s:
            print(j)
'''

for i in range(n):
    for j in range(1, n-i):
        if aaas[i] + aaas[i+j] == s:
            # 何回使われるかの計算
            # print(i, aaas[i], j, aaas[i + j])
            sum_s_list.append(['i', 'j'])

            # 考え違えをしてた。1≤L≤R≤Nを満たす整数 (L,R)の組すべてに対するf(L,R)の和を求めてください。
            # 現在の式は、2つしか足せないうえに、ていぎもちがーう！かなP

print(ans_total)'''

# === improvement ===
