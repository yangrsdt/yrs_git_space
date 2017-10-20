#namedtuple

from collections import namedtuple

Circle = namedtuple("Circle",["x","y","r"])
c = Circle(1,2,3)
print(c.x)

from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)