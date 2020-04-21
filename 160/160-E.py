"""
問題文
あなたは、X個の赤色のリンゴとY個の緑色のリンゴを食べようとしています。
あなたはA個の赤色のリンゴを持っており、美味しさはそれぞれ
p1,p2,…,pAです。
あなたはB個の緑色のリンゴを持っており、美味しさはそれぞれ
q1,q2,…,qBです。
あなたはC個の無色のリンゴを持っており、美味しさはそれぞれ
r1,r2,…,rCです。
無色のリンゴは食べる前に着色することで、赤色のリンゴもしくは緑色のリンゴと見なすことができます。
以上のリンゴの中から、できるだけ美味しさの総和が大きくなるように食べるリンゴを選びます。
0個以上の無色のリンゴに適切に着色したとき、食べる
X+Y個のリンゴの美味しさの総和が最大でいくつになるか求めてください。

制約
1≤X≤A≤10^5
1≤Y≤B≤10^5
1≤C≤10^5
1≤pi≤10^9
1≤qi≤10^9
1≤ri≤10^9
入力はすべて整数である。
===================
tried-01:

improvement:
"""

# === tried-01 ===
x, y, a, b, c = map(int, input().split())
ps = sorted(list(map(int, input().split())), reverse=True)
qs = sorted(list(map(int, input().split())), reverse=True)
rs = sorted(list(map(int, input().split())), reverse=True)

choice_apples = sorted(ps[:x] + qs[:y])
total = 0
j = 0

for i in choice_apples:
    if rs and i < rs[0]:
        total += rs[0]
        del rs[0]
    else:
        total += i

print(total)

# === improvement ===


def f():
    return list(map(int, input().split()))


X, Y, *e = f()
P = f()
Q = f()
R = f()
P.sort()
Q.sort()
R.sort()
print(sum(sorted(P[-X:]+Q[-Y:]+R)[-X-Y:]))
