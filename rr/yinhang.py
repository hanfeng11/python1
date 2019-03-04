card1="1001"
pwd1="123456"
ban1=10000
card2="1002"
pwd2="123456"
ban2=10000
card3="1003"
pwd3="123456"
ban3=10000
print("欢迎来到python银行!")
count=0
while True:
    ban=0
    card=input("请输入用户名:")
    pwd=input("请输入密码:")
    if card==card1 and pwd==pwd1:
        ban=ban1
    elif card==card2 and pwd==pwd2:
        ban = ban2
    elif card==card3 and pwd==pwd3:
        ban = ban3
    else:
        count+=1
        if count>=3:
            print("输入次数超过三次，账户已被冻结，请去柜台服务！")
            break
        else:
            print("输入的用户名或密码有误,请重新输入!")
            continue



    while True:
        num=input("请输入你要办理的业务:1.存款 2.取款 3.退卡:")
        if num=="1":
            inn=float(input("请输入您要存款金额:"))
            if inn<=0:
                print("存款失败,请输入正确的存款金额!")
            else:
                ban = ban + inn
                print("存款成功!存款:", inn, "卡内余额为:", ban)
        elif num=="2":
            out=float(input("请输入您要取款的金额:"))
            if out>ban:
                print("卡内余额不足!")
            else:
                ban=ban-out
                print("取款成功!取款:",out,"卡内余额为:",ban)
        elif num=="3":
            print("退卡成功，欢迎下次再来!")
            break




