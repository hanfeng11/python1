import random
a=[]
for i in range(50):
    num=random.choice(range(-10,11))
    a.append(num)
print("a:",a)
b=[]
c=[]
for i in a:
    if i>0:
     b.append(i)
    elif i<0:
        c.append(i)
print("正数:",b)
print("负数:",c)