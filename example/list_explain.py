# Listの宣言
z = ['a', 'b', 'c']
x = [1, 2, 3.4, "a", z]
# in
a_in_list = 'a' in z
d_in_list = 'd' in z
print("a_in_list {0}".format(a_in_list))
print("d_in_list {0}".format(d_in_list))
# プロパティ値取得
print("len(z) {0}".format(len(z)))
print("max(z) {0}".format(max(z)))
print("min(z) {0}".format(min(z)))
# 一部指定
print("x[1] {0}".format(x[1]))
print("x[-1] {0}".format(x[-1]))
print("x[1:3] {0}".format(x[1:3]))
print("x[1:] {0}".format(x[1:]))
print("x[:3] {0}".format(x[:3]))
# 一部代入
x[1:4] = ["taro", "jiro"]
print("changed x {0}".format(x))
# 結合
a = z + x
print("a {0}".format(a))

# 空のリスト
y = []  # create empty list
# append, remove, reverse, sort
y.append("spam")
print("y {0}".format(y))
y.append("ham")
print("y {0}".format(y))
y2 = ["egg", "ham"]
y.append(y2)
y.remove('ham')
print("y {0}".format(y))
z.reverse()
print("z {0}".format(z))
sortlist = [0, 1, 3, 7, 5]
sortlist.sort()
print("sort {0}".format(sortlist))
