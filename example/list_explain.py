z = ['a','b','c']
x = [1, 2, 3.4, "a", z]
a_in_list = 'a' in z
d_in_list = 'd' in z
print("a_in_list {0}".format(a_in_list))
print("d_in_list {0}".format(d_in_list))
print("len(z) {0}".format(len(z)))
print("max(z) {0}".format(max(z)))
print("min(z) {0}".format(min(z)))
print("x[1] {0}".format(x[1]))
print("x[-1] {0}".format(x[-1]))
print("x[1:3] {0}".format(x[1:3]))
print("x[1:] {0}".format(x[1:]))
print("x[:3] {0}".format(x[:3]))
x[1:4] = ["taro","jiro"]
print("changed x {0}".format(x))
a = z + x
print("a {0}".format(a))

y = [] #create empty list
y.append("spam")
print("y {0}".format(y))
y.append("ham")
print("y {0}".format(y))
y2 = ["egg","ham"]
y.append(y2)
y.remove('ham')
print("y {0}".format(y))

z.reverse()
print("z {0}".format(z))

sortlist = [0,1,3,7,5]
sortlist.sort()
print("sort {0}".format(sortlist))
