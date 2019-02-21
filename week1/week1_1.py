var1=input("请输入电话号码:")
str=[185,175,159,188,176]
try:
    int(var1)
    if(len(var1)==11):
        head=var1[0:3]
        bool=False
        for i in str:
            if(int(head)==(i)):
                bool=True
                break
        if(bool):
            print("有效电话号")
        else:
            print("无效电话号")
    else:
        print("输入的电话号长度不够")
except:
    print("请勿输入字母")




