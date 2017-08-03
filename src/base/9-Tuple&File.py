T = (0,'Ni',1.2,3)
T = 0,'Ni',1.2,3    #这样子也是可以滴
print(T.count('Ni'))
print(T.index('Ni'))
print(T * 4)

T = ('cc','aa','dd','bb')
tmp = list(T)
print(tmp.sort())
sorted(T)

T = (1,2,3,4,5)
L = [x + 20 for x in T]
print(L)

T = (1,[2,3],4)
T[1][0] = 'spam'
print(T)#元组不可变只适用于元组本身顶层而并非其内容

###################File###############################
output = open(r'E:\data.txt','w')
input = open(r'E:\data.txt','r')
input = open(r'E:\data.txt')#r为默认值，遇上一行一致

myfile = open('myfile.txt','w')
myfile.write('hello text file\n')
myfile.write('text文件你好\n')
myfile.close()
myfile = open('myfile.txt','r')
txt = myfile.readline()
print("line 1:"+txt)
txt = myfile.readline()
print("line 2:"+txt)
txt = myfile.readline()
print("line 3:"+txt)

for line in open('myfile.txt'):
    print(line,end='')
    
myfile = open('myfile.txt','rb').read() #以二进制处理方式打开文件
print(myfile)

#在文件中存储并解析Python对象
#存储
X,Y,Z = 43,44,45
S= 'Spam'
D = {'a':1,'b':2}
L = [1,2,3]
F = open('class.txt','w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X,Y,Z))
F.write(str(L)+'$'+str(D)+'\n')
F.close()
#解析
chars = open('class.txt').read()
print(chars)
F = open('class.txt')
line = F.readline()
line.rstrip()#Python中的strip用于去除字符串的首尾字符,同理,lstrip用于去除左边的字符,rstrip用于去除右边的字符
print(line)

line = F.readline()
parts = line.split(',')
print(parts)

line = F.readline()
parts = line.split('$')
objects = [eval(P) for P in parts]
print(objects[0],objects[1])

#使用pickle存储Python的原生对象
D = {'a':1,'b':2}
F = open('dictClass.txt','wb')
import pickle
pickle.dump(D, F)
F.close

F = open('dictClass.txt','rb')
D = pickle.load(F)
print(D)

#文件中打包二进制数据的存储与解析
F = open('data.bin','wb')
import struct
data = struct.pack('>i4sh',7, 'spam'.encode('utf-8'),8)
F.write(data)
F.close()

F = open('data.bin','rb')
data = F.read()
values = struct.unpack('>i4sh', data)
print(values)

#文件上下文管理器
with open('myfile.txt') as myfile:
    for  line  in  myfile:
        print(line)
#结束后文件会自动关闭，下面代码块有同样效果
myfile = open('myfile.txt')
try:
    for line in myfile:
        print(line)
finally:
    myfile.close()
    
#应用&拷贝&深度拷贝

#比较&相等&真值
L1 = [1,('a',3)]
L2 = [1,('a',3)]
print(L1 == L2,L1 is L2)
# ==比较值是否相等，is判断是否为同一对象 
#数字非0即为真，其他对象非Null即为真