from abc import ABCMeta,abstractclassmethod
#3.0抽象类
class Super(metaclass = ABCMeta):
    @abstractclassmethod
    def method(self,*a):
        pass
#2.6抽象类
class Super:
    __metaclass__ = ABCMeta
    @abstractclassmethod
    def method(self,*a):
        pass
    
################例子#########################
class Super(metaclass = ABCMeta):
    def delegate(self):
        self.action()
    @abstractclassmethod
    def action(self):
        pass

#x = Super() #抽象类不能实例化
class Sub(Super):
    def action(self):
        print('spam')
x = Sub()
x.delegate()

