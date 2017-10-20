#!/usr/bin/python
# -*- coding: utf8 -*-

#默认参数

def add_end(L = None):
	if L is None:
		L = []
	L.append("END")
	print(L)
	return L

add_end()


#可变参数

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	print(sum)
	return sum

calc(1,2,3)

#关键字参数

def person(name,age,**detail):
	print("name:",name,"age:",age,"detail:",detail)
	print("name:"+name+",""age:"+str(age)+",""detail:"+str(detail))

person("A",20,city = "Hangzhou",address = "西湖区")

#五种参数实例

def person(name,age=23,*args,city,**detail):
	print("name:"+name+","
		"age:"+str(age)+","
		"args:"+str(args)+","
		"city:"+str(city)+","
		"detail:"+str(detail))

person("yang",args=["nanren"],city="Hangzhou",address = "西湖区")

#递归函数

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

#print(fact(1000))

#递归函数(尾递归优化)
def fact_weidigui(n):
	return fact_iter(n,1)

def fact_iter(num,result):
	if num == 1:
		return result
	return fact_iter(num - 1,num * result)

#print(fact_weidigui(1000))

#汉诺塔

def hannuo(n,A,B,C):
	if n == 1:
		move(1,A,C)
	else:
		hannuo(n-1,A,C,B)
		move(n,A,C)
		hannuo(n-1,B,A,C)

i = 1
max = 0
def move(n,f,t):
	global i
	global max
	if n > max:
		max = n 
	print("第%d步：将%d号盘子从%s柱--->%s柱  目前最大盘子为%s" %(i,n,f,t,max))
	i+=1

n = int(input())
hannuo(n,"A","B","C")	