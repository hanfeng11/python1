import random
a=[]
for i in range(20):
    num=random.randint(1,11)
    a.append(num)
    a[::2]=sorted(a[::2],reverse=True)
print(a)