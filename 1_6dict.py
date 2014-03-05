#!/usr/bin/env python
# -*-coding: utf-8 -*-

#dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'Jack': 95, 'Michael': 75, 'Tracy': 85}
print d
print d['Jack']

print'-----------'
#key不存在，会报错可以通过in判断
print 'Li' in d
if 'Li' in d:
	print d['Li']
else:
	print u'不存在'
print'-----------'
#通过get方法，如果不存在返回None或者指定的Value
print d.get('Li')
print d.get('Li',-1)
print'-----------'
#删除元素
d.pop('Jack')
print d