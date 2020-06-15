"""
問題文
 K   K   K
 ∑   ∑   ∑  gcd(a,b,c)
a=1 b=1 c=1

を求めてください。

ただし、gcd(a,b,c)は a,b,cの最大公約数を表します。

制約
1≤K≤200
Kは整数
===================
improvement:
シグマの3連を見て、ビビッてしまった。
しかし、分解して考えてみれば大したことはない掛け算。
数式とnumpyの扱いに慣れておかなければと思う。
"""

# === improvement ===
import numpy as np

K = int(input())
x = np.arange(1, K + 1)
nums = np.gcd.outer(np.gcd.outer(x, x), x)

print(np.sum(nums))
