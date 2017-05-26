#coding=utf-8


#有序可变的list 可以保持过程中的中间结果，动态的保存了函数体动态执行结果
l = list
lss = list((1,2))
lw = []
l1 = [1]
l2 = [1,2,3,4,1]
print  dir(list)

# 位置
print   l2.count(3)
print   l2.index(3)
l2.extend('1')
print l2
# 在最后位置增加
l2.append(2)
print l2
# 在某个位置插入一个数
l2.insert(1,10)
print  l2
#弹出在某个位置的数

l2.pop(1)
print l2
#删除某个数
l2.remove(4)
print l2

l2.reverse()
print l2
#排序
l2.sort()
print l2


