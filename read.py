def read():
    f=open('config.txt','r')
    fp=f.readlines()
    f.close()
    users=[]
    pwds=[]
    for data in fp:
        m,n=date.split(',')
        k=m.strip('\t\r\n')
        n=n.strip("\t\r\n")
        users.append(k)
    return user,pwds

