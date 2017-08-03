import socket  
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
sock.bind(('localhost',7556))  
sock.listen(5)  
while True:  
    connection,address = sock.accept()  
    print("client ip is ",address)   
    try:  
        connection.settimeout(5)  
        buf = connection.recv(1024).decode()
        if buf == '1':  
            connection.send(b'welcome to python server!')  
        else:  
            connection.send(b'please go out!')  
    except socket.timeout:  
        print('time out')  
    connection.close()  

input('stop......')