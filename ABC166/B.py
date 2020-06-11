"""
問題文
ある街に、N人のすぬけ君(すぬけ君1、すぬけ君2、...、すぬけ君N)が住んでいます。
この街には、K種類のお菓子(お菓子1、お菓子2、....、お菓子K)が売られています。
お菓子iを持っているのは、すぬけ君Ai,1,Ai,2,⋯,Ai,diの計di人です。
高橋君は今からこの街を回り、お菓子を1つも持っていないすぬけ君にいたずらをします。
このとき、何人のすぬけ君がいたずらを受けるでしょうか。

制約
入力は全て整数
1≤N≤100
1≤K≤100
1≤di≤N
1≤Ai,1<⋯<Ai,di≤N
===================
tried-01:
set型.add()は、1つの値しか追加できないので、foreachでひとつひとつ取得した。

improvement:
a |= b を用いて、和集合を代入した。これにより、listをsetに追加することが出来る。
(a |= b は a = a | b と同じ)
"""

# === tried-01 ===
n, k = map(int, input().split())
have_treats = set()

for i in range(k):
    input()
    for j in map(int, input().split()):
        have_treats.add(j)

print(n - len(have_treats))

# === improvement ===
N, K = list(map(int, input().split()))

r = set()
for i in range(K):
    input()
    r |= set(map(int, input().split()))
print(N - len(r))
