from collections import frozenmap

dict1 = {'a': 1, 'b': 2}
dict1['c'] = 3
print(dict1)

h = frozenmap()
print("inited", h)
print("members", dir(h))
print(len(h))
print(h.get("hi"))
h2 = h.set('a', 'b')
print("setted")
assert h is not h2
assert len(h) == 0
assert len(h2) == 1
assert h2['a'] == 'b'
h3 =  h2.set('b', 10)