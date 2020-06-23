#Memo

###小数点以下の切り捨て
 - int( 小数 )

###組み合わせ
v個の中から2つを取り出す場合
 - v*(v-1)//2
 
### 総和
1からnまでの総和を求める
 - n/2(n+1)
 
### 文字列中のある特定ワード以降の文字列を抽出
文字列x中の、"ちなみに"以降を抽出する

正規表現は使わないものとする

 - x[x.find("ちなみに"):]
 
### 要素をランダムに並べ替える
文字列"あいうえお"をランダムに並べ替える

import random
 
 - "".join(random.sample("あいうえお", 10))
 
### ランダムなn文字の文字列
123~90abc~XYZのstrを作り、そこからランダムに1つ取り出す。それをn回繰り返す。

import random
import string

 - ''.join(random.choices(string.ascii_letters + string.digits, k=n))