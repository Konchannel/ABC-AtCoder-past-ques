"""
問題文
N種類の商品に対して人気投票を行いました。商品iは Ai票を得ています。
この中から人気商品M個を選びます。ただし、得票数が総投票数の1/4M未満であるような商品は選べません。

人気商品M個を選べるならYes、選べないならNoを出力してください。

制約
1≤M≤N≤100
1≤Ai≤1000
Aiは相異なる
入力は全て整数
===================
tried-01:

improvement:
複数行を一気に読み込むopen(0)、
Yes or Noを表示する際によくある"YNeos"[bool::2]の形。
foreachでリスト全体に得票数が総投票数の1/4M以上な商品かどうか判別し、boolのListをsumすることで
得票数が総投票数の1/4M以上の商品数がM以上あるならYes、っていう判別の仕方がエモい。
"""

# === tried-01 ===
n, m = map(int, input().split())
votes = list(map(int, input().split()))
vote_total = sum(votes)
base_4m = vote_total / (4 * m)
over4m_count = 0

for i in votes:
    if i >= base_4m:
        over4m_count += 1

if over4m_count >= m:
    print('Yes')
else:
    print('No')

# === improvement ===
N, M, *A = map(int, open(0).read().split())
S = sum(A) / (4*M)
print("YNeos"[not(sum(a >= S for a in A) >= M)::2])
