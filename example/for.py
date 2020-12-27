for i in range(5):
   print("{0}".format(i))


for i in range(1, 10):
   print("{0}".format(i))


a = ["a", "b", "c", "d", "e"]
for idx, elem in enumerate(a):
   print("{0} = {1}".format(idx, elem))


a = ["a", "b", "c", "d", "e"]
for idx in enumerate(a):
   print("{0}".format(idx))


a = ["ok", "ok", "ok", "ng", "ok"]
i = 0
while a[i] == 'ok':
    print("a[{0}] is ok".format(i))
    i = i + 1


a = ["ok", "ok", "ok", "ng", "ok"]
i = 0
while a[i] == 'ok':
    print("a[{0}] is ok".format(i))
i = i + 1


i = 0
while i < 10:
    i = i + 1
    if i < 3:
        continue
    print("i is {0}".format(i))
    if i == 5:
        break

print("final i is {0}".format(i))


for i in range(3):
    print("{0}".format(i))
else:
    print("for loop done")

while i < 5:
    i = i + 1
    print("{0}".format(i))
else:
    print("while loop done")


for i in range(3):
    print("{0}".format(i))

print("for loop done")

while i < 5:
    i = i + 1
    print("{0}".format(i))

print("while loop done")


