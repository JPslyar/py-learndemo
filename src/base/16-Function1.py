#####################函数定义及调用##################
def times(x,y):
    return x*y
print(times('你好', 2))

def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
print(intersect('abcf', 'fdce'))
print(intersect([1,2,3,4], (2,3,6,7)))#多态性



