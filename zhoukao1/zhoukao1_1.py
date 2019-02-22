var1=input("请输入电话号码:")
str=[153,185,176,188]
try:
    int(var1)
    if (len(var1)==11):
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
        print("不是有效的电话号码！")
except :
    print("请输入正确的电话号码")



