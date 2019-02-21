# 二 输入一个数求1！+2！+3！+4！+n！=？
sum=0
factorial=1
var1=int(input("请输入一个数:"))
for i in range(1,var1+1):
    factorial=factorial*i
    sum+=factorial
print("阶乘之和为:",sum)