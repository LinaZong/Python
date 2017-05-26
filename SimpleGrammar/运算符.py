#coding=utf-8
a = 3
b = 2
print  a + b
print 1* 2
print 1 / 3 #默认是整除

print 3 /2.0#非整除的话 需要除于浮点型
print 1% 2 #取余
print 8 // 3.0 #地板除 整除的结果 但是如果有浮点型 显示的类型为浮点型形式
print  8// 3
print  3 **2 #乘方

#赋值运算符
print '赋值运算符'
a = 1
b = 3
a +=1 #自增
print a

print  True and False
print  True or False\

print '位移运算符'
print 8<< 1
print 8 & 4
print 8 | 4
print  8 ^ 4
print ~ 90

print '成员运算符'
print 1 in [1,2,3,4,5]
print  3 not in [23,3]
print  1 is 1 #比较是不是同一个成员的 地址
print 1 is not 3

print '三元运算符'
b = 10; c = 11;
a = b if b>c else c
print a
print b>c and b or c
a = (b> c and [b] or  [c])[0]
print a

print '列表解析表达式'
print '列表解析式相比于for循环更加高效'
print [i for i in range(10)]# 只有一个iter参数的map函数
print [i * 2 for  i in range(10) if i %2 == 0] #filter函数
print [(i * 2, j ) for  i in range(10) if i / 2== 0 for j in range(10) if j / 2 == 0]


print '生成器表达式'

a =  (i for i in range(10))

for i in a:
    print i

print '~~~~~~'
b = (i for  i  in range(10) if i % 2 == 0)
for i in b:
    print  i

print '~~~~~~'
c = ((i,j) for i  in range(10) for  j in range(10))

for i ,j  in c:
    print  i ,j


print 'lambda'

f = lambda  *x: 'more args' if len(x) > 1 else 'one arg'
print f(1,2,3,4,5,6)

d = lambda  *x: [i for i  in x if i %2 == 0]
print d(1,4,6,8,9,7,6,5,10)

def map2(f,seq, *seqs):

    l = []
    new_seqs = [seq]
    new_seqs.extend(seqs)
    args_list = zip(* new_seqs)
    for i in args_list:

        f(*i)
        l.append(f(*i))
    return l

l =[1,2,3,4]
ll= [5,6,7,8]
lll = [7,8,9,10]
f = lambda x:x*2

print '~~~~~~~~'
print  map(f,l)
print map2(f,l)
