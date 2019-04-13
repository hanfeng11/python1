# import threading
# lock=threading.Lock()
# import time
# list1=[i for i in range(1,101)]
# def fun():
#     global list1
#     while True:
#         if list1!=[]:
#             lock.acquire()
#             one=list1[0]
#             del list1[0]
#             lock.release()
#             time.sleep(0.01)
#             print(threading.current_thread().name,one,'平方为:',one*one)
# list_th=[]
# list_name=['窗口1','窗口2','窗口3','窗口4','窗口5']
# for i in list_name:
#     t=threading.Thread(target=fun,name=i)
#     list_th.append(t)
# for i in list_th:
#     i.start()
# for i in list_th:
#     i.join()

# class hero:
#     h_name=''
#     h_xue=100
#     h_gongji=10
#     def __init__(self,n):
#         self.h_name=n
#     def hurt(self,g):
#         print("%s收到%s的攻击，血量值减少%d"%(self.h_name,g.g_name,g.g_gongji))
#         self.h_xue-=g.g_gongji
#     def h_show(self):
#         print("%s的血量值剩余%d" % (self.h_name, self.h_xue))
# class grut:
#     g_name=''
#     g_xue=80
#     g_gongji=15
#     def __init__(self,g):
#         self.name=g
#     def hurt(self,h):
#         print("%s收到%s的攻击，血量值减少%d"%(self.g_name,h.h_name,h.h_gongji))
#         self.g_xue-=h.h_gongji
#     def g_show(self):
#         print("%s的血量值剩余%d" % (self.g_name, self.g_xue))
# hero1=hero('英雄1')
# hero2=hero('英雄2')
# g1=grut('g1')
# g2=grut('g2')
# g3=grut('g3')
# hero1.hurt(g1)
# hero1.hurt(g2)
# hero1.hurt(g3)
# hero1.h_show()
#
# hero2.hurt(g1)
# hero2.hurt(g2)
# hero2.h_show()
# import threading
# lock=threading.Lock()
# import time
# list1=[i for i in range(1,1001)]
#
# def fun(a):
#     bllo=True
#     for i in range(2,a):
#         if a%i==0:
#             bllo=False
#     if bllo==True:
#         print(threading.current_thread().name,a)
# list1 = [i for i in range(1, 1001)]
# def na():
#
#     while   list1!=[]:
#             lock.acquire()
#             a=list1[0]
#             del list1[0]
#             fun(a)
#             lock.release()
#             time.sleep(0.01)
# list_th=[]
# for i in range(5):
#     t=threading.Thread(target=na,name='线程---'+str(i+1))
#     list_th.append(t)
# for i in list_th:
#     i.start()
import numpy as np
matrix = []
hang = int(input("请输入矩阵的行数: "))
lie = int(input("请输入矩阵的列数: "))
for r in range(hang):
    hang = []
    for c in range(lie):
        hang.append(int(input("M1-> R: {} C: {}\n>>>".format(r+1, c+1))))
    matrix.append(hang)
print(matrix)
a1=np.matrix(matrix)
print(np.linalg.det(a1))
if abs(np.linalg.det(a1))<0.01:
    print("没有逆矩阵")
    print("因为矩阵为0")
else:
    print("有逆矩阵")
    print("逆矩阵为:")
    print(a1.I)