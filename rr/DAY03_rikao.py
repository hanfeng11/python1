# var1=int(input("请输入第一个人的生日:"))
# var2=int(input("请输入第二个人的生日:"))
# if var1<var2:
#     print("第一个人的年龄大")
# else:
#     print("第二个人的年龄大")

import random
var3=""
for i in range(1,10):
    var3=int(random.randrange(1,i+1))
    print("随机生成的数列为:",var3)

var4=int(random.randrange(1,10))
print("生成的整数为:",var4)

for i in var3:
    if var4 == var3[i]:
        print("在数列中")
    else:
        print("不在数列中")



