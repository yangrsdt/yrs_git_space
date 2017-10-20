#!/usr/bin/python
name = input();
print('hello world',name)

s = 'hello \'adam\''
print(s)

s1 = r'hello,"adam"'
print(s1)

s2 = r'''hello,
adam'''
print(s2)

s3 = ord('A')
print(s3)

s4 = chr(25991)
print(s4)

s5 = b'Abc'
print(s5)

s6 = '中文'.encode('utf-8')
print(s6)

s7 = 'hello %s' % 'world'
print(s7)

list = [1,2,3]
list.insert(0,0)
print(len(list))
list.pop()
print(list)
for l in list:
	print(l)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0],'\n'+L[1][1],'\n'+L[2][2])

tuple1 = (1,2,3)
tuple2 = (1,[2,3])
print(tuple1)
print(tuple2)

sum = 0
for x in range(101):
	sum = sum + x
print(sum)

dict = {"1":"x","1":"y"}
print(dict.get("1"))

s1 = set([1,2,3])
s2 = set([1,3,4])
print(s1 & s2)
print(s1 | s2)

print(bool(0))

n1 = 255
n2 = 1000
print(hex(n1) ,hex(n2))

n1 = 255
n2 = 1000
print('n1的为:'+str(hex(n1)),'n2的为:'+str(hex(n2)))