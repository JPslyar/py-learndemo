T = (1,2,3,4,5)
print(len(T))

T = T + (5,6)
print(T)

print(T.index(4))#元素下标
print(T.count(4))#元素出现次数

T = ('spam',3.0,[1,2,3])
print(T[1])
print(T[2][1])
print(T[2])
T[2].append(4)
print(T[2])