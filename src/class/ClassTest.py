class FirstClass:
    name = 'hahha'  # 顶层赋值运算创造属性

    def setdata(self, value):  # 方法的第一个参数为默认参数，及当前对象本身
        self.data = value

    def display(self):
        print(self.data, self.age)


demo1 = FirstClass()
demo1.setdata(5)
demo1.age = 22
demo1.display();
demo1.name = 'jiangpeng'

print(demo1.name)

demo2 = FirstClass()
print(demo2.name)


################类的继承###################
class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def setName(self, name):
        self.name = name

    def setAge(self, sex, add):  # 该方法会被下面的同名方法覆盖而不生效,不会长生重写效果,重写体现在参数形式
        self.sex = sex + add

    def setAge(self, *age):
        self.age = sum(age)

    def setSex(self, sex):
        self.sex = sex

    def toString(self):
        return '姓名:' + self.name + ' 年龄:' + self.age + ' 性别:' + self.sex


class Student(People):
    def __init__(self, name, age, sex, score):
        People.__init__(self, name, age, sex)
        self.score = score

    def setScore(self, score):
        self.score = score

    def toString(self):
        return '姓名:' + self.name + ' 年龄:' + str(self.age) + ' 性别:' + self.sex + ' 分数:' + self.score


xiaoming = People('小明', '20', '男')
print(xiaoming.toString())
zhangsan = Student('张三', '22', '男', '100')
# zhangsan.setScore('98')
zhangsan.setSex('女')
zhangsan.setAge(20, 1)
print(zhangsan.toString())


###################类运算符的重载##################
class SecondClass:
    count = 0

    def __init__(self, value):
        self.data = value
        # self.count = 100
        SecondClass.count += 1

    def __add__(self, other):
        return SecondClass(self.data + other)

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return attrs

    def __str__(self):
        return '[%s:%s]' % (self.__class__.__name__, self.gatherAttrs())

    def mul(self, other):
        self.data *= other

    def __getattr__(self, attr):
        return getattr(self, attr)


a = SecondClass('101')
print(a)
b = a + 'xyz'
print(b)
a.mul(4)
print(a)
c = SecondClass('111')
print(SecondClass.count, a.count, c.count)  # 此时啊a,c实体引用的为类的count,为同一值，相当于类的静态变量
SecondClass.count += 1  # 改变的是类的count
a.count += 1  # 为实体a添加count属性改变的是
print(SecondClass.count, a.count, c.count)  # 此时a实体拥有了自己的count属性,c实体引用的仍是类的count
print(a.__getattr__('data'))


###################最简但的Python类#################
class rec: pass


rec.name = 'Bob'
rec.age = 40
a = rec()
a.name = 'Tom'
b = rec()
print(rec.name, a.name, b.name, b.age)
rec.name = 'Jane'
print(rec.name, a.name, b.name, b.age)


# 总结为：对于某一属性,首先搜索实体自身，若没有则搜索类定义及其顶层超类

############类的通用工具&类的终极形式#######################
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return attrs

    def __str__(self):
        return '[%s:%s]' % (self.__class__.__name__, self.gatherAttrs())


class Person(AttrDisplay):
    '''Create and process person records'''

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):
    '''
     A customized Person with special requirements    
    '''

    def __init__(self, name, pay):
        Person.__init__(self, name, '管理员', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(0.2)
    print(tom.lastName())
    print(tom)

################Python对象持久化Pickle\Shelve\dbm################
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)
# 将类数据存储到文件中
import shelve

db = shelve.open('classdb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close
# 从文件中读取类数据
db = shelve.open('classdb')
newbob = db['Bob Smith']  # 获取实例
print(newbob)
print(newbob.lastName())

for key in sorted(db):
    print(key, '--->', db[key])
sue = db['Sue Jones']
sue.giveRaise(.10)
db['Sue Jones'] = sue
db.close()


###############命名空间链接#################
def classtree(cls, indent):
    print('.' * indent + cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)


def instancetree(inst):
    print('Tree of % s' % inst)
    classtree(inst.__class__, 3)


def selftest():
    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B, C): pass

    class E: pass

    class F(D, E): pass

    instancetree(B())
    instancetree(F())


if __name__ == '__main__':
    selftest()
