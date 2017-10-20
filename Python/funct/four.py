#!/usr/bin/python
# coding = utf8

#高阶函数

def abs(x,y):
	return x + y

f = abs

def gaojie(a,b,c):
	return c(a,b)

print(gaojie(1,2,f))

#map/reduce

#map
L1 = ["adam","LISA","barT"]

def normalize(name):
	first = name[0].upper()
	second = name[1:].lower()
	return first + second
	#return name.capitalize()
L2 = list(map(normalize,L1))
print(L2)

#reduce

from functools import reduce

def prod(L):
	return reduce(lambda x,y:x * y,L)
print("3 * 5 * 7 * 9 =",prod([3,5,7,9]))

#map and reduce 

def str2float(s):
	L = s.split(".",1)
	return reduce(lambda x,y:x * 10 + y,map(int,L[0])) + reduce(lambda x,y:x * 10 + y,map(int,L[1]))/(10**len(L[1]))

s = "196.25"
L = list(map(int,"25"))
print(str2float("123.456"))
print(str(len(L)))
print(str(2**5))

#filter

def is_palindrome(n):
	m = list(str(n))
	for i in range(len(m)):
		return m[i] == m[len(m)-1]
output = filter(is_palindrome,range(1,1000))
print(list(output))

#sorted

LL = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0]
L = sorted(LL,key = by_name)
print(L)


#闭包

def count():
	return list(map(lambda j:lambda:j * j,range(1,4)))

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())

#装饰器
import time
import functools

#不带参数的装饰器
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print("begin call %s()" % func.__name__)
		f = func(*args,**kw)
		print("end call")
		return f
	return wrapper

@log
def now():
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print(t)

now()

#带参数的装饰器
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print("%s begin call %s()" % (text,func.__name__))
			f = func(*args,**kw)
			print("end call")
			return f
		return wrapper
	return decorator

@log("execute")
def now():
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print(t)

now()

#带参和无参的装饰器
import types

def log(text):
	if isinstance(text,types.FunctionType):
	#if callable(text)
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print("begin call %s()" % text.__name__)
			f = func(*args,**kw)
			print("end call")
			return f
	else:
		def decorator(func):
			def wrapper(*args,**kw):
				print("%s begin call %s()" % (text,func.__name__))
				f = func(*args,**kw)
				print("end call")
				return f
			return wrapper
		return decorator

@log("execute")
def now():
	t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	print(t)

now()