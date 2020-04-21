#Memo
###小数点以下の切り捨て
 - int( 小数 )

###組み合わせ
v個の中から2つを取り出す場合
 - v*(v-1)//2
 
### 総和
1からnまでの総和を求める
 - n/2(n+1)
 
### ランダムなn文字の文字列
012~XYZのstrを作り、そこからランダムに1つ取り出す。それをn回繰り返す。
 - import random, string

　　def randomname(n):

　　　　return ''.join(random.choices(string.ascii_letters + string.digits, k=n))