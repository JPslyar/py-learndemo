import socket

print('创建socket.....')
s = socket.socket(socket.AF_INET,socket.SHUT_RDWR)
print('Socket已创建')
print('尝试连接服务器')
s.connect(('www.baidu.com',80))
print('链接',s.getsockname())