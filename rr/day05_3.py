import random
list1=[]
for i in range(10):
    num=random.randint(1,10)
    list1.append(num)
print("原列表:",list1)
list2=[]
list2=list1
print("现列表:",list2)
list2=sorted(list2,reverse=True)
print("排序后的列表:",list2)
