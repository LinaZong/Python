#coding=utf-8
import copy

print '集合'

s = set([3,5,9,10])
t = set([1,3,4,10,4,5,35,6,7])
a = t|s #t和s的并集
print  a

b = t &s   # t 和 s的交集
print b

c = t - s  # 求差集(项在t中,但不在s中)
print c
d = s- t
print d
f = t ^s #对称差集 （项目在t或者s中，但不会同时出现在2者之间）


print '浅复制和深复制'
print '浅复制：只复制父对象，不会拷贝对象的内部的子对象'
print '深拷贝：拷贝对象以及其子对象'
print '拷贝应用'
a = [1,2,3,4,['a','b']]
b = a
print b
c = copy.copy(a) #对象拷贝,浅拷贝
print c
d = copy.deepcopy(a) #对象拷贝,深拷贝
print d
a.append(5)
a[4].append('c')
print 'a=', a
print 'b=',b
print'c=', c
print 'd=',d
