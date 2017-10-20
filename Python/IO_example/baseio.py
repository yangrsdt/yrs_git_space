#!/usr/bin/python
# coding = utf8

#读写文件
f = open("/home/yangrs/Desktop/DTSTUDIO-1399","r")
# f.writable("1")
print(f.read())
f.close()

#StringIO
from io import StringIO
f1 = StringIO()
a = f1.write("1111")
print(a)
print(f1.getvalue())

f = StringIO("Hello!\nPython!!")
while 1:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

#BytesIO
from io import BytesIO
f2 = BytesIO()
f2.write("中文".encode("utf-8"))
print(f2.getvalue())

#操作文件和目录
import os
print(os.uname())
print(os.environ)
print(os.path.abspath("."))
print(os.path.join("/users/name","yangrs"))
print(os.path.split("/user/name/yangrs"))



dir = [x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1] == ".py"]
# for x in dir:
#     print(os.path.splitext(x))
print(dir)
print(os.listdir("."))

def find_p(path,str):
    if path != None and str != "":
        for x in os.listdir(path):
            if os.path.isdir(x):
                find_p(os.path.join(path,x),str)
            elif str in x:
                print(os.path.join(path,x))
find_p(os.path.abspath("."),"i")


#序列化
import pickle
d = dict(name = "yrs",age = 23)
f = open("/home/yangrs/Desktop/pickle.txt","wb")
pickle.dump(d,f)
f.close()

f = open("/home/yangrs/Desktop/pickle.txt","rb")
d = pickle.load(f)
print(d)

#JSON
import json
d = dict(name = "yrs",age = 23)
f = open("/home/yangrs/Desktop/pickle.txt","w")
json.dump(d,f)
f.close()
