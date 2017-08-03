######################递归函数###########################
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
print(mysum([2,4,1,6,4]))
      
def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])
print(mysum([2,4,1,6,4]))

def mysum(L):
    if not L:
        return 0
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])
print(mysum([2,4,1,6,4]))

def mysum(L):
    if not L:
        return 0
    first,*rest = L
    return first if not rest else first + mysum(rest)
print(mysum([2,4,1,6,4]))

###################处理复杂结构####################
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
print(sumtree([1,[2,[3,4],5],6,[7,8]]))


#################函数属性####################
def  func():
    print(func.art)
func.art = '我靠'
func()

################函数注解####################
def func(a:'spam',b:(1,10),c:float=5) ->int:
    return a + b + c
print(func(2,3))
print(func.__annotations__)

##############序列映射函数map##################
#map函数的定义：
#map(function, sequence[, sequence, ...]) -> list
#通过定义可以看到，这个函数的第一个参数是一个函数，剩下的参数是一个或多个序列，返回值是一个集合。
#function可以理解为是一个一对一或多对一函数，map的作用是以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的list。
L = [2,3,4,5,6]
K = [8,9,10,11,12]
def inc(x): return x ** 2
LL = list(map(inc,L))
print(LL)

print(list(map(lambda x:x + 3,L)))
print(list(map(lambda x,y:x + y,L,K)))

############函数编程工具filter和reduce######
#filter函数的定义：
#filter(function or None, sequence) -> list, tuple, or string
#function是一个谓词函数，接受一个参数，返回布尔值True或False。
#filter函数会对序列参数sequence中的每个元素调用function函数，最后返回的结果包含调用结果为True的元素。
L = list(filter(lambda x:x>0,range(-5,5)))
print(L)

#reduce函数的定义：
#reduce(function, sequence[, initial]) -> value
#function参数是一个有两个参数的函数，reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function。
#第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function，否则会以序列sequence中的前两个元素做参数调用function。
from functools import reduce
K = reduce(lambda x,y:x+y,range(-5,5),5)
print(K)