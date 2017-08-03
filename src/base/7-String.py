print("ssss'sss")
print('s\np\ta\x00m')
print('''...''')
print(r'\temp\spam')#raw字符串-抑制转义
print(b'spam')
print(u'spam')

print("a%sparrot"%'kind')
print("a{0}{1}parrot".format('kind','ww'))
s = 'jiangpengp,ahahadddssdsd'
print(s.find('pa'))
print(s.rstrip())
print(s.replace('pa', 'XX'))
print(s.split(','))
print(s.isdigit())#内容测试 判断是不是字符
print(s.lower())
print(s.endswith('dsd'))
print('  '.join(['sssss','wqw','ewwr']))

mantra = """Always look
on the bright
side of life."""
print(mantra)

#字符串切片
s = 'qwertyuiopasdfghjklzxcvbnm'
print(s[1:25:2])#间隔取数
print(s[::-1])#字符串反置
print(s[slice(1,25,2)])
print(s[slice(None,None,-1)])

#字符串转换工具
print(str('jiangpeng'),repr('jiangpeng'),int("42"))

#字符ASCII转换工具
print(ord('s'),chr(115))

#字符串格式化
print("%(n)d %(x)s" % {"n":1,"x":"spam"})

reply ="""
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
values = {'name':'Bob','age':40}
print(reply % values)

food = 'spam'
age = 40
print("%(age)d %(food)s" % vars())#vars()该函数将前面所有出现过的函数转换为字典

print("%s hahaha %s" % ('1','2'))

print('%-10s = %10s' % ('spam',123.456))
print('%10s = %-10s' % ('spam',123.456))


template = '{0},{1} and {2}'
print(template.format('spam','ham','eggs'))

template = '{motto},{pork} and {food}'
print(template.format(motto='spam',pork='ham',food='eggs'))

template = '{motto},{0} and {food}'
print(template.format('ham',motto='spam',food='eggs'))

#在字符串转换时添加键、属性和偏移量
import sys
s = 'My {1[spam]} runs {0.platform}'.format(sys,{'spam':'laptop'})
print(s)
s = 'My {config[spam]} runs {sys.platform}'.format(sys=sys,config={'spam':'laptop'})
print(s)

s = '{0:10} = {1:10}'.format('spam',123.456)
print(s)
s = '{0:>10} = {1:<10}'.format('spam',123.456)
print(s)
s = '{0.platform:>10} = {dict[item]:<10}'.format(sys,dict={'item':'laptop'})
print(s)