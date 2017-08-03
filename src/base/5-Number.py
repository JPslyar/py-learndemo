i = 190
#将数字转换为16、8、2进制
print(hex(i))
print(oct(i))
print(bin(i))

#将数字转换为十进制
print(int("100010",2))
print(int('100',8))
print(int('40',16))
print(int('0x40',16))

#创建复数
z = complex(5,6)
print(z)

#数字显示格式
num = 100000000.0/ 3.0
print('%e' % num)
print('%0.3f' %num)
print('{0:4.2f}'.format(num))

#str与repr函数将任意对象转换为字符串形式
print(repr(num))#默认交互模式回显
print(str(num))#打印模式

#floor与trunc
import math
print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))

#eval()函数，将会把参数字符串当做Python代码执行
i = eval('3>2')
print(i)

#bit_length()查看二进制长度
print((256).bit_length())

#其它内置数学工具
print(math.pi)
print(math.e)
print(math.sin(2 * math.pi / 180))
print(math.sqrt(144))
print(pow(2, 4))
print(abs(-42.0))
print(sum((1,2,3,4,5)))
print(min(1,2,3,4,5))
print(max(1,2,3,4,5))
print(round(2.567),round(2.456),round(2.456,2))

import  random
print(random.random())
print(random.randint(1,10))
print(random.choice(['Life of Brian','Holy Grail','Meaning of Life']))

import decimal
decimal.getcontext().prec = 4 #设置全局的小数点精度
dec = decimal.Decimal(1) / decimal.Decimal(7)
print(dec)

from fractions import Fraction
x = Fraction(1,3)
print(x)
print((2.5).as_integer_ratio())#转换为比例

x = set('abcde')
y = set('bdyxz')
z = x.intersection(y)#或
m = x.union(y)#与
n = x.issubset(range(1,256))#范围
print(z,m,n)
z.add('SP')
print(z)
z.update(set(['H','J','K']))
print(z)
z.remove('J')
print(z)
#集合本身不可改变，集合本身只能包含不可变的对象类，因此无法包含列表、字典，但可以包含元组

e = {'bob','sue','ann','vic'}
m = {'tom','sue'}
print('bob' in e)
print(e & m)
print(e | m)
print(e ^ m)

print(type(True))
print(isinstance(True,int))