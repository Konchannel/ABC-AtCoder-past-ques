"""
問題文
いろはちゃんは 長さLの文字列をN個持っており、それぞれ S1,S2,...,SNです。
それらの文字列を好きな順番で全て結合してできる文字列のうち、もっとも辞書順で小さいものを求めてください。
なお、ある文字列 s=s1s2s3...snと t=t1t2t3...tmについて、以下のどちらかを満たすとき、辞書順比較で
s<tであるといいます。
・ある整数i(1≦i≦min(n,m))に関して、1≦j<iを満たす任意の整数jにおいてsj=tjが成立し、かつsi<tiが成立する。
・任意の整数i(1≦i≦min(n,m))に関してsi=tiが成立し、かつn<mが成立する。

制約
1≦N,L≦100
全てのi(1≦i≦N)に対し、Siの長さはLに等しい。
各iについて,Siは全て半角英小文字のみから成る文字列である。
===================
tried-01:

improvement:
"""

# === tried-01 ===
n, l = map(int, input().split())
strs = []

for i in range(n):
    strs.append(input())

strs.sort()
print(''.join(strs))

# === improvement ===
