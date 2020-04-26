"""

===================
tried-01:
これはWAのコード。ラストのテストケースだけなぜか通らなかった。つらい。
検証用も兼ねて残しておく。

improvement:
"""

# === tried-01 ===

a, b, c, d = map(int, input().split())
print('Yes' if a/d+int(bool(a % d)) >= c/b+int(bool(c % b)) else 'No')

# === improvement ===
