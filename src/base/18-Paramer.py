#############################################################
#传的是值而非引用
x = [1,2,3]
y = 1 
def f(x,y):
    print(x,y)
    x = [6,6,4]
    y = 2
    print(x,y)
f(x,y)
print(x,y)

def changer(a,b):
    a = 2
    b[0] = 'spam'
X = 1
Y = [1,2]
changer(X, Y[:])#传的为Y的拷贝
print(X,Y)
changer(X, Y)
print(X,Y)

##################传参及调用##################################
def f(a,b,c):
    print(a,b,c)
f(1, 2, 3)
f(a=1, b='2', c=[1])
f(1,c=[1],b='1',)#若有键值形式的参数，那么只能出现一个无key的参数


def f(a,b=2,c=3):
    print(a,b,c)
f(1, 2, 3)
f(a=1, b='2', c=[1])
f(1,c=[1],b='1',)
f(3)

#加包的参数
def f(*args):#将会把传入的参数以元组的形式封装
    print(args)
f()
f(1,2,3,4)

def f(**args):#只对键值对参数有效，将会把传入的参数以字典的形式封装
    print(args)
f()
f(a=1,b=2,c=3,d=4)

#加包参数混合
def f(a,b=1,*pargs,**kargs):
    print(a,b,pargs,kargs)
f(2,'r',4,5,m='g',n='m')

#参数解包
def f(a,b,c,d):
    print(a,b,c,d)
args = (1,2,3,4)
f(*args)
f(*(1,2),**{'d':4,'c':3})
f(1,*(2,3),**{'d':4})
f(1,*(2,3),d=4)
f(1,*(2,),d=4,**{'c':3})#顺序必须为值、元组、键值、字典

#keyword-only可用*号强制后面的参数必须按照名称来赋值
def kwonly(a,*,b,c='s'):
    print(a,b,c)