#-*- coding: UTF-8 -*-
import os
import sys
import  re
print "hello  Woerld"


l = [1, True, 'a', None]
print type(l)
l.append(3.14)
print l
del l[2]#增加

################字典########
d = {1:1, 'a':'a', 'k': [0,1,2]}
print type(d), d
print d[1]
d['k2'] = 'hello'
print d
del d['a']
print d
d[1] = 10
print d

#帮助   Python帮助方式
# dir()## //打印对象的所有属性和方法
# help(obj.method1) ##会打印出method1方法的调用参数、功能说明等等 忘记了python有哪些内建凼数了,怎么办?
# dir(__builtins__) ##直接查诟python自带的内建凼数、常量、对象
# help(‘modules’) ##查看python的内建模块

########字符串操作########
a = 'hello' + ' Bob'
print a
s = '1234567890'
print s[3:], s[:5], s[3:7], s[-1]
b = 'my name is %s, and age is %i' % ('John', 25)
print b
c = 'value of name is %(name)s' % {'name':'macy'}
print c
d = 'hello ' * 5
print d


########函数参数传递##############

###位置传递  默认值参数在定义时,必须在位置参数的后面 一个*代表数组 两个** 代表字典
def foofex(arg1,arg2,arg3 = 22):
    print arg1,arg2, arg3

foofex(1,2,3)

def  fooA(a1=1,a2=2,a3=3):
    print a1,a2,a3
fooA()
foofex(2,4,6)
#########动态参数####
def fooB(*args):
    print type(args)
    for i in args:
       print i

fooB(1)
fooB(1,'6',True,None)

def fooC(**args):
    print type(args)
    for k,v in args.items():
        print k,v
fooC(k1 = 1)
fooC(k1=1, k2='a', k3=True, k4=None)


def fooD(*arg1, **arg2):
	for i in arg1:
		print i
	for k,v in arg2.items():
		print k,v

print '##################'
fooD(1)
fooD(k1=1)
fooD(100, 200, k3=True, k4=None)

print '##################'
def fooE(a, k=100, *arg1, **arg2):
	print a, k, arg1, arg2
fooE(1)

#########内建函数###############
#######用户输入################
# s = raw_input('请输入一个任意内容')
# print s
# w = input('Please input something:')
# print w

###################文件操作#######
f = open('1.txt','a')
dir(f)
f.write('sdfsdfsdf\r\nfsdfsdf')
f.close()


f1 = open('1.txt', 'r')  ##rb
dir(f)
for l in f1:
	print l
f1.close()

f2 = open('1.txt', 'w')  ##rw
dir(f)
f2.write('sdfsdfsdf\r\nfsdfsdf\r\n2342423423')
f2.close()

f3 = open('1.txt', 'r')  ##rb
dir(f3)
for l in f3:
	print l
f3.close()
# #########map########## 主要用来对多个序列迚行映射处理幵返回一个处理后的对应序列##
s1=[2,3,5,3,7,9,4]
s2=[5,3,5,4,7,6,8]
s3=[9,6,5,3,2,1,5]
s = map(lambda x,y,z:x+y+z,s1,s2,s3)
print s

#########reduce主要用来单个序列迚行逐一叠加处理############
s4=[1,2,3,4,5,6,7,8,9,10]
newS =reduce(lambda  x,y:x+y,s4)
print newS

#########filter   过滤函数############
s5=[1,2,3,4,5,6,7,8,9,10]
sF = filter(lambda x:x%2==0, s5)
print sF

#################OS 操作函数 用来操作不同系统的接口交互的模块
# dir(os)
# os.mkdir('d:\pytest')
# ls = os.listdir('d:\pytest')
# print ls


#########sys  环境模块############

# print dir(sys)
# print sys.getdefaultencoding()
# print sys.path

########re 正在表达式#######

text = "JGood is a handsome boy, he is cool, clever, and so on... "
m = re.match(r"(\w+)\s", text)
if m:
	print m.group(0), '\n', m.group(1)
else:
	print 'not match'


##########元祖##########
t = tuple()
T = tuple([1])

print  t(1)
