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

# === improvement ===
n, s = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * (s + 1)
ans = 0
mod = 998244353
for i in range(n):
    c_ = c.copy()
    if a[i] <= s:
        for j in range(a[i], s + 1):
            c[j] += c_[j - a[i]]
        c[a[i]] += i + 1
    ans += c[s]
    ans %= mod

print(ans)

# === improvement-02 ===
import numpy as np

n, s = map(int, input().split())
a = list(map(int, input().split()))
mod = 998244353

res = 0
dp = np.zeros(s + 1, dtype=int)

for i in range(n):
    dp[0] += 1
    dp[a[i]:] += dp[:-a[i]].copy()
    dp %= mod
    res += dp[s]
    res %= mod

print(res)
