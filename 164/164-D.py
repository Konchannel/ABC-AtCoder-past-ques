"""
問題文
1から9までの数字のみからなる文字列Sが与えられます。
次のような条件を満たす整数の組
(i,j)(1≤i≤j≤|S|) の総数を求めてください。

条件:
Sのi文字目からj文字目までを10進法の整数としてみると、この整数は2019の倍数である。

制約
1≤|S|≤200000
Sは 1 から 9 までの数字のみからなる文字列

===================
tried-01:

improvement:
"""

# === tried-01 ===


# === improvement ===
s = input().strip()
x = remain = 0
remains = [0] * 2019
k = 1
for d in map(int, list(s[::-1])):
    x = d * k + remain
    remain = x % 2019
    k = (10 * k) % 2019
    remains[remain] += 1

print(sum([(remain * (remain - 1)) // 2 for remain in remains]) + remains[0])

