"""
問題文
文字列Sが与えられます。
Sに含まれる文字をそれぞれ一度ずつ使い、何個かの回文を作ることを考えます。
例えばS=aaab のとき、二つの回文 aba と a を作ることができます。
このように、文字は自由な順序で使用することができ、Sに複数回現れる文字は合計でその回数だけ使用します。
長さLの回文を1個作るごとに、L^2のスコアが得られます。
最大で合計いくつのスコアを得ることができるでしょうか？

制約
1≦|S|≦100,000
Sは小文字アルファベットのみからなる。
===================
tried-01:

improvement:
"""

# === tried-01 ===
from collections import Counter

s = list(input())

vals = Counter(s).values()
'''
戦略
・2文字以上ある単語はまとめて、長大な1つの回文にする
・1文字しかない単語（や、余った文字）は1単語のみの回文として計上
'''
long_word = 0
short_words = 0
result = 0

for val in vals:
    long_word += val // 2
    short_words += val % 2

if 1 <= short_words:
    result += (long_word * 2 + 1) ** 2
    result += short_words - 1
elif 0 == short_words:
    result += (long_word * 2) ** 2
else:
    pass

print(result)

# === improvement ===
