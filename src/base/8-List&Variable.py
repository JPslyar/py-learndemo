L = ['eat','more','please','aBc','abc']
print(L.sort())
print(L.sort(key=str.lower,reverse=True))#key用来排序的值，reverse反排序
print(sorted(L,key=str.lower,reverse=True))
print(sorted([x.lower() for x in L],reverse = True))

L = [1,2]
L.extend([3,4,5])#在末尾追加
print(L)
L.pop(2)#无参数时删除最末尾的数，有参数时以参数为下标删除
print(L)
L.insert(2,'insert')
print(L)
L.remove(2)
print(L)
del L[0]
print(L)

######################################################################

D = {'spam':1,'ham':2,'eggs':3}
print(list(D.keys()))
print(list(D.values()))
print(list(D.items()))
print(D.get('spam'))
print(D.get('total'))
print(D.get('total',4))#给默认值
print(D)

D2 = {'toast':4,'muffin':5}
D.update(D2)
print(D)
print(D.pop('toast'))
print(D)
print(D['spam'])

D = {}
D['spam'] = 1
print(D)#这一点列表不行

#字典记录系数矩阵值
Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99
x = 2;y = 3;z = 4
print(Matrix[(x,y,z)])

#字典的创建
D = {}
D = dict(name = 'mel',age = 45)
D = dict([('name','mel'),('age',45)])
D = dict.fromkeys(['a','b'], 0)
L = list(zip(['a','b','c'],[1,2,3]))
D = dict(zip(['a','b','c'],[1,2,3]))
D = {k : v for (k,v) in zip(['a','b','c'],[1,2,3])}

del D['a']
print(D)

#字典视图和几何
K = {'x':4,'b':1}
print(D.keys()|K.keys())
print(D.keys()&K.keys())
print(D.items()|K.keys())
print(D.items()&K.keys())

#字典排序
D = dict(zip(['a','c','b'],[1,2,3]))
Ks = D.keys()
Ks = list(Ks)
Ks.sort()
for k in Ks:
    print(k,D[k])

Ks = D.keys()
for k in sorted(Ks):
    print(k,D[k])

for k in sorted(D):
    print(k,D[k])

print(D)