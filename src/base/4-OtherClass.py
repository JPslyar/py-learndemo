X = set('spam')
Y = {'h','a','m'}
print(X,Y)
print(X&Y)
print(X|Y)
print(X-Y)

print(1/3)
import decimal
d = decimal.Decimal('3.141')
print(d+1)

decimal.getcontext().prec = 2
de = decimal.Decimal('1.00') / decimal.Decimal('3.00')
print(de)

from fractions import Fraction           #分数
f = Fraction(2,3)
print(f + 1)
print(f + Fraction(1,2))

print(1 > 2)
X = None
print(X)
L = [None] * 100
print(L)

print(type(L))#获取类的类型
print(type(type(L)))

if type(L) == type([]):#判断类的类型
    print('yes')
if type(L) == list:
    print('yes')
if isinstance(L,list):
    print('yes')


###########自定义类
class Worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def setName(self,name):
        self.name = name 
    def getName(self):
        return self.name.split()[-1]
    def setPay(self,pay):
        self.pay = pay
    def getPay(self):
        return self.pay
    def fiveRaise(self,percent):
        self.pay *= (1.0 + percent)

bob = Worker('Bob Smith',50000)
sue = Worker('Sue Jones',60000)
#bob.setName('Bob Smith')
#bob.setPay(50000)
#sue.setName('Sue Jones')
#sue.setPay(60000)
print(bob.getName())
print(sue.getName())
sue.fiveRaise(0.2)
print(sue.pay)
        