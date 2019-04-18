import re
a=input("请输入邮箱:")
b=re.compile(r"^[A-Za-z0-9]+@\w+\.(com|cn)$")
c=b.search(a)
if c:

    print("是正确的邮箱")
    num=re.sub(r'@.*$',' ',a)
    print("用户名:",num)

else:
    print("不是正确的邮箱")
