"""
問題文
AtCoder丘陵にはN個の展望台があり、展望台iの標高はHiです。
また、異なる展望台どうしを結ぶM本の道があり、道jは展望台Ajと展望台Bjを結んでいます。
展望台iが良い展望台であるとは、
展望台iから一本の道を使って辿り着けるどの展望台よりも展望台iの方が標高が高いことをいいます。
展望台iから一本の道を使って辿り着ける展望台が存在しない場合も、展望台iは良い展望台であるといいます。
良い展望台がいくつあるか求めてください。

制約
2≤N≤10^5
1≤M≤10^5
1≤Hi≤10^9
1≤Ai,Bi≤N
Ai≠Bi
同じ展望台の組を結ぶ道が複数あることもある。
入力中の値はすべて整数である。
===================
tried-01:

improvement:
"""

# === tried-01 ===
mounten_num, bridge_num = map(int, input().split())
mounten_higests = [0] + list(map(int, input().split()))
not_bad_mountens = ['x'] + ['o'] * mounten_num

# inputをさばく. 橋の架かっている展望台のうち、低いほうはgood_mountenではない
for i in range(bridge_num):
    a, b = map(int, input().split())
    if mounten_higests[a] <= mounten_higests[b]:
        not_bad_mountens[a] = 'x'
    if mounten_higests[a] >= mounten_higests[b]:
        not_bad_mountens[b] = 'x'

print(not_bad_mountens.count('o'))

# === improvement ===
