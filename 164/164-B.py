"""

===================
tried-01:
これはWAのコード。ラストのテストケースだけ通らなかった。

=>
例えば入力が 1 2 1 1 だったとき、tried-01の例では
    a/d + int(bool(a % d)) >= c/b + int(bool(c % b))
  = 1/1 + int(bool(1 % 1)) >= 1/2 + int(bool(1 % 2))
  =  1  +        0         >= 0.5 +       1
となり、本来先行が1撃で倒せていたところを、1/2の0.5が入ることで式が狂っている。（本来は2/1が整数部分の0だけ入る想定だった）

improvement:
intでくくる位置が間違っていたので修正。ついでに条件式の判定がうまくいってなかったのでboolで囲む。
これでめでたくACできた。

improvement-02:
math.ceilで切り上げちゃった方が簡単だし見やすい。
それに速い。
"""

# === tried-01 ===

a, b, c, d = map(int, input().split())
print('Yes' if a/d+int(bool(a % d)) >= c/b+int(bool(c % b)) else 'No')

# === improvement ===
a, b, c, d = map(int, input().split())
print('Yes' if bool(int(a/d + bool(a % d)) >= int(c/b + bool(c % b))) else 'No')

# === improvement-02 ===
import math

a, b, c, d = map(int, input().split())
print('Yes' if math.ceil(a/d) >= math.ceil(c/b) else 'No')