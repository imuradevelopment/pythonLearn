set_a = {1, 2, "a", "b", 1, "a"}
set_b = set([1, 2, "a", "b", 1, "a"])
print("set_a {0}".format(set_a))
print("set_b {0}".format(set_b))


set_a = {7, 9, 2}
set_b = {9, 22, 2, 25}

set_b_25 = 25 in set_b
set_b_0 = 0 in set_b
print("set_b_25 {0}".format(set_b_25))
print("set_b_0 {0}".format(set_b_0))

print("len(set_a) {0}".format(len(set_a)))

set_b.add(12)
set_b.remove(25)
set_b.discard(0)
set_c = {"a", "b", "c"}

set_union = set_a.union(set_b)
print("set_union {0}".format(set_union))

set_unions = set_a.union(set_b, set_c)
print("set_unions {0}".format(set_unions))

set_intersection = set_a.intersection(set_b, set_c)
print("set_intersection {0}".format(set_intersection))

set_difference = set_a.difference(set_b)
print("set_difference {0}".format(set_difference))

set_differences = set_a.difference(set_b, set_c)
print("set_differences {0}".format(set_differences))

set_difference_1 = set_a.difference(set_b)
set_difference_2 = set_b.difference(set_a)
print("set_difference_1 {0}".format(set_difference_1))
print("set_difference_2 {0}".format(set_difference_2))

set_symmetric_difference = set_a.symmetric_difference(set_b)
print("set_symmetric_difference {0}".format(set_symmetric_difference))

set_big = {"a", "b", "c"}
set_small = {"a", "b"}
set_issuper = set_big.issuperset(set_small)
set_issub = set_small.issubset(set_big)
print("set_issuper {0}".format(set_issuper))
print("set_issub {0}".format(set_issub))
