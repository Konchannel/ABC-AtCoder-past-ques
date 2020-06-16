"""
問題文
正整数Nが与えられます。
2以上N以下の整数Kを決めて、
NがK未満になるまで次の操作を繰り返し行います。

操作：
NがKで割り切れるとき、NをN/Kに置き換える。そうでないとき、
NをN−Kに置き換える。
最終的にNが1になるような Kの決め方は何通りありますか？

制約
2≤N≤10^12
Nは整数
===================
tried-01:

improvement:
"""

# === tried-01 ===


# === improvement ===
n=int(input())
if n == 2:
    count = 1
else:
    count = 2
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        k = n//i
        while k > 0:
            if k % i == 0:
                k = k//i
            else:
                if k % i == 1:
                    count += 1
                break
    elif (n-1) % i == 0:
        count += 1
        if i != (n-1)//i:
            count += 1
print(count)
