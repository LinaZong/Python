#coding=utf-8
d = dict(a = 2,b = 4,c = 10)
t = {
    'a':1,
    'b':2,
    'c': (1,2),
     'd': [None, True]
}

#返回字典一个浅拷贝
d.copy()
print d
#用于创建一个新的字典   seq 字典键值    value 可选参数 设置值
print  d.fromkeys(d,'10')
#获取某个key的Value
print  d.get('a')
#判断是否有某个值  返回值 ture  False
print d.has_key('d')
#所以的键值对 返回的是列表对象
print d.items()
for (k,v) in d.items():
    print k,v


#迭代输出字典的键值对 返回的是iterator对象
print ('~~~~')
for k,v in d.iteritems():
    print k,v
print ('####')

#返回iteraKey对象
print d.iterkeys()
for k in d.iterkeys():
    print k

#返回所有值对象
for v in d.itervalues():
    print v

print ('所以keys')
for kw in d.keys():
    print kw

#弹出某个值移除 并返回移除值
print '弹出某个key值对应的value'
print d.pop('a')

print '随机返回并删除字典中的一对键和值（项）'
print t.popitem()
print t

print '添加键值对'
print d
d.setdefault('r',[1])
print d
d['f'] = 10
print d

print '函数把字典dict2的键/值对更新到dict里  添加到指定字典dict里的字典。'
d.update(t)
print d
print '获取字典中所以的value'
print d.values()
print '---返回一个view对象，key的列表'
for  key in  d.viewitems():
    print  key
for  key in  d.viewvalues():
    print  key