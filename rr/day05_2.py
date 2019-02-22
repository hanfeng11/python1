list=[]
s=0
for i in range(101,201):
    bool=True
    for j in range(2,i-1):
        if(i%j==0):
            bool=False
    if(bool==True):
        list.append(i)
        s+=1
    else:
        continue
print(list)
print("素数个数为:",s)