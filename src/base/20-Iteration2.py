L = list(map(ord,'spam'))
print(L)

L = list(map(lambda x:x**2,range(10)))
print(L)

L = [x for x in range(5) if x % 2 == 0]
print(L)

L = list(filter(lambda x:x%2==0,range(5)))
print(L)

L = list(map(lambda x:x**2,filter(lambda x:x%2==0,range(10))))
print(L)

L = [x+y for x in [1,2,3] for y in [100,200,300]]
print(L)

L = [(x,y) for x in range(5) if x%2==0 for y in range(5) if y%2==1]
print(L)

M = [[1,2,3],[4,5,6],[7,8,9]]
N = [[2,2,2],[3,3,3],[4,4,4]]
L = [r[1] for r in M]
print(L)
K = [M[r][c]*N[r][c] for r in range(3) for c in range(3)]
print(K)
K = [[M[r][c]*N[r][c] for c in range(3)] for r in range(3)]
print(K)

############yield生成器函数应用#############################
def gensquares(N):
    for i in range(N):
        yield i**2
for i in gensquares(5):
    print(i)

#def gen():
    #sum = 0
    #for i in range(10):
        #x = yield i
        #sum = sum + (x if x != None else i)
        #print(sum)
#G = gen()



