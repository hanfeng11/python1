s='The column above illustrates apparently' \
  ' the polularity of people ' \
  'doing exercise in a certain year ' \
  'from 2013 to 2018.Based upon the data,' \
  'we can see that python is wonderful. ' \
  'python is wonderful. Python'
print("原字符串:",s)
s=s.replace(".","")
print("替换后的字符串:",s)
s=s.split(" ")
print("原列表:",s)
s.pop()
print("去除空字符列表:",s)
dict={}
for i in s:
  key=dict.get(i)
  if(key==None):
    dict[i]=1
  else:
    dict[i]+=1

dict1={}
sv = list(dict.values())
sv.sort()

# 去除个数相同，减少循环次数
sv =set(sv)
sv =list(sv)

# 实现单词升序
for i in sv:
    for j in dict:
        if(dict[j]==i):
            dict1[j]=i

# 输出结果
print(dict1)