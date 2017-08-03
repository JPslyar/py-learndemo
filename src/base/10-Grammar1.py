#while True:
    #reply = input('请输入：')
    #if reply == 'stop' : 
        #break
    #elif not reply.isdigit():
        #print('Bad!'*8)
    #else:
        #print("输入数字平方：",(int(reply)**2))
#print('Bye')


#while True:
    #reply = input('请输入：')
    #if reply == 'stop' : 
        #break
    #try:
        #num = int(reply)
    #except:
        #print('Bad!'*8)
    #else:
        #print("输入数字平方：",(int(reply)**2))
#print('Bye')


while True:
    reply = input('请输入：')
    if reply == 'stop' : 
        break
    elif not reply.isdigit():
        print('Bad!'*8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:
            print("输入数字平方：",(num**2))
print('Bye')