"""
問題文
N人の社員からなる会社があり、各社員には1,...,Nの社員番号が割り当てられています。
社員番号1の社員以外の全ての社員には、自分より社員番号が小さい直属の上司がちょうど1人います。
XさんがYさんの直属の上司であるとき、YさんはXさんの直属の部下であるといいます。
社員番号iの社員の直属の上司の社員番号がAiであることが与えられます。
各社員について直属の部下が何人いるか求めてください。

制約
2≤N≤2×10^5
1≤Ai<i
===================
tried-01:
collections.Counterを利用した。
社員数が多ければこっちの方が早くなりそうな気がする。

improvement:
listでカウント。
社員数が少なければこっちの方が早かった。
"""

# === tried-01 ===
from collections import Counter

emproyee_num = int(input())
bosses = list(map(int, input().split()))
boss_counter = Counter(bosses)

for i in range(1, emproyee_num+1):
    print(boss_counter[i])

# === improvement ===
N = int(input())
A = list(map(int, input().split()))
B = [0]*N
for a in A:
    B[a-1] += 1
print("\n".join(map(str, B)))
