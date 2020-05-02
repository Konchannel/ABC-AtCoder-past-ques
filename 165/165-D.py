"""

===================
tried-01:

improvement:
例えば、1~7のそれぞれを3で割った整数部分を求めると、0,0,1,1,1,2,2となる。
nの倍数xをnで割った整数部分は、x-1をnで割った整数部分より1大きくなる。
よって、aとbの間にkの倍数があれば、b//kと(a-1)//kの間に少なくとも1以上の差ができると言える。
"""

# === tried-01 ===
k = int(input())
a, b = map(int, input().split())

if a <= a // k * k or (a // k + 1) * k <= b:
    print('OK')
else:
    print('NG')

# === improvement ===
k = int(input())
a, b = map(int, input().split())
print("OK" if b//k > (a-1)//k else "NG")
