import random
a=[]
for i in range(20):
    num=random.choice(range(10))
    a.append(num)
print("排序前:",a)
a[::2]=sorted(a[::2],reverse=True)
print("排序后:",a)
