d = {'key1': 'Value1', 'key2': 'Value2'}

print("len(d) {0}".format(len(d)))
print("min(d) {0}".format(min(d)))
print("max(d) {0}".format(max(d)))

dic_d_key1 = 'key1' in d
dic_d_key3 = 'key3' in d
print("dic_d_key1 {0}".format(dic_d_key1))
print("dic_d_key3 {0}".format(dic_d_key3))

print("d[key1 {0}".format(d['key1']))
print("d[key1 {0}".format(d.get('key1')))
print("d[key1 {0}".format(d.get('key3')))
print("d[key1 {0}".format(d.get('key3', 'No Existance')))
d['key1'] = 'NewValue1'
d['key3'] = 'Value3'
del d['key2']
print("d {0}".format(d))
print(d.pop('key3'))
print("d {0}".format(d))
