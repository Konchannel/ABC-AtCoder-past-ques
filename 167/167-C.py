"""
問題文
競技プログラミングを始めた高橋くんは、学びたいアルゴリズムがM個あります。
最初、各アルゴリズムの理解度は0です。
高橋くんが書店に行くと、N冊の参考書が売っていました。
i番目の参考書(1≤i≤N)はCi円で売られていて、購入して読むことで、各j(1≤j≤M) についてj番目のアルゴリズムの理解度が
Ai,j上がります。
また、それ以外の方法で理解度を上げることはできません。
高橋くんの目標はM個すべてのアルゴリズムの理解度をX以上にすることです。
高橋くんが目標を達成することが可能か判定し、可能な場合は目標を達成するのに必要な金額の最小値を計算してください。

制約
入力はすべて整数
1≤N,M≤12
1≤X≤10^5
1≤Ci≤10^5
0≤Ai,j≤10^5
===================
tried-01:
解けなかった
リストの要素同士の全ての組み合わせを出すの難しい。

improvement:
"""

# === tried-01 ===
'''
import itertools

n, m, x = map(int, input().split())
ans = -1
books = []

for i in range(n):
    books.append(list(map(int, input().split())))

for j in range(n):
    for k in itertools.combinations(books, j):
        tmps = [sum(a) for a in list(zip(k))]
        print(k, tmps)
'''

# === improvement ===
N, M, X = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]

C = 10 ** 7
for i in range(2 ** N):
    P, T = [0] * M, 0
    for j in range(N):
        if i & 2 ** j:
            T += A[j][0]
            for k in range(M):
                P[k] += A[j][k + 1]
    for j in range(M):
        if P[j] < X:
            break
    else:
        C = min(C, T)

print(-1 if C == 10 ** 7 else C)