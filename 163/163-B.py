"""
問題文
高橋君の夏休みはN日間です。
夏休みの宿題がM個出されており、
i番目の宿題をやるにはAi日間かかります。
複数の宿題を同じ日にやることはできず、また、宿題をやる日には遊ぶことができません。
夏休み中に全ての宿題を終わらせるとき、最大何日間遊ぶことができますか？
ただし、夏休み中に全ての宿題を終わらせることができないときは、かわりに -1 を出力してください。

制約
1≤N≤106
1≤M≤10^4
1≤Ai≤10^4

===================
tried-01:

improvement:
"""

# === tried-01 ===
n, m = map(int, input().split())
days = list(map(int, input().split()))

playday = n - sum(days)

if playday < 0:
    print(-1)
else:
    print(playday)

# === improvement ===
