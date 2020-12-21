def odd_or_even():
  for i in range(1, 6):
    if i % 2 != 0:
      print("{0} is odd".format(i))
    elif i % 2 != 1:
      print("{0} is even".format(i))
    else:
      print("{0} is not even and not odd.".format(i))

if __name__ == "__main__":
    odd_or_even()

# -*- coding: utf-8 -*-
print("こんにちは世界")

str = 'jhbjkj'
str2 = """sdvc
b.jb"""

print("{0},{1}".format(str,str2))
