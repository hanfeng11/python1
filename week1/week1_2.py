import random
a=[]
for i in range(50):
   b=random.randint(-10,11)
   a.append(b)

print("原字符是:",a)

c=[]
d=[]
for i in a:
    if i>0:
        c.append(i)
    elif i<0:
        d.append(i)
print("正数:",c)
print("负数:",d)






