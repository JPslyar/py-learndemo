l = [123,'jiangpeng',1.234];
print(len(l));
print(l[:-1]);
print(l[1:]);
print(l[:]);
print(l+['hahah',567]);
l.append('span');
print(l);
l.pop(2);
print(l);
l.remove(123);
print(l);
l.insert(1, 'aobject');
print(l);
l.sort();
print(l);
#反续排列
l.reverse();
print(l);


##############################################
M = [[1,2,3],[4,5,6],[7,8,9]];
print(M[1]);
print(M[1][2]);

col2 = [row[1] for row in M];
print(col2);

col2 = [d[1] for d in M]
print(col2);

col2 = [row[1]+1 for row in M];
print(col2);

col2 = [row[1] for row in M if row[1]%2==0];
print(col2);

diag = [M[i][i] for i in [0,1,2]];
print(diag);

doubles = [c * 2 for c in 'spam'];
print(doubles);

G = (sum(row) for row in M);
print(next(G));
print(next(G));

print(list(map(sum,M)));

print({sum(row) for row in  M});

z = {i:sum(M[i]) for i in range(3)}
print(z[1])

z = [ord(x) for x in 'spaam'] 
print(z)


