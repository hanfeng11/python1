import random
a=[]
for i in range(50):
    num=random.randint(-10,11)
    a.append(num)
print(a)
c=[]
d=[]
for i in a:
    if i>0:
        c.append(i)
    else:
        d.append(i)
print("正数:",c)
print("负数:",d)