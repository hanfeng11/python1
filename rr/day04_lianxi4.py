# .实现100-200里面所有的质数字,打印这些质数并且求出个数
# a=[]
# for i in range(100,201):
a=[]
# for i in range(100,201):
#     b=0
#     for x in range(2,i-1):
#         if i%x==0:
#             b+=1
#     if b==0:
#         a.append(i)
# print(a)
# print(len(a))
a=[]
for i in range(100,201):
    b=0
    for j in range(2,i-1):
        if i%j==0:
            b+=1
    if b==0:
        a.append(i)
print(a)
print("长度为:",len(a))