#!/usr/bin/env python
# -*-coding: utf-8 -*-


#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回

print '-----map-----'
def f(x):
   return x * x

print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
print '-----reduce-----'
def add(x,y):
	return x +y

print reduce(add,[1,3,5,7,9])

print u'------字符串转换------'
def fn(x,y):
	return x * 10 + y

print reduce(fn, map(int, '12345'))

def strint(s):
	def fn(x,y):
		return x * 10 +y
	return reduce(fn,map(int,s))

print strint('3321')

def str2int(s):
	return reduce(lambda x,y: x*10+y,map(int,s))

print str2int('1114')

print u'-----排序算法-----'

# 内置的sorted()函数可以对list进行排序
print sorted([17,213,12,3,453])

def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	return 0

print sorted([36,3,1,11,8,21],reversed_cmp)

print u'-----函数作为返回值-----'
def lazy_sum(* args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,3,5,7,9)
print f
print f()

print u'-----匿名函数-----'
#匿名函数 lambda x: x * x
# def f(x):
#    return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数，不用写return

f = lambda x: x * x
print f
print f(5)

print u'-----装饰器-----'
def now():
	print '2014-03-05'

print now.__name__

def log(func):
	def wrapper(*args,**kw):
		print 'call %s()' % func.__name__
		return func(*args,**kw)
	return wrapper

@log
def now():
	print '2014-03-05'

now()

#log()是一个decorator，返回一个函数

print u'-----偏函数-----'

#functools.partial的作用就是，把一个函数的某些参数（不管有没有默认值）给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# int2 = functools.partial(int, base=2)
# print int2('1010')