#一种思想：包可视为模板，__init__.py及目录下的.py文件为其属性

import os
import sys

print(os.sys.path)
sys.path.append('../../../../')#将更目录添加到主目录列表中
print(os.sys.path)

#导入父目录模块,from\import皆为赋值语句,并且都只会加载一次
from src.pg.pga import *
print(x)
x += 600 #该x为本地的x 与导入文件中的无关
from src.pg.pga import *
print(x)

import src.pg.pga
print(src.pg.pga.x)
src.pg.pga.x = 600#若想改变被导入文件中的变量名，必须使用import
import src.pg.pga
print(src.pg.pga.x)


from MD import *
print(x)
#print(z)

from src import pg

print(pg.x)
print(src.pg.pg1.x)
print(src.pg.pg1.pg2.x)
print(src.pg.pg1.pg2.pg3.x)

#查看模块命名空间
print(dir(src.pg.pg1.pg2.pg3))
print(src.pg.pg1.pg2.pg3.__dict__)

#reload之前必须先导入模块对象
import MD as MD#取别名
from imp import reload
z = reload(MD)
print(z.x)

#将包导入，将其当做一个对象使用
from src.pg import *
print(x)
print(MD.x)
print(MD.__name__)

#"."表示当前包
#from . import ND #导入当前包下的ND
#print(ND.x)
#from .ND import x #导入当前包下ND模板的x变量
#print(x)
#from .. import pg2
#print(pg2.MD.x)
#from ..pg2 import MD
#print(MD.x)

#获取木块中属性值
import MD,sys
print(MD.x)
print(MD.__dict__['x'])
print(sys.modules['MD'].x)
print(getattr(MD, 'x'))#getattr()是内置函数

#动态导入模板
modname = 'MD'
exec("import " + modname)
print(x)

M = __import__(modname)
print(M.x)