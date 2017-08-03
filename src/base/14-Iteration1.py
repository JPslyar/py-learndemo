################文件迭代解析############################
f = open('myfile.txt')
flag = False
while not flag:
    try:
        s = f.__next__()#文件自身迭代器
        print(s,end='\n')
    except:
        flag = True
else:
    f.close()
    print('The flag is True')
###############next(I)&I=iter()&I.__next__()########################    
f = open('myfile.txt')
flag = False
while not flag:
    try:
        s = next(f)
        print(s,end='\n')
    except:
        flag = True
else:
    f.close()
    print('The flag is True')
#######################################  
L = [1,2,3,4,5,6]
I = iter(L)
flag = False
while not flag:
    try:
        s = I.__next__()# I.__next__()等效于next(I)
        print(s)
    except:
        flag = True
else:
    print('The flag is True')


f = open('myfile.txt')
flag = False
I = iter(f)
while not flag:
    try:
        s = I.__next__()#因为文件对象本身含有__next__()函数，所以iter(f)即为文件对象本身
        print(s,end='\n')
    except:
            flag = True
else:
    f.close()
    print('The flag is True')
        
##############迭代字典###############
D = {'a':1,'b':2,'c':3}
for key in D.keys():
    print(key,D[key])
for key in D:
    print(key,D[key])  
    
###############列表解析#################
L = [1,2,3,4,5]
for i in range(len(L)):
    L[i] += 10;
print(L)
L = [x-5 for x in L]
print(L)

f = open('myfile.txt')
lines = f.readlines()
lines = [line.rstrip() for line in lines]
print(lines)

lines = [line.rstrip() for line in open('myfile.txt') if line[0] == 't']
print(lines)

#################简单的双for循环################
L = [x+y for x in '123' for y in '456']
print(L)
print(any(L))#存在在不为空的对象
print(all(L))#所有对象都不为空

#range()可同时支持多个迭代器，之间互不影响，zip,map,filter使用多个迭代器时会使用同一迭代位置
M = map(abs,(-1,2,3))
print(M)