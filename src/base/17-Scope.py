X = 99
def func(Y):
    Z = X + Y
    return Z
print(func(1))

X = 88
def func():
    X = 100
func()
print(X)

X = 88
def func():
   global X 
   X = 99
func()
print(X)

##################其它访问全局变量的方法###############################
var = 999
def local():
    var = 0  #本地
    return var
def glob1():
    global var  #全局
    var += 1
    return var
def glob2():
    import Test
    Test.var += 1  #全局
    return Test.var
def glob3(): 
    import sys
    glob = sys.modules['Test']
    glob.var += 1  #全局
    return glob.var
def test():
    return [local(),glob1(),glob2(),glob3()]

print(test())

################嵌套作用域##############

Y = 99
def f1():
    Y = 88
    def f2():
        print(Y)   #此处打印88
    f2()
f1()


##############工厂函数##################
def marker(N):
    def action(X):
        return X ** N
    return action

f = marker(2)#f记住了N-->2;g记住了N-->3
g = marker(3)
print(f(3))
print(g(3))

##############使用默认参数保留嵌套作用域#########
def f1():
    X = 88
    def f2(Y=X):#X为f1中的88，同时将其值赋给f2的参数Y使其成为默认参数值
        print(Y)
    f2()#再不传入参数情况下Y=88
f1()

#非嵌套函数写出等价形式
def f1():
    X = 88
    f2(X)
def f2(X):
    print(X)
f1()

################lambda函数的使用################
def func(X):
    action = (lambda n ,X = X: n ** X)
    return action
f = func(2)
print(f(5,3))

##############循环中变量的应用###############
def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x:i ** x)
    return acts
acts = makeActions()
print(acts[0](2),acts[1](2),acts[2](2))

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x,i=i:i ** x)
    return acts
acts = makeActions()
print(acts[0](2),acts[1](2),acts[2](2))

############任意作用域的嵌套#############
def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
    f2()
f1()        

#############nonlocal关键字使用###########
def tester(start):
    state = start
    def nested(label):
        nonlocal state   #调用nonlocal时，其变量必须已经赋过值，而global则无此需求
        print(label,state)  
        state += 1    
    return nested
f = tester(0)
f('jiangpeng')
f('haha')

def tester(start):
    state = start
    def nested(label):
        state = 1    #此处state为nested里面的新变量；若用print(state)或state += 1之类的语句需要事先申明：nonlocal state
    return nested
f = tester(0)
f('jiangpeng')
f('haha')

###############全局共享状态#############
def tester(start):
    global state
    state = start
    def nested(label):
        global state
        print(label,state)
        state += 1
    return nested
F = tester(0)
F('jiang')
F('peng')

###############实用类的状态###############
class tester: 
    email = 'qq'
    def __init__(self,start):
        self.state = start
    def change(self):
        self.state += 1
        self.age = 12
        print(self.state,self.sex)
    def __call__(self):
        print(state,self.age)
F = tester(0)
F.sex = '男'
F.change()
F.change()
F()
print(F.age)
print(F.email)
#类可以随时添加属性和方法

#######################使用函数属性的状态###############
def  tester(start):
    def nested(label):
        print(label,nested.state)
        nested.state += 1
    nested.state = start #定义nested的属性state并给初值———可将函数也可看为对象来给与属性
    return nested
F = tester(0)
F('label')
F('label')

