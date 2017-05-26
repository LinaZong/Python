#coding=utf-8
#元组有序不可变  意义在于代码安全 内容确保不会在任何环节中被改变 通常是作为参数在函数调用时被使用
t = tuple()
t1 = tuple([1])

T = ()
T1 = (1,)
T2 = (1,2,3,4)

T3 =  T2
print T3
T2.count(2)
#某个数在元祖中的位置
print  T2.count(2)

#第一个数 出现在元组中的位置
print T2.index(1)
#根据下标取值
print  T2[0]
#某个数以后的值
print  T2[2:]



