#!/usr/bin/python
# coding=utf8
import math

#定义函数
def getMax(x,y):
	if x > y:
		return x
	else:
		return y

#a = getMax(input(),input())
#print(a)

#计算二元一次方程
def jisuan(a,b,c):
	if not (isinstance(a,int) or isinstance(b,int) or isinstance(c,int)):
		raise TypeError("bad operand type")
	if b*b < 4*a*c:
		print("方程无解")
	elif b*b == 4*a*c:
		print("方程有两个相同解，为:"+"%.3f" %(-b/(2*a)))
	else:
		x = (-b + math.sqrt(b*b-4*a*c)) / (2*a)
		y = (-b - math.sqrt(b*b-4*a*c)) / (2*a)
		return x,y

z = jisuan(2,3,1)
print(z)