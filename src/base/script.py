import aa
import math
print(aa.a)
input('change file aa.py now......')
#from imp import reload
#reload(aa)
exec(open('aa.py').read())
print(aa.a)
input('observe the result......')

from aa import a,b,c
print(a,b,c)
d = "{0} world,{1} are {2}".format("hello","how","you")
e = "%s world,%s are %s"%("hello","how","you")
print(d)
print(e)
print(dir(aa))
input(math.pi)




