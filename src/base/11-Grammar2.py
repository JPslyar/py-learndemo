spam = 'Spam'
spam,ham = 'yum','YUM'
[spam,ham] = ['yum','YUM']
a,b,c,d = 'spam'
a,*b = 'spam'#b匹配剩下的内容['p','a','m']
spam = ham = 'lunch'
spam += '42'

nudge = 1
wink = 2
A,B = nudge,wink
[C,D] = [nudge,wink]
[a,b,c] = (1,2,3)

string = 'SPAM'
a,b,c,d = string
a,b,c = string[0],string[1],string[2]
a,b,c = list(string[:2])+[string[2:]]
(a,b),c = string[:2],string[2:]
((a,b),c) = ('SP','AM')


for(a,b,c) in [(1,2,3),(4,5,6)]:
    print(a,b,c)
for((a,b),c) in [((1,2),3),((4,5),6)]:
    print(a,b,c)

def f(a,b,c):
    print(a,b,c)
    
f(1,2,3)

red,green,blue = range(3)

L = [1,2,3,4]
while L:
    front,L = L[0],L[1:]
    print(front,L)
    
seq = [1,2,3,4]
a,b,c,d = seq
a,*b = seq
a,*b,c = seq#b为[2,3],*表示匹配剩下的所有内容，所以只能有一个

import sys
print(3,4,5,sep = '***',end = '')
print(3,4,5,sep = '***',end = '\n')
print(3,4,5,sep = '***',end = '',file = sys.stdout)
temp = sys.stdout
sys.stdout = open('myfile.txt','a')
print("你好啊！！！！！！！！！",file = sys.stdout)
sys.stdout = temp
print('hello world')