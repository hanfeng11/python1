dict={}
key=0
i=1
list=[]
while 1:
    str = input("请输入你要投的职位:")
    if (str == "结束"):
        break
    list.append(str)
for i in list:
    key = dict.get(i)
    if (key==None):
        dict[i] = 1
    else:
        dict[i]+= 1
print(dict)
print("票数最多的人是:",max(dict,key=dict.get))
print("票数是:",dict[max(dict,key=dict.get)])
dict1=sorted(dict.items(),key=lambda item:item[1],reverse=True)
print("排序后的结果是:",dict1)






