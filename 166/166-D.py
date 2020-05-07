"""
問題文
A5−B5=Xを満たす整数の組(A,B)をひとつ示してください。
ただし、与えられるXに対して、条件を満たす整数の組(A,B)が存在することが保証されています。

制約
1≤X≤10^9
Xは整数である。
条件を満たす整数の組(A,B)が存在する。
===================
tried-01:
解けなかった。
5乗して10^9以内の数って範囲がそもそも狭いので、総当たりでもよかったらしい。

improvement:

"""

# === tried-01 ===


# === improvement ===
import math
X = int(input())
a1 = math.ceil(X**(1/5))
N = int(1e10)
c = 0
b = 0
b2 = 0
while c <= N:
    c += 1
    if b**5 < -X:
        b2 = b + 1
        break
    b -= 1

c = 0
while c <= N:
    c += 1
    b1 = math.floor((a1**5-X)**(1/5))
    a2 = math.floor((X+b2**5)**(1/5))

    print('a1:' + str(a1) + ' b1:' + str(b1) + ' b2:' + str(b2) + ' a2:' + str(a2) + ' c:' + str(c))

    if a1**5 - b1**5 == X:
        print(a1, b1)
        break
    elif a2**5 - b2**5 == X:
        print(a2, b2)
        break
    a1 += 1
    b2 += 1
