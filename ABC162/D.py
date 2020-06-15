"""
問題文
R,G,Bのみからなる、長さNの文字列Sがあります。
以下の2つの条件をともに満たす組 (i, j, k) (1≤i<j<k≤N)の数を求めてください。
・Si≠SjかつSi≠SkかつSj≠Skである
・j−i≠k−jである

制約
1≤N≤4000
Sは R, G, B のみからなる、長さNの文字列である
===================
improvement:
よく考えればRGBの組は6通りしかないので、この書き方でも読みやすいかな。

"""

# === improvement ===
n = int(input())
s = input()
c = s.count
r, g, b = c('R'), c('G'), c('B')
t = 0
for i in range(n-2):
    for w in range(1, (n-i+1)//2):
        if s[i]+s[i+w]+s[i+w*2] in ('RGB', 'RBG', 'GRB', 'GBR', 'BRG', 'BGR'):
            t += 1
print(r*g*b-t)
