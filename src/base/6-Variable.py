L1 = [2,3,4]
L2 = L1[:] #分片会产生列表的复制，但不会应用到字典与集合上，因为他们不是序列
L1[0] = 24
print(L1)
print(L2)
#复制对象一般会使用copy
import copy
X = {'a':'a','b':'b'}
Y = copy.copy(X)
print(Y)
Y = copy.deepcopy(X)
print(Y)

L = [1,2,3]
M = L 
print(L == M)#判断值是否相等
print(L is M)#判断是否为同一对象
X = 42
Y = 42
print(X == Y)
print(X is Y)#常量被缓存，X与Y引用同一个常量对象
import sys
print(sys.getrefcount(42))#查看对象引用的次数