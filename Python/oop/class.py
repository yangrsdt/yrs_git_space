#!/usr/bin/python
# coding = utf8

#调用限制
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def print_s(self):
        print("%s : %s" % (self.__name,self.__score))

s1 = Student("y","100")
s1.set_score("50")
print(s1.get_score())

#继承和多态
class Animal(object):
    def run(self):
        print("animals are living")

class Dog(Animal):
    def run(self):
        print("dogs are living")

class Stone(object):
    def run(self):
        print("stone is dead")

def run_s(x):
    x.run()

run_s(Animal())
run_s(Dog())
run_s(Stone())

#获取对象信息
print(dir("abc"))

#类属性和实例属性
class T():
    name = "student"

s = T()
print(s.name)