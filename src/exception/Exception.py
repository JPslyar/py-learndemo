try:
    raise IndexError
except IndexError:
    print('got exception')

############自定义异常##################
class Bad(Exception):
    pass
def doomed():
    raise Bad
    print('doomed')
try:
    doomed()
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
    
#############断言：assert##################
def f(x):
    assert x < 0,'x must be negative'
    return x ** 2

print(f(-1))
#########用来取代try的with/as语句######
#from __future__ import with_statement
#with open(r'C:\misc\data') as myfile:#这种写法下当for循环完成或代码异常时myfile会自动关闭
    #for line in myfile:
        #print(line)
