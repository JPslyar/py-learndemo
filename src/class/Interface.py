class Super:
    def  method(self):
        print('in Super.method')
    def delegate(self):#定义期待在子类中实现的方法
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):#取代父类方法
    def method(self):
        print('in Replacer.method')

class Extender(Super):#扩展父类方法
    def method(self):
        Super.method(self)

class Provider(Super):#实现父类接口
    def action(self):
        print('in Provider.action')
        
if __name__ == '__main__':
    for klass in (Inheritor,Replacer,Extender):
        print('\n'+klass.__name__+'...')
        klass().method()
        print('\nProvider')
        x = Provider()
        x.delegate()