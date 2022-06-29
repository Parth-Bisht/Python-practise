a = {1,2,5,1,6}
print(type(a))
print(a)

c = {}
print(type(c))

b = set()
print(type(b))
b.add(4)
b.add(5)
b.add((4,5,6))
print(b)
print(len(b))

b.remove(5)
print(b)

print(b.pop())
print(b)
b.clear()
print(b)