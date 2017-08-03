class Number:
    def __init__(self,start):#构造函数
        self.data = start
    def __sub__(self,other):
        return Number(self.data - other)#减号
    
#########__getitem__和__setitem__#####################
class Indexer:
    def __getitem__(self,index):
        return index ** 2

X = Indexer()
print(X[2])

class Indexer:
    data = [1,2,3,4,5,6,7,8,9]
    def __getitem__(self,index):
        print('getitem:',index)
        return self.data[index]
    def __setitem__(self,index,value):
        print('setitem',index,value)
        self.data[index] = value

X = Indexer()
print(X[0],X[1],X[2],X[2:6],X[1:7:2],sep = '\n')
X[3] = 100
print(X[3])
X[2:6] = [100,101]
print(X.data)

#############迭代：__iter__和__next__################
#Python中所有的迭代环境都会先尝试__iter__方法，在尝试__getitem__。
class Squares:
    def  __init__(self,start,stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5):
    print(i,end='  ')
X = Squares(1, 5)
I = iter(X)
print(next(I),next(I),next(I),next(I))

#让对象支持多迭代
class SkipIterator:
    def  __init__(self,wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2  #迭代步大小
            return item

class SkipObject:
    def __init__(self,wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)  #放回一个新的迭代对象
    
if __name__ == '__main__':
    alpha = 'abcdefghijk'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I),next(I),next(I))
    
    for x in skipper:
        for y in skipper:
            print(x+y,end='  ')
            
#__contains__判断成员关系
#优先级:contains--iter--getitem
print('')
class Iters:
    def __init__(self,value):
        self.data = value
    def __getitem__(self,i):
        print('get[%s]:'%i,end = ' ')
        return self.data[i]
    def __iter__(self):
        print('iter=>',end=' ')
        self.ix = 0
        return self
    def __next__(self):
        print('next:',end=' ')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self,x):
        print('contains:',end=' ')
        return x in self.data

X = Iters([1,2,3,4,5])
print(3 in X)

for i in X:
    print(i,end = '|')
print()
print([i ** 2 for i in X])
print(list(map(bin,X)))

I = iter(X)
while True:
    try:
        print(next(I),end = '@')
    except StopIteration:
        break;
    
################__getattr__和__setattr__###########
class GetSet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __getattr__(self,attrname):
        print('----get----')
        if attrname == 'age':
            return self.age
        elif attrname =='name':
            return self.name
        else:
            raise AttributeError
    def __setattr__(self,attrname,value):
        print('----set----')
        if attrname == 'age':
            self.__dict__[attrname] = value  #不能直接赋用值语句self.age = value ,这样会导致无限循环
        elif attrname =='name':
            self.__dict__[attrname] = value
        else:
            raise AttributeError  
        
X = GetSet('Tom', '22')
print(X.name)
X.age = '33'
print(X.age)

#################__call__##################
class Callee:
    def __call__(self,*pargs,**kargs):
        print('Called:',pargs,kargs)

C = Callee()
C(1,2,3)#调用实体本身时会调用__call__方法

################对象析构函数：__del__##########
class Life:
    def __init__(self,name='unknown'):
        print('Hello',name)
        self.name = name
    def __del__(self):
        print('Goodbye',self.name)
        
brian = Life("Brian")
brian = 'lost'

##############静态方法：staticmethod()##########
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances:",Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)
#使用装饰器
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    @staticmethod
    def printNumInstances():
        print("Number of instances:",Spam.numInstances)
    
    
a = Spam()
a = Spam()
a = Spam()
Spam.printNumInstances()
a.printNumInstances()

##############类函数：classmethod############
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances:",cls.numInstances)
    printNumInstances = classmethod(printNumInstances)
#使用装饰器
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    @classmethod
    def printNumInstances(cls):
        print("Number of instances:",cls.numInstances)
    
a = Spam()
a = Spam()
a = Spam()
Spam.printNumInstances()
a.printNumInstances()

###############装饰器例子################
#函数装饰器
class tracer:
    def __init__(self,func):
        self.calls = 0
        self.func = func
    def __call__(self,*args):
        self.calls += 1
        print('call %s to %s' % (self.calls,self.func.__name__))
        self.func(*args)
@tracer
def spam(a,b,c):
    print(a,b,c)
    
spam(1, 2, 3)
spam('a', 'b', 'c')

#类装饰器
def decorator(aClass):
    aClass.show()
@decorator
class C:
    def show():
        print('c-->show')
#与下面代码等价
def decorator(aClass):
    aClass.show()
class C:
    def show():
            print('c-->show')    
decorator(C)