# python

- 定数大文字
- Python では、整数と小数点のある数（実数：浮動小数点数）は別
- しかし「== 」の比較では同じ
- 整数と実数の間の変換は int 関数, float 関数を使用
- Python では整数はいくらでも大きくなります。
- もちろん、コンピュータのメモリに納まる限りにおいて
- '''または”””で改行含む文字列
- print(format)

## 参考

[リスト、タプル](https://qiita.com/Usek/items/65a3df2be7bd0a2b4189)
[セット](https://qiita.com/Usek/items/6d05a580142db7c31c07)
[ディクショナリ](https://qiita.com/Usek/items/1463b544ca2d0aeec4e2)
[内包表記](https://qiita.com/Usek/items/5eb3235ba10becb6df96)

## 文字列

```python
# エンコード指定(コメント形式で記述してOK)
# -*- coding: utf-8 -*-

# 改行あり
text = """sdvc
b.jb"""

# in(真偽地)
str_var = "abc"
"a" in str_var

# 繰り返し
str_var = str_var * 3

# 部分指定(-1でlastIndex)
#  str[開始インデックス:終了インデックス]
#  str[開始インデックス]
# len()
# min()
# max()
```

## List, Tuple

```python
# 宣言
list_var = [1, 2, 3.4, "a", z]
# Listより速い
tuple_var = (1, 2, 3.4, "a", "test")
# List固有(append, remove, reverse, sort)
list_var.append("要素")
list_var.append("要素")
list_var.remove('要素')
list_var.reverse()
list_var.sort()
# list_var.[0:4]
# in
# len()
# min()
# max()

```

## set

```python
# セット(Set)は、ユニークなデータのグループを保持します。
# セットはデータの順番を持たないため、文字列やリストのようにインデックシングを行うことが出来ません。
# セットを使用するメリットは、ユニオン(合併)やインターセクション(積集合)、ディファレンス(差集合)の処理が高速に行える点です。
set_var = {1, 2, "a", "b", 1, "a"}
set_var2 = set([1, 2, "a", "b", 1, "a"])

# in
# len()
# add, remove
set_var.add("要素")
set_var.remove("要素")
# discard(要素がセットに存在している時に限り削除する)
set_var.discard("要素")

# union(合併), intersection(交差・積集合), difference(差集合)
# 複数のセットから重複要素を省いて1つのセットにする処理のことです。
set_var.union(set_var2)
# 指定したセット両方(全て)に重複している要素を抽出します。
set_var.intersection(set_var2)
# 一方に存在し、もう一方に存在しない要素を抽出します。
set_var.difference(set_var2)

# symmetric_difference(2セット限定)
# 順番に関係なくXとY一方のセットに存在する項目を抽出できる
set_var.symmetric_difference(set_var2)

```

## dectionary

```python
dictionary_var = {'key1': 'Value1', 'key2': 'Value2'}

# 追加, 更新 (あれば更新なければつい追加)
dictionary_var['key3'] = 'value3'

# 取得 get (キーが存在していなくてもエラーにならない)
dictionary_var.get('key3', 'No Existance')

# 削除 del, pop (popはキーが存在していなくてもエラーにならない)
dictionary_var.del('key3')
dictionary_var.pop('key3', 'No Existance')

# in
# len()
# min()
# max()
```

## 内包表記

```python
# 内包表記を使用するとリスト、セット、ディクショナリのデータ操作を短い行数で記述できます。
# また処理速度も早くなるので、膨大な要素を持つ場合はこちらを使いましょう。


# Listの内包表記
result = [x**2 for x in [1, 2, 3, 4, 5]]
print("{0}".format(result)) # [1, 4, 9, 16, 25]
# 内包表記なし
result = []
for i in [1, 2, 3, 4, 5]:
    result.append(i**2)
print("{0}".format(result))
# リスト内包表記は、リストの要素内で処理する要素、処理しない要素を条件指定することができます。
print("{0}".format( [x*10+1 for x in range(1,6) if x > 2 and x < 5]))
# [31, 41]
# 内包表記なし
result = []
for x in range(1,6):
    if x > 2 and x < 5:
        result.append(x*10+1)
print("{0}".format(result))

# setの内包表記
# 内包表記はセットでも使用可能です。使用方法はリスト内包表記と同じです。
print("{0}".format( {x*10+1 for x in range(1,6) if x > 2 and x < 5}))
# set([41, 31])

# dictionaryの内包表記
print("{0}".format( {str(x):x**2 for x in range(1,6)}))
```

## 制御構文

```python
# if
# 比較演算子
# ==, != , <, <=, >, =>
# and, or, not
# falsyな値(空のリスト, タプル, ディクショナリ, セット, None(値が存在しない」ことを示す特別な型))
# is None
flg_true = True
flg_false = False
flg_none = None
list_var = ["a", "b"]
if list_var in "c" or flg_false == True :
  print(False)
elif flg_true != True :
  print(False)
elif not(list_var in "a" and flg_none == None) :
  print(False)
else :
  print(True)

# for
# for i in range() :
for i in range(1,10):
   print("{0}".format(i))
# enumurate
a = ["a","b","c","d","e"]
for idx,elem in enumerate(a):
   print("{0} = {1}".format(idx,elem))
else:
    print("for loop done")
# while
a = ["ok","ok","ok","ng","ok"]
i = 0
while a[i] == 'ok':
    print("a[{0}] is ok".format(i))
    i = i + 1
else:
    print("while loop done")
```

## 例外

```python
# try/except
try:
    a = 10 / 0
    print("{0}".format(a))
except ZeroDivisionError as e:
    print("type:{0}".format(type(e)))
    print("args:{0}".format(e.args))
    print("message:{0}".format(e.message))
    print("{0}".format(e))
# type:<type 'exceptions.ZeroDivisionError'>
# args:('integer division or modulo by zero',)
# message:integer division or modulo by zero
# integer division or modulo by zero

# else/finaly
try:
    a = 10 / 0
#    a = 10 / 1
    print("{0}".format(a))
except ZeroDivisionError as e:
    print("ZeroDivisionError!!")
else:
    print("else statement")
finally:
    print("finally statement")
```

## 関数

```python
# def 関数名 ( 引数 ):
#     処理
#     return 戻り値
# return省略
# デフォルト引数
# グローバル変数の指定
# global 変数名

# *可変長引数(tuple型として渡される)
def spam(*args):
    print("{0}".format(args))

spam("arg1",2,3.4)

# **可変長引数(dictionary型として渡される)
def spam2(**args):
    print("{0}".format(args))

spam(taro=165,jiro=180,saburo=170)
```

## クラス

```python
# 先頭大文字
# 「クラス名()」でインスタンス化
# 最低1つの引数を持つ
# 最初の引数は必ずselfという名前にする慣例がある
# Javaで言う「this」
# コンストラクタ
#   「__init__()」であらわされる
# デストラクタ(オブジェクトが不要となりPythonが削除する時に自動で実行される関数)
#   「__del__ 」であらわされるが、ほとんどの場合デストラクタは定義しない。
# 継承
#   
# 1.クラスSpamのオブジェクトspamを生成します(コンストラクタで初期化)
# 2.spamオブジェクトがhamメソッドを呼び出します
# 3.spamオブジェクトのhamメソッドはspamオブジェクト(=自身)のeggメソッドを呼び出します
# 4.spamオブジェクトのeggメソッドは引数のmsgを出力します
# 5.eggメソッドはspamオブジェクトの変数valを出力します
class Spam:
    def __init__(self,val2):
        self.val2 = val2
    val = 100
    def ham(self):
        self.egg('call method')

    def egg(self,msg):
        print("{0}".format(msg))
        print(("{0}".format(self.val)))

spam = Spam(200)
spam.ham()
```
