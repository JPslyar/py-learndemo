rec = {'name':{'first':'Bob','last':'Smith'},'job':['dev','mgr'],'age':40.5}
print(rec['name'])
print(rec['name']['last'])
print(rec['job'][-1])
rec['job'].append('jiangpeng')
print(rec)

D = {'a':1,'b':2,'c':3,'g':7,'e':5}
ks = list(D.keys())
print(ks)
ks.sort()
print(ks)
for key in ks :
    print(key,'=>',D[key])
#############上面三步可被简化####################
for key in sorted(D):
    print(key,'=>',D[key])
   
if 'z' in D.keys():
    print('z是D中的有效键值')
else:
    print('z不是D中的有效键值')
    
if not 'z' in D.keys():
    print('z不是D中的有效键值')
else:
    print('z是D中的有效键值') 
    
value = D.get('x',0)
print(value)
value = D['x'] if 'x' in D else 0
print(value)
    
x = 4
while x > 0:
    print('spam' * x)
    x -= 1

squares = []
for x in [1,2,3,4,5,6]:
    squares.append(x ** 2)
print(squares)
