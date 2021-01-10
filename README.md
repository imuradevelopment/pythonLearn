# python(p48 まで)

## 言語特徴

- インタプリタ言語(1 行ずつ機械語に変換：逆はコンパイル言語)
- 言語の習得とアプリケーション開発にかかる労力が少ない
- インタプリタ上で実行されるため、C 言語や Java などに比べて実行速度は遅いが、多言語との連携が容易である

## python でできること

- 機械学習
- ニューラルネットワーク
- データサイエンス
- GUI/Web アプリケーション

## インストール

- https://www.python.org/
  - ディストリビューションによって、ライブラリの管理パッケージ等が異なる
    - Anaconda
    - PSF

## 規約

エンコード

```python
# 下記コメントは意味を成す。
# coding: utf-8
# または
# -*- coding: utf-8 -*-
```

インデント  
不要なインデントは実行時エラーになる  
エスケープ  
「/」

## 変数とデータ型

変数に格納する値には様々な**型**がある。  
C や Java では、使用する変数は先立って明示的に型を指定して宣言しておく必要がある。(静的型付き言語)  
これに対して、Python は動的型付き言語である。  
また、日本語を変数名として使用できる。

### 型の種類

- 数値
  - int
  - float
  - complex
- 文字列
  - raw stinrg
  - stinrg
- 真偽値
  - bool
- ヌルオブジェクト
  - None

### 型変換, 検査

- 型(値)
- type(値)
- isinstance(値, 型)

## メソッド

- split()
  - 文字列の分解
- splitlines()
  - 行の分離
- join()
  - リストの要素連結
- replace()
  - 文字列置換
- isalpha(), isdecimal(), isalnum()
  - すべての要素が「アルファベット, 数字, アルファベットか数字」
- upper(), lower(), isupper(), islower()
  - 大文字小文字変換、大文字小文字判定
- capitalize(), title(), swapcase()
  - 文頭を大文字に変換、各単語の先頭を大文字に変換、大文字小文字反転
- ord)(), chr()

  - 文字コードの取得、指定した文字コードの文字

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
# 改行あり
text = """sdvc
b.jb"""

# in(真偽地)
str = "abc"
"a" in str

# 繰り返し
str = str * 3

# 部分指定(-1でlastIndex)
#  str[開始インデックス:終了インデックス]
#  str[開始インデックス]
# len()
# min()
# max()
```

## List

```python
# 宣言
list = [1, 2, 3.4, "a", z]
# 追加, 挿入
list.append("要素")
list.insert(index, "要素")
# 連結
list3 = list1 + list2  # 新規オブジェクトとして
list1.extend(list2)    # リストの追加
# 削除
del list[0]
list.remove('要素') # 指定要素の削除, 先頭から一致したもの
list.pop() # 指定したインデックスの要素を取り出して削除, 引数なしで末尾対象
# メンバシップの検査
'要素' in list
'要素' not in list
# 要素の探索(なければValueError)
list.index('要素')
# カウント
list.count('要素')
len(list)
# sum, sort, sorted, reverse
sum(list)
min(list)
max(list)
list.sort()   # リストそのものを変更
list.sorted() # 別のリストにソート
list.reverse()  # リストそのものを変更
list.reversed() # 別のリストにソート
# リストの複製
list2 = list.copy() # shallowcopy
import copy
list2 = copy.copy(list) # shallowcopy
list2 = copy.deepcopy(list) # deepcopy
```

## Tuple

```python
# Listより速い
# Listと混在させる事がきる
# 一度生成すると変更できない(イミュータブル)
tuple = (1, 2, 3.4, "a", "test")
# 括弧の省略
(x, y) = (2, 3)
# sorted()
list = sorted(tuple)
```

## set

```python
# 重複値は格納できない
# 順番を保持せず、文字列やリストのようにインデックシングを行うことが出来ない。
# セットを使用するメリットは、
# ユニオン(合併)やインターセクション(積集合)、ディファレンス(差集合)の処理が高速に行える点です。
set = {1, 2, "a", "b", 1, "a"}
set = set([1, 2, "a", "b", 1, "a"])

# 要素の追加, 削除, 取得, 複製
set.add()
set.discard()
set.clear()
len(set)
set2 = set.copy()

# 集合論の操作
set.issubset(set2)              # 真偽値
set.issuperset(set2)            # 真偽値
set.isdisjoint(set2)            # 真偽値
set.intersection(set2)          # set
set.intersection.update(set2)   # set
set.union(set2)                 # set
set.update(set2)                # set
set.differece(set2)             # set
set.symmetric_difference(set2)  # set
# union(合併), intersection(交差・積集合), difference(差集合)
# 複数のセットから重複要素を省いて1つのセットにする処理のことです。
set.union(set2)
# 指定したセット両方(全て)に重複している要素を抽出します。
set.intersection(set2)
# 一方に存在し、もう一方に存在しない要素を抽出します。
set.difference(set2)

# symmetric_difference(2セット限定)
# 順番に関係なくXとY一方のセットに存在する項目を抽出できる
set.symmetric_difference(set2)

```

## dectionary

```python
dictionary = {'key1': 'Value1', 'key2': 'Value2'}

# 追加, 更新 (あれば更新なければつい追加)
dictionary['key3'] = 'value3'

# 取得 get (キーが存在していなくてもエラーにならない)
dictionary.get('key3', 'No Existance')

# 削除 del, pop (popはキーが存在していなくてもエラーにならない)
dictionary.del('key3')
dictionary.pop('key3', 'No Existance')

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
list = ["a", "b"]
if list in "c" or flg_false == True :
  print(False)
elif flg_true != True :
  print(False)
elif not(list in "a" and flg_none == None) :
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
finally:
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

## django

ファイルはそれぞれ以下のような役割を持っています:  
外側の mysite/ ルートディレクトリは、このプロジェクトのただの入れ物です。  
この名前は Django に関係しませんので、好きな名前に変更できます。  
- manage.py:
Django プロジェクトに対する様々な操作を行うためのコマンドラインユーティリティです｡  
詳しくは django-admin と manage.py 内の manage.py を参照してください｡  
内側の mysite/ ディレクトリは、このプロジェクトの実際の Python パッケージです。  
この名前が Python パッケージの名前であり、 import の際に 使用する名前です (例えば import mysite.urls) 。  
- mysite/__init__.py:
このディレクトリが Python パッケージであることを Python に知らせるための空のファイルです。  
Python の初心者は、 Python の公式 ドキュメントの more about packages を読んで下さい。  
mysite/settings.py:
Django プロジェクトの設定ファイルです。  
設定の仕組みは Djangoの設定 を参照してください。  
mysite/urls.py: Django プロジェクトの URL 宣言、いうなれば Django サイトにおける「目次」に相当します。  
詳しくは URL ディスパッチャ を参照 してください。  
- mysite/wsgi.py:
プロジェクトをサーブするためのWSGI互換Webサーバーとのエントリーポイントです。  
詳細は WSGI とともにデプロイするには を参照してください。

## djangoチュートリアル
### 仮想環境構築

```ps1
# 仮想環境の作成
python --version
python -m venv venv
# 仮想環境の実行(windows)
venv\Scripts\activate.bat
# djangoのインストール
pip install django
pip list
```

### チュートリアル

```ps1
# djangoプロジェクト作成
django-admin startproject mysite

```
