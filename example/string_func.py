text1 = "abc"
a_in_text = "a" in text1
b_in_text = "d" in text1
print("in_text_a {0}".format(a_in_text))
print("in_text_d {0}".format(b_in_text))
text2 = "abc" + "def"
print("abc + def {0}".format(text2))
print("abc * 3 {0}".format("abc" * 3))
print("text2[3] {0}".format(text2[3]))
print("text2[-1] {0}".format(text2[-1]))
print("text2[1:4] {0}".format(text2[1:4]))
print("text2[0:6:2] {0}".format(text2[0:6:2]))
print("text2[0:6:3] {0}".format(text2[0:6:3]))
print("len(text2) {0}".format(len(text2)))
print("min(text2) {0}".format(min(text2)))
print("max(text2) {0}".format(max(text2)))
print("{0},{1},{2}".format(10,"20",str(10)+"20"))
