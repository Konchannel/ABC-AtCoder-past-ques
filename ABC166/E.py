"""
問題文
AtCoder王国の優秀なエージェントであるあなたは、盗まれた極秘情報がAlDebaran王国の手に渡ることを阻止するため、取引現場であるパーティに潜入しました。
パーティにはN人の参加者がおり、それぞれ1からNまでの番号がついています。参加者iの身長はAiです。
あなたは事前の尋問によって、極秘情報を取引するのは以下の条件を満たす2人組であることを知っています。
2人の持つ番号の差の絶対値が、2人の身長の和に等しい。
N人の参加者のうちから2人を選んでペアにする方法は
N(N−1)/2通りありますが、このうち上の条件を満たすペアは何通りあるでしょう？

なお、極秘情報の内容が何であるかはあなたの知るところではありません。

制約
入力はすべて整数
2≤N≤2×10^5
1≤Ai≤10^9(1≤i≤N)
===================
tried-01:
TLEしてしまったコード。
計算量はO(N^2)。

improvement:
計算量がO(N)に抑えられている。
そもそも、AtCoderで可能なループ数は10^9までと言われており、制約のAi上限的にも、計算量はO(N)に抑える前提で設計し始める必要があった。
"""

# === tried-01 ===
n = int(input())
members = list(map(int, input().split()))
pairs = 0

for index1, member1 in enumerate(members, 1):
    for index2, member2 in enumerate(members[index1:], index1 + 1):
        if member1 + member2 == index2 - index1:
            pairs += 1

print(pairs)

# === improvement ===
n, *a = map(int, open(0).read().split())
d, s = [0]*n, 0
for i, x in enumerate(a):
    if i+x < n:
        d[i+x] += 1
    if i-x >= 0:
        s += d[i-x]
print(s)
