#coding=utf-8
#什么叫生成器
#一边循环一边计算的机制，成为生成器   一个可以生成可迭代对象的函数或表达式 包含__iter__方法的

print  range(10)
print  xrange(10) #返回xrange可迭代对象,iter()  rangeiterator
