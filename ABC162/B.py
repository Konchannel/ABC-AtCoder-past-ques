"""
問題文
FizzBuzz列a1,a2,...を次のように定めます。
iが3でも5でも割り切れるなら、
ai=FizzBuzz
そうではなくiが3で割り切れるなら、
ai=Fizz
そうではなくiが5で割り切れるなら、
ai=Buzz
そうではないなら、
ai=i
FizzBuzz列のN項目までに含まれる数の和を求めてください。

制約
1≤N≤10^6
===================
improvement:
ゴリ書きで時間に収まっていたらしい。
効率の良いアルゴリズムを追い求めていたが、まず書いて動かした後リファクタ、の原則を忘れていた。
1番に動くこと、2番に速いこと、3番にキレイなこと、なんです。
"""

# === tried-01 ===

n = int(input())


def souwa(n):
    syo, jyoyo = divmod(n, 2)
    return (n + 1) * syo + (n + 1) // 2 * jyoyo


print(souwa(n) - souwa(n//3)*3 - souwa(n//5)*5 + souwa(n//15)*15)


# === improvement ===
n = int(input())
print(sum(i for i in range(n+1) if i % 3 and i % 5))
