#!/usr/bin/env python
# -*-coding: utf-8 -*-

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]
print L[-2:]
print L[-2:-1]

L = range(100)
print L

#可以通过切片轻松取出某一段数列。比如前10个数：

print L[:10]

#后10个数：
print L[-10:]

#前11-20个数：
print L[10:20]

#前10个数，每两个取一个：
print L[:10:2]

#所有数，每5个取一个：
print L[::5]

#甚至什么都不写，只写[:]就可以原样复制一个list：
print L[:]

#tuple也可以使用切片

#迭代
#给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们成为迭代（Iteration）
#在Python中，迭代是通过for ... in来完成的

print u'迭代dict'
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print key
for ch in d.itervalues():
	print ch

for k, v in d.iteritems():
	print k
	print v

print u'字符串也可以迭代'
for ch in 'ABC':
	print ch
print u'判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断'

#print isinstance('abc',Iterable)
#print isinstance([1,2,3],Iterable)
#print isinstance(123,Iterable)

for i, value in enumerate(['A', 'B', 'C']):
	print i, value

#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式
print range(1,11)
print [x * x for x in range(1,11)]
print [x * x for x in range(1,11) if x % 2 ==0]
# 生成全排列
print [m + n for m in 'ABC' for n in'XYZ']
#dict的iteritems()可以同时迭代key和value
d = {'x':'A','y':'B','z':'C'}
for k,v in d.iteritems():
	print k,'=',v
#也可以用列表生成式
print [k + '=' + v for k,v in d.iteritems()]
print [s.lower() for s in d]

#Python中，这种一边循环一边计算的机制，称为生成器（Generator）
g = (x*x for x in range(10))
i = 0
while i < 10:
	i = i + 1
	print g.next()

def fab(max):
	n,a,b = 0,0,1
	while n < max:
		print b
		a,b = b,a+b
		n = n + 1
fab(10)

def fab2(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n + 1
#generator的另一种方法，yield
#yield作用每次调用函数是，遇到yield返回，再次执行时从上次返回的yield语句处继续执行
def odd():
	print 'step 1'
	yield
	print 'step 2'
	yield
	print 'step 3'
	yield

o = odd()
o.next()
o.next()
o.next()