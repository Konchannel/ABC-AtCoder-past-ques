"""
問題文
高橋君は明日からのN日間のうちK日を選んで働くことにしました。
整数Cと文字列Sが与えられるので、次の2つの条件を満たすようにして働く日を選びます。

ある日働いたら、その直後のC日間は働かない
Sのi文字目が x のとき、今日から i日後には働かない

高橋君が必ず働く日をすべて求めてください。

制約
1≤N≤2×10^5
1≤K≤N
0≤C≤N
Sの長さは N
Sの各文字は o か x
問題文中の条件を満たすように働く日を選ぶことが可能
===================
improvement:
"""
# === improvement ===
N, K, C = map(int, input().split())
S = input()

latest = [None] * K
i = len(S) + C
for j in range(K):
    i = S.rindex("o", 0, i - C)
    latest[j] = i

if i <= C or "o" not in S[:i - C]:
    i = -C - 1
    for j in range(K - 1, -1, -1):
        i = S.index("o", i + C + 1)
        if i == latest[j]:
            print(i + 1)
