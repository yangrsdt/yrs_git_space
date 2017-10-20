#!/usr/bin/python
# coding = utf8

#切片

L=[]
for i in range(20):
	L.append(i)

print(L[0:10:2])
print(L[-1])
print(L[::2])
print(L[:])

s = "abcdef"
print(s[:3])
tuple = (1,2,3,4,5)
print(tuple[:3])

#迭代

dict = {"a":1,"b":2,"c":3}

for key in dict:
	print(key)

for value in dict.values():
	print(value)

for key,value in dict.items():
	print(key,value)

for x in L:
	print(x)

#列表生成式

list = ["Hello","World","Apple",18,None]
list=[s.lower() for s in list if isinstance(s,str)]
print(list)

#杨辉三角

def triangles(max):
	b,n = [1],0
	while n < max:
		n += 1
		yield b
		b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]

max = int(input())

for x in triangles(max):
	print(x)

#迭代器

from collections import Iterator
flag = isinstance(triangles(max),Iterator)
print(flag)