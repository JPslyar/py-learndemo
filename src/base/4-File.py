f = open('data.txt','w')
z = f.write('hello world')
f.close()
print(z)#返回number of bytes written in


f = open('data.txt')#默认‘r’模式打开  与open('data.txt','rb')等效
text = f.read()
print(text)


