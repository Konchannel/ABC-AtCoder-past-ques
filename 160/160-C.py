"""
問題文
1周Kメートルの円形の湖があり、その周りに N軒の家があります。
i番目の家は、湖の北端から時計回りにAiメートルの位置にあります。
家の間の移動は、湖の周りに沿ってのみ行えます。
いずれかの家から出発してN軒すべての家を訪ねるための最短移動距離を求めてください。

制約
2≤K≤10^6
2≤N≤2×10^5
0≤A1<...<AN<K
入力中のすべての値は整数である。
===================
tried-01:

improvement:
A += [A[0]+K]
の一行を入れることで、処理の際に終端と最初の差も求めている。
"""

# === tried-01 ===
k, n = map(int, input().split())
home_positions = list(map(int, input().split()))


def max_distance_homes(homes):
    max_distance = 0
    for i in range(len(homes) - 1):
        distance = homes[i + 1] - homes[i]
        if max_distance < distance:
            max_distance = distance
    # 終端と最初の差を求める。
    distance = k + homes[0] - homes[-1]
    if max_distance < distance:
        max_distance = distance
    return max_distance


print(k - max_distance_homes(home_positions))


# === improvement ===
K, N = map(int, input().split())
A = list(map(int, input().split()))
A += [A[0]+K]
print(K-max(A[i+1]-A[i] for i in range(N)))
