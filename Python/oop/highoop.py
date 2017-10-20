#!/usr/bin/python
# coding = utf8

#使用@property
class Student():

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

s = Student()
s.name = "nanshou"
print(s.name)

class Screen(object):
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self,width):
        self.__width = width

    @property
    def height(self):
        return self.__width

    @height.setter
    def height(self,height):
        self.__height = height

    @property
    def resolution(self):
        return self.__width * self.__height

s1 = Screen()
s1.width = 1024
s1.height = 768
print(s1.resolution)
assert s1.resolution == 786432, '1024 * 768 = %d ?' % s1.resolution


#多重继承
class Father(object):
    def func(self):
        print("生父打儿子")
class Laowang(object):
    def func(self):
        print("老王打儿子")
    def fun1(self):
        print("我才是你亲爹")
class Stepfather():
    def func(self):
        print("我不打你")
    def fun1(self):
        print("我不是你爹")
class Child(Father,Laowang,Stepfather):
    pass
c = Child()
c.func()
c.fun1()

import inspect
class D(object):
    pass

class E(object):
    pass

class F(object):
    pass

class C(D, F):
    pass

class B(E, D):
    pass

class A(B, C):
    pass

if __name__ == '__main__':
    print(inspect.getmro(A))

#定制类

#__str__

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    #__repr__ = __str__

print(Student("Nezha"))
s2 = Student("Nezha")
print(s2)

#__iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1                    # 初始化两个计数器a，b

    def __iter__(self):
        return self                              # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 1:                      # 退出循环的条件
            raise StopIteration()
        return self.a                            # 返回下一个值

for n in Fib():
    print(n)

#__getitem__
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b,a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            L = []
            a,b = 1,1
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a + b
            return L
print(Fib()[0:5])

#__getattr__
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def users(self,user):
        return Chain('%s/%s' % (self._path,user))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('yrs').users('fzl').repos)

#枚举类
from enum import Enum ,unique

Month = Enum("Month",('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name, '=>', member, ',',member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6




#元类