import random
import threading
import time
lock=threading.Lock()
num=1000
def Acun():
    global num
    sum_A=0#截至当天A两个车间各自生产的总的货物数量
    for i in range(30):
        a=random.randint(30,50)
        lock.acquire()
        num+=a
        lock.release()
        sum_A+=a
        time.sleep(1)
        print(threading.current_thread().name,'第%d天生产的产品数额为:%d,截至第%d天生产的总的产品数目为：%d'%(i+1,a,i+1,sum_A))

def Bcun():
    global num
    sum_B=0
    for i in range(30):
        b = random.randint(45, 60)
        lock.acquire()
        num += b
        lock.release()
        sum_B+=b
        time.sleep(1)
        print(threading.current_thread().name,'第%d天生产的产品数额为:%d,截至第%d天生产的总的产品数目为：%d'%(i+1,b,i+1,sum_B))

def mai():
    global num
    sum_M=0
    for i in range(30):
        c = random.randint(80, 100)
        lock.acquire()
        num -= c
        lock.release()
        sum_M+=c
        time.sleep(1.1)
        print(threading.current_thread().name,'第%d天销售的产品数额为:%d,截至第%d天销售的总的产品数目为：%d'%(i+1,c,i+1,sum_M))
list_th=[]
tA=threading.Thread(target=Acun,name='生产车间A')
tB=threading.Thread(target=Bcun,name='生产车间B')
tM=threading.Thread(target=mai,name='销售部')
list_th.append(tA)
list_th.append(tB)
list_th.append(tM)
for i in list_th:
    i.start()
for i in list_th:
    i.join()
print("30天猴剩余:",num)






# def Acun():
#     for i in range(1):
#         a = random.randint(30, 51)
#         print("A车间生产%d件货物", a)
#         print("A车间的总得货物数量%d", num + a)
#
#
# def Bcun():
#     for i in range(1):
#         b = random.randint(45, 61)
#         print("B车间生产%d件货物", b)
#         print("B车间的总得货物数量%d", num + b)
#
#
# def mai():
#     for i in range(1):
#         c = random.randint(80, 101)
#         print("销售部%d件货物", c)
#
#
# list_th = []
# for i in range()