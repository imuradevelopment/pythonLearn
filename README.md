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

## List, Tuple, set, dictionary

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
