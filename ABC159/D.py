"""
問題文
ボールがN個あり、i番目のボールには整数 Aiが書かれています。
k=1,2,...,N
に対して以下の問題を解いて、答えをそれぞれ出力してください。

k番目のボールを除いた N−1個のボールから、書かれている整数が等しいような異なる
2つのボールを選び出す方法の数を求めてください。選ぶ順序は考慮しません。

制約
3≤N≤2×10**5
1≤Ai≤N
入力はすべて整数である。
===================
tried-01:
ローカルではうまくいくが、提出するとREになってしまう。

improvement:

"""

# === tried-01 ===
import collections
from scipy import special

n = int(input())
num_list = list(map(int, input().split()))

for i in range(0, n):
    target_list = num_list[0:i] + num_list[i+1:]
    target_items = collections.Counter(target_list).items()
    ans = 0

    for item in target_items:
        if item[1] > 1:
            ans += special.comb(item[1], 2, True)

    print(ans)

print()
# === improvement ===
cnt = collections.Counter(num_list)
ttl = 0
for v in cnt.values():
    ttl += v*(v-1)//2
for a in num_list:
    print(ttl - (cnt[a] - 1))

