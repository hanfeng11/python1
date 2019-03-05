for i in range(2,1001):
    k=[] #用于收集一个数的所有因子
    n=-1
    s=i
    for j in range(1,i):
        if i%j==0:
            n+=1
            s-=j
            k.append(j)#收集所有因子
    if s==0:
        print(i,":") #打印完数
        for j in range(n):#遍历完数的所有因子
            print(str(k[j]),end="+") #打印所有因子
        print(k[n])#打印
