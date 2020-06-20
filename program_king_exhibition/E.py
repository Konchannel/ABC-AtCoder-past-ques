"""
問題文
整数Nが与えられます。FizzBuzz問題 (リンク先は Wikipedia「Fizz Buzz」) を解いてください。
ただし、通常のFizzBuzz問題においては3の倍数に対し Fizz 5の倍数に対し Buzzと出力しますが、今回は、
2の倍数に対し a
3の倍数に対し b
4の倍数に対し c
5の倍数に対し d
6の倍数に対し e
と出力してください。 (より詳しくは、出力例 1 をご覧ください。)

制約
1≦N≦1,000
===================
tried-01:

improvement:
"""

# === tried-01 ===
n = int(input())
answers = []

for i in range(1, n + 1):
    i_fb_result = []

    if i % 2 == 0:
        i_fb_result.append('a')
    if i % 3 == 0:
        i_fb_result.append('b')
    if i % 4 == 0:
        i_fb_result.append('c')
    if i % 5 == 0:
        i_fb_result.append('d')
    if i % 6 == 0:
        i_fb_result.append('e')
    if not i_fb_result:
        i_fb_result.append(str(i))

    answers.append(''.join(i_fb_result))

for j in answers:
    print(j)

# === improvement ===
