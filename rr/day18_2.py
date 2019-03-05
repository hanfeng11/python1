n=int(input("请输入第几项:"))
a=0
b=1
count=2
if n==0:
    print("请输入一个正整数！")
elif n==1:
    print("斐波那契数列为:")
    print(a)
else:
    print("斐波那契数列为:")
    print(a,",",b,end=" , ")
    while count<n:
        c=a+b
        print(c,end=" , ")
        a=b
        b=c
        count+=1
