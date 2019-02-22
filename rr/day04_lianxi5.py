# 随机生成数字，猜大小
try:
    import random
    b = random.randint(1, 100)
    a = int(input("请输入一个数字（1-100）:"))
    while 1:

        if a == b:
            print("恭喜你猜对了!")
            break
        elif a < b:
            print("猜小了")
            a = int(input("请输入一个数字（1-100）:"))
        elif a > b:
            print("猜大了")
            a = int(input("请输入一个数字（1-100）:"))
except:
    print("不能输入中文")

