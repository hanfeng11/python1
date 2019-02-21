# .有四个数字1，2，3，4，能组成多少个互不相同的三位数
for i in range(1,5):
    for j in range(1,5):
        for m in range(1,5):
           if(i!=j) and (i!=m) and (j!=m):
                print(i,j,m)