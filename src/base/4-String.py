import re
s = "jiangp, p eng "
print(len(s))
print(s[1])
print(s[3:6])
print(s[3:-2])
print(s[3:])
print(s[:-2])
print(s.find('gp'))
print(s.replace("gp", "bb"))
print(s.split(","))   
print(s.upper())
#去除空格
print(s.rstrip())
#判断是否为字母
print(s.isalpha())
#占位填充
d = "{0} world,{1} are {2}".format("hello","how","you")
e = "%s world,%s are %s"%("hello","how","you")
print(d)
print(e)
#取字符的ASCIIֵ
print(ord('a'))

###################################################


match = re.match('Hello[ \t]*(.*)world', 'Hello    Python world')
print(match.group(1))
print(match.groups())
