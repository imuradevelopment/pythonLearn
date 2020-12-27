a = 1
if a == 1:
    print("a is 1")


a = 1
if a == 1:
    print("a is 1")
else:
    print("a is not 1")


a = 1
if a == 1:
    print("a is 1")
elif a == 2:
    print("a is 2")
elif a == 3:
    print("a is 3")
else:
    print("a is not 1,2,3")


a = 1
b = ['a', 'b', 'c']

if not (a == 1 and 'z' in b) or len(b) != 3:
    print("ok!")


x = None
if x is None:
    print("x is none")

y = False
if y is not None:
    print("y is not none")
