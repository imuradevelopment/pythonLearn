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
- mysite/**init**.py:  
  このディレクトリが Python パッケージであることを Python に知らせるための空のファイルです。  
  Python の初心者は、 Python の公式 ドキュメントの more about packages を読んで下さい。  
  mysite/settings.py:
  Django プロジェクトの設定ファイルです。  
  設定の仕組みは Django の設定 を参照してください。
- mysite/urls.py:  
  Django プロジェクトの URL 宣言、いうなれば Django サイトにおける「目次」に相当します。  
  詳しくは URL ディスパッチャ を参照 してください。
- mysite/wsgi.py:  
  プロジェクトをサーブするための WSGI 互換 Web サーバーとのエントリーポイントです。  
  詳細は WSGI とともにデプロイするには を参照してください。

## django チュートリアル

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

### プロジェクト(mysite)作成

参考リンク:  
[django 公式チュートリアル](https://docs.djangoproject.com/ja/2.2/intro/tutorial01/)

1. django プロジェクト作成

```ps1
django-admin startproject mysite
cd mysite
<#
作成されるファイル群
mysite/               プロジェクトのただの入れ物
    manage.py         ロジェクトに対する様々な操作を行うためのコマンドラインユーティリティ
    mysite/           プロジェクトの実際の Python パッケージ,  import に 使用する名前 (例えば import mysite.urls)
        __init__.py   Python パッケージであることを Python に知らせるための空のファイル
        settings.py   Django プロジェクトの設定ファイル
        urls.py       Django プロジェクトの URL 宣言、いうなれば Django サイトにおける「目次」に相当
        wsgi.py       プロジェクトをサーブするためのWSGI互換Webサーバーとのエントリーポイント
#>
```

2. django 開発サーバー起動:port8000

```ps1
# 絶対に運用環境では 使わない
python manage.py runserver
```

3. アプリケーション(polls)作成

```ps1
python manage.py startapp polls
# アプリケーションは Python path のどこにでも置ける
<#
作成されるファイル群(アプリの全体像)
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
#>
```

4. ビューの作成

```python
# polls/views.py¶
from django.http import HttpResponse
from django.template import loader # templateの読み込みのみ

from django.http import Http404 # 404 エラーの送出
from django.shortcuts import get_object_or_404 # 404 エラーの送出(簡易：オブジェクトがない場合)
from django.shortcuts import get_list_or_404 # 404 エラーの送出(簡易：リストが空の場合)
# テンプレートをロードしてコンテキストに値を入れ、
# テンプレートをレンダリングした結果を HttpResponse オブジェクトで返す
# HttpResponse, loaderが必要なくなる
from django.shortcuts import render
rom django.urls import reverse # 設定した URLconfを返す
from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail_stb(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def detail_404_error(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote_stab(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # POST データに choice がなければ、質問投票フォームを再表示します。
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "選択肢を選択していません。",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POSTデータを正常に処理した後は、常にHttpResponseRedirectを返します。
        # これにより、ユーザーが[戻る]ボタンを押した場合にデータが2回投稿されるのを防ぎます。
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results_stab(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
```

5. ビュー呼ぶための設定(urls.py で URL の対応付け)

```python
# polls/urls.py
# index ビューを URLconf に紐付ける
# URLからビューを得るために、Django は「URLconf」と呼ばれているものを使います。
# URLconf はURLパターンをビューにマッピングします。
from django.urls import path

from . import views

# URLconf に名前空間を追加
app_name = 'polls'

# 山括弧を使用すると、URLの一部が「キャプチャ」され、
# キーワード引数としてビュー関数に送信します。
# テンプレートタグ{％url％}によって呼び出される「name」
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/specifics/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# mysite/urls.py(リクエストから呼ばれる)
from django.contrib import admin
from django.urls import include, path

# /polls/34/にリクエストが来た場合
# `polls/` にマッチした箇所を見つけた後、一致した文字列 ("polls/") を取り除き、
# 残りの文字列である "34/" を次の処理のために 『polls.urls』 の URLconf に渡します。
# これは '<int：question_id>/' に一致し、結果として下記のように detail() が呼び出されます。
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

6. Database の設定(初期化)

```ps1
#  INSTALLED_APPS の設定を参照するとともに、
# mysite/settings.py ファイルのデータベース設定に従って
# 必要なすべてのデータベースのテーブルを作成します。
python manage.py migrate
```

7. モデルの作成

```python
# polls/models.py
import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
```

8. モデルを有効にする

```python
# mysite/settings.py¶
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

9. モデルの適応

```ps1
# makemigrations を実行することで、
# Djangoにモデルに変更があったことを伝え、
# そして変更を マイグレーション の形で保存
# マイグレーションはDjangoがモデルの変更を保存する方法です。
# データベーススキーマでもあります
python manage.py makemigrations polls
```

10. 作成したモデルのテーブルをデータベースに作成

```ps1
python manage.py migrate
```

11. Django Admin の設定

```ps1
# 管理ユーザーを作成する
python manage.py createsuperuser
```

12. Poll アプリを admin 上で編集できるようにする

```python
# polls/admin.py
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

13. テンプレートの作成
    [テンプレートガイド](https://docs.djangoproject.com/ja/2.2/topics/templates/)  
    polls/urls.py の  
    "path()関数"で"name"引数を定義したので"{％url％}"が使用可能  
    "app_name"で URLconf に名前空間を追加したことで"polls:"が使用可能

```html
<!--polls/templates/polls/index.html-->
{% if latest_question_list %}
<ul>
  {% for question in latest_question_list %}
  <!--
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        -->
  <li>
    <a href="{% url 'polls:detail' question.id %}"
      >{{ question.question_text }}</a
    >
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No polls are available.</p>
{% endif %}

<!--polls/templates/polls/detail.html-->
<!--POST フォーム(データを改ざんされる恐れのある) を作成しているので、
    クロス サイトリクエストフォージェリを心配する必要があります。
    手短に言うと、自サイト内を URL に指定した POST フォームには全て、 
    {% csrf_token %} テンプレートタグを使うべきです。
-->
<h1>{{ question.question_text }}</h1>

{% if error_message %}
<p><strong>{{ error_message }}</strong></p>
{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
  {% csrf_token %}
  <!--forloop.counter は、 for タグのループが何度実行されたかを表す値-->
  {% for choice in question.choice_set.all %}
  <input
    type="radio"
    name="choice"
    id="choice{{ forloop.counter }}"
    value="{{ choice.id }}"
  />
  <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label
  ><br />
  {% endfor %}
  <input type="submit" value="Vote" />
</form>

<!--polls/templates/polls/results.html¶-->
<h1>{{ question.question_text }}</h1>

<ul>
  {% for choice in question.choice_set.all %}
  <li>
    {{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize
    }}
  </li>
  {% endfor %}
</ul>

<a href="{% url 'polls:detail' question.id %}">Vote again?</a>
```

14. 汎用ビュー
    ビューは基本的な Web 開発の一般的なケース、  
    URL を介して渡されたパラメータに従ってデータベースからデータを取り出し、  
    テンプレートをロードして、レンダリングしたテンプレートを返します。  
    これはきわめてよくあることなので、  
    Django では、汎用ビュー（generic view）というショートカットを提供しています。  
    汎用ビューとは、よくあるパターンを抽象化して、  
    Python コードすら書かずにアプリケーションを書き上げられる状態にしたものです。  
    poll アプリを汎用ビューシステムに変換して、 コードをばっさり捨てる。  
     1. URLconf を変換する。 2. 古い不要なビューを削除する。 3. 新しいビューに Django の汎用ビューを設定する。  
    [汎用ビューガイド](https://docs.djangoproject.com/ja/2.2/topics/class-based-views/)

```python
# polls/urls.py
# 1. URLconf を変換する。
# <question_id> から <pk> に変更
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

# polls/views.py¶
# 2. 古い不要なビューを削除する。
# ここでは、ListView(オブジェクトのリストを表示する)
# DetailView(あるタイプのオブジェクトの詳細ページを表示する) という二つの概念を抽象化
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """最後に公開された5つの質問を返します。"""
        return Question.objects.order_by('-pub_date')[:5]

#  "pk" という名前で URL からプライマリキーをキャプチャして渡す
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    # context_object_nameはデフォルトでquestionになる


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
```
15. 自動テストの導入
```python
# polls/tests.py
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

"""テスト用のメソッドとして、test で始まるメソッドを作成。"""
class QuestionModelTests(TestCase):

  def test_was_published_recently_with_future_question(self):
      """
      was_published_recently（）は、pub_dateが将来の質問に対してFalseを返します。
      """
      time = timezone.now() + datetime.timedelta(days=30)
      future_question = Question(pub_date=time)
      self.assertIs(future_question.was_published_recently(), False)

  def test_was_published_recently_with_old_question(self):
      """
      was_published_recently（）は、pub_dateが1日より古い質問に対してFalseを返します。
      """
      time = timezone.now() - datetime.timedelta(days=1, seconds=1)
      old_question = Question(pub_date=time)
      self.assertIs(old_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
      """
      was_published_recently（）は、pub_dateが月末以内の質問に対してTrueを返します。
      """
      time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
      recent_question = Question(pub_date=time)
      self.assertIs(recent_question.was_published_recently(), True)

```

16. テストの実行
```ps1
py manage.py test polls
```
```ps1
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_was_published_recently_with_future_question (polls.tests.QuestionModelTests)
「was_published_recently（）」は、pub_dateが将来の質問に対してFalseを返します。
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\work\python\django\mysite\polls\tests.py", line 17, in test_was_published_recently_with_future_question
    self.assertIs(future_question.was_published_recently(), False)
AssertionError: True is not False

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (failures=1)
Destroying test database for alias 'default'...
```
```ps1
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
Destroying test database for alias 'default'...
```
### プログラム実行順

1. mysite/manage.py
1. mysite/__init__.py
1. mysite/settings.py
1. mysite/opps.py
1. polls/models.py
1. polls/admin.py
1. mysite/manage.py

1. mysite/
```
